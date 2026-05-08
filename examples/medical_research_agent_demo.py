"""Medical research assistant demo for the OpenAI Agents SDK tutorial.

Run without network/API usage:
    python3 examples/medical_research_agent_demo.py --offline

Run with the real SDK:
    export OPENAI_API_KEY="sk-..."
    python3 examples/medical_research_agent_demo.py --live
"""

from __future__ import annotations

import argparse
import asyncio
import os
from dataclasses import dataclass


SAFETY_NOTE = (
    "安全边界：本示例只做医学科研辅助，不提供诊断、治疗、分诊、用药或患者个体化建议。"
)


@dataclass(frozen=True)
class OfflineBrief:
    research_question: str
    method_suggestion: str
    key_findings: str
    risk_note: str


def pubmed_search_stub(query: str) -> str:
    """Return a deterministic literature-search placeholder for teaching."""
    return (
        f"PubMed 检索占位：query={query!r}。真实项目中应接入 NCBI E-utilities、"
        "机构数据库或人工导出的文献表，并保留检索日期、关键词和纳排标准。"
    )


def explain_scale(scale_name: str) -> str:
    """Explain a medical scale at research-planning level."""
    normalized = scale_name.strip().lower()
    if normalized in {"apache ii", "apache2", "apache-ii"}:
        return "APACHE II 常用于 ICU 病情严重程度评估；科研中要说明评分时间窗和缺失值处理。"
    if normalized in {"sofa"}:
        return "SOFA 常用于器官功能衰竭程度评估；科研中要明确基线、动态变化和评分时间点。"
    return f"{scale_name}：请先确认量表适用人群、评分范围、临床含义和中文/本地验证版本。"


def format_research_brief(question: str, method: str, evidence: str) -> OfflineBrief:
    """Format the same four fields used by the structured-output example."""
    return OfflineBrief(
        research_question=question,
        method_suggestion=method,
        key_findings=evidence,
        risk_note="该建议仅用于研究设计草案，不能替代统计师、伦理审查或临床专家判断。",
    )


def run_offline_demo() -> None:
    """Show the workflow shape without importing or calling the SDK."""
    print("OpenAI Agents SDK 医疗科研助手：离线理解模式\n")
    print(SAFETY_NOTE)
    print("\n1. Agent 定角色：主助手负责把问题转成科研计划。")
    print("2. Runner 跑流程：把用户问题交给主助手执行。")
    print("3. Tools 做事情：本地函数可补充检索、量表、格式化能力。")
    print("4. Agents-as-tools 分专家：文献、统计、写作助手各做一小块。")
    print("5. Guardrails 守边界：患者个体化诊疗建议要拒绝或转人工。")
    print("6. Sessions 留记忆：同一课题的多轮上下文可保存。")
    print("7. Tracing 查过程：看清模型、工具、handoff、guardrail 的执行链路。")

    evidence = pubmed_search_stub("sepsis AND SOFA AND mortality")
    scale = explain_scale("SOFA")
    brief = format_research_brief(
        question="SOFA 动态变化是否能预测脓毒症 ICU 患者 28 天死亡？",
        method="回顾性队列研究；先做描述统计，再考虑多变量 logistic 回归或 Cox 模型。",
        evidence=f"{evidence}\n{scale}",
    )

    print("\n离线结构化输出示例：")
    print(f"- 研究问题：{brief.research_question}")
    print(f"- 方法建议：{brief.method_suggestion}")
    print(f"- 证据提示：{brief.key_findings}")
    print(f"- 风险提示：{brief.risk_note}")


async def run_live_demo() -> None:
    """Run the real OpenAI Agents SDK version."""
    if not os.getenv("OPENAI_API_KEY"):
        raise SystemExit("请先设置 OPENAI_API_KEY，再运行 --live。")

    from pydantic import BaseModel, Field
    from agents import (
        Agent,
        GuardrailFunctionOutput,
        InputGuardrailTripwireTriggered,
        RunConfig,
        RunContextWrapper,
        Runner,
        SQLiteSession,
        TResponseInputItem,
        function_tool,
        input_guardrail,
        trace,
    )

    class ResearchBrief(BaseModel):
        research_question: str = Field(description="一句话研究问题")
        method_suggestion: str = Field(description="推荐的研究设计或统计方法")
        key_findings: str = Field(description="文献或工具得到的要点")
        risk_note: str = Field(description="安全边界、不确定性和人工复核提醒")

    class MedicalRiskCheck(BaseModel):
        patient_specific_advice: bool = Field(
            description="用户是否在请求诊断、治疗、用药、分诊或患者个体化建议"
        )
        reasoning: str = Field(description="判断理由")

    @function_tool
    def search_literature(query: str) -> str:
        """Search literature placeholder for a biomedical research question."""
        return pubmed_search_stub(query)

    @function_tool
    def explain_medical_scale(scale_name: str) -> str:
        """Explain a clinical scale for research planning, not clinical advice."""
        return explain_scale(scale_name)

    guardrail_agent = Agent(
        name="医疗安全边界检查",
        instructions=(
            "判断用户是否请求诊断、治疗、分诊、用药或患者个体化医疗建议。"
            "科研设计、文献总结、统计方案、论文写作不算患者个体化医疗建议。"
        ),
        output_type=MedicalRiskCheck,
    )

    @input_guardrail
    async def medical_safety_guardrail(
        ctx: RunContextWrapper[None],
        agent: Agent,
        input: str | list[TResponseInputItem],
    ) -> GuardrailFunctionOutput:
        result = await Runner.run(guardrail_agent, input, context=ctx.context)
        return GuardrailFunctionOutput(
            output_info=result.final_output,
            tripwire_triggered=result.final_output.patient_specific_advice,
        )

    literature_agent = Agent(
        name="文献助手",
        instructions="你只负责把医学科研问题转成检索思路，并总结证据线索；不要给临床诊疗建议。",
        tools=[search_literature],
    )

    statistics_agent = Agent(
        name="统计助手",
        instructions=(
            "你只负责研究设计和统计分析建议。说明变量、结局、混杂因素、缺失值和人工复核点。"
        ),
        tools=[explain_medical_scale],
    )

    writing_agent = Agent(
        name="写作助手",
        instructions="你只负责把科研计划写成清晰的论文草案结构；保留不确定性和待确认事项。",
    )

    orchestrator = Agent(
        name="医疗科研主助手",
        instructions=(
            "你是医疗科研助手，不是临床医生。你要调用专家工具，输出研究设计草案。"
            "必须明确：这不是诊断或治疗建议，最终需要研究者、统计师和伦理审查复核。"
        ),
        input_guardrails=[medical_safety_guardrail],
        tools=[
            literature_agent.as_tool(
                tool_name="literature_helper",
                tool_description="为医学科研问题提供文献检索思路和证据线索。",
            ),
            statistics_agent.as_tool(
                tool_name="statistics_helper",
                tool_description="为医学科研问题提供研究设计和统计分析建议。",
            ),
            writing_agent.as_tool(
                tool_name="writing_helper",
                tool_description="把科研设计整理成论文草案结构。",
            ),
        ],
        output_type=ResearchBrief,
    )

    session = SQLiteSession("demo_sepsis_sofa_project")
    prompt = (
        "我想做一个回顾性研究：SOFA 动态变化是否能预测脓毒症 ICU 患者 28 天死亡？"
        "请给我一个非常简洁的研究计划。"
    )

    try:
        with trace("medical_research_agent_demo"):
            result = await Runner.run(
                orchestrator,
                prompt,
                session=session,
                run_config=RunConfig(workflow_name="medical_research_agent_demo"),
            )
    except InputGuardrailTripwireTriggered:
        print("Guardrail 已触发：这个请求超出了科研辅助边界。")
        return

    output = result.final_output
    print("真实 SDK 结构化输出：")
    print(f"- 研究问题：{output.research_question}")
    print(f"- 方法建议：{output.method_suggestion}")
    print(f"- 证据提示：{output.key_findings}")
    print(f"- 风险提示：{output.risk_note}")
    print("\n可到 OpenAI Dashboard 的 Traces 页面查看本次运行链路。")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="OpenAI Agents SDK 医疗科研助手示例")
    mode = parser.add_mutually_exclusive_group()
    mode.add_argument("--offline", action="store_true", help="不调用 SDK，仅演示结构")
    mode.add_argument("--live", action="store_true", help="调用真实 OpenAI Agents SDK")
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    if args.live:
        asyncio.run(run_live_demo())
    else:
        run_offline_demo()


if __name__ == "__main__":
    main()

