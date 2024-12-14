// https://nuxt.com/docs/api/configuration/nuxt-config
export default defineNuxtConfig({
  app: {
      head: {
          meta: [
              {name: "theme-color", content: "#326CB3"},
          ],
          link: [
              {rel: 'icon', href: `/favicon.ico`, sizes: "48x48"},
              {rel: 'apple-touch-icon', href: `/apple-touch-icon-180x180.png`},
          ],
      },
  },
  modules: ['@vite-pwa/nuxt'],
  pwa: {
      registerType: "autoUpdate", // 多分なくてもよい
      manifest: {
          name: 'アプリ名',
          description: "アプリ説明",
          theme_color: "#326CB3", // テーマカラー
          lang: "ja",
          short_name: "P!NT",
          start_url: "/",
          display: "standalone",
          background_color: "#ffffff",
          "icons": [
            {
              "src": "pwa-64x64.png",
              "sizes": "64x64",
              "type": "image/png"
            },
            {
              "src": "pwa-192x192.png",
              "sizes": "192x192",
              "type": "image/png"
            },
            {
              "src": "pwa-512x512.png",
              "sizes": "512x512",
              "type": "image/png"
            },
            {
              "src": "maskable-icon-512x512.png",
              "sizes": "512x512",
              "type": "image/png",
              "purpose": "maskable"
            }
          ]
      },
      workbox: { // なんか必要
          navigateFallback: null
      },
      devOptions: { // テスト用
          enabled: true,
          type: "module"
      },
  },
})