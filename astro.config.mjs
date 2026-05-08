import { defineConfig } from 'astro/config';
import starlight from '@astrojs/starlight';

export default defineConfig({
  site: 'https://2023Anita.github.io',
  base: '/openai-agents-medical-research-guide',
  integrations: [
    starlight({
      title: 'OpenAI Agents SDK for Medical Research',
      logo: {
        src: './src/assets/brand/logo.png',
        alt: 'OpenAI Agents SDK for Medical Research',
      },
      social: [
        {
          icon: 'github',
          label: 'GitHub',
          href: 'https://github.com/2023Anita/openai-agents-medical-research-guide',
        },
      ],
      defaultLocale: 'zh',
      locales: {
        zh: {
          label: '中文',
          lang: 'zh-CN',
        },
        en: {
          label: 'English',
          lang: 'en-US',
        },
        ja: {
          label: '日本語',
          lang: 'ja-JP',
        },
      },
      editLink: {
        baseUrl: 'https://github.com/2023Anita/openai-agents-medical-research-guide/edit/main/',
      },
      customCss: ['./src/styles/custom.css'],
      sidebar: [
        {
          label: 'Course',
          translations: {
            zh: '课程',
            en: 'Course',
            ja: 'コース',
          },
          items: [{ autogenerate: { directory: 'guides' } }],
        },
      ],
    }),
  ],
});
