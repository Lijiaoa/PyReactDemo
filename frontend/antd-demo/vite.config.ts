import { defineConfig } from 'vite'
import react from '@vitejs/plugin-react'

// https://vitejs.dev/config/
export default defineConfig({
  plugins: [react()],
  build: {
    // transform: {
    //     "^.+\\.(jsx|js)?$": "babel"
    // },
    outDir: "../backend/client/build",
    emptyOutDir: true,
    sourcemap: true,
    minify: "terser",
    target: "esnext"
},
})
