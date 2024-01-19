import legacy from '@vitejs/plugin-legacy'
import vue from '@vitejs/plugin-vue'
import path from 'path'
import { defineConfig } from 'vite'
import { VitePWA } from 'vite-plugin-pwa'
import viteCompression from 'vite-plugin-compression'

// https://vitejs.dev/config/
export default defineConfig({
  plugins: [
    vue(),
    legacy(),
    /* Do not enable text compression (to improve performance score).
     * not in development mode (npm run dev)
     * Note: Effect only visible in production mode (npm run preview),
     * It breaks the android build for some reason (Error is "duplicate resources"). Its not needed anyway as nginx will compress the files.
     * viteCompression()
     */
    VitePWA({
      manifest: {
        name: 'OneShot Web',
        short_name: 'OneShot',
        theme_color: '#feba4b',
        background_color: '#000000',
        display: 'standalone',
        icons: [
          {
            src: "/icons/512.png",
            sizes: "512x512",
            type: "image/png",
            purpose: "any maskable",
          },
          {
            src: "/icons/1024.png",
            sizes: "1024x1024",
            type: "image/png",
            purpose: "any maskable",
          }
        ]
      },
      devOptions: {
        enabled: true
        /* other options */
      }
    })
  ],
  resolve: {
    alias: {
      '@': path.resolve(__dirname, './src'),
    },
  },
  define: {
    'process.env.VITE_DEPLOYMENT_MODE': JSON.stringify(process.env.VITE_DEPLOYMENT_MODE),
  },
  test: {
    globals: true,
    environment: 'jsdom'
  },
  build: {
    rollupOptions: {
      output: {
        manualChunks(id) {
          if (id.includes('node_modules')) {
            return id.toString().split('node_modules/')[1].split('/')[0].toString();
          }
        }
      }
    }
  }
})
