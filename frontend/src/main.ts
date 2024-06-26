import { createApp } from "vue"
import App from "./App.vue"
import router from "./router"

import { IonicVue } from "@ionic/vue"

/* Core CSS required for Ionic components to work properly */
import "@ionic/vue/css/core.css"

/* Basic CSS for apps built with Ionic */
import "@ionic/vue/css/normalize.css"
import "@ionic/vue/css/structure.css"
import "@ionic/vue/css/typography.css"

/* Optional CSS utils that can be commented out */
import "@ionic/vue/css/padding.css"
import "@ionic/vue/css/float-elements.css"
import "@ionic/vue/css/text-alignment.css"
import "@ionic/vue/css/text-transformation.css"
import "@ionic/vue/css/flex-utils.css"
import "@ionic/vue/css/display.css"

/* Theme variables */
import "./theme/variables.css"

/* Boot scripts */
import setup_api_client from "./boot/apiClient"

/* Other imports */
import BaseLayout from "./components/base/BaseLayout.vue"

import { isPlatform } from "@ionic/vue"
import { createHead } from "@vueuse/head"
import { defineCustomElements } from "@ionic/pwa-elements/loader"
import { createPinia } from "pinia"

defineCustomElements(window)

setup_api_client().then(() => {
    const pinia = createPinia()
    const app = createApp(App).use(IonicVue).use(router).use(createHead())
    app.use(pinia)

    // make base layout component known to all components
    app.component("base-layout", BaseLayout)

    router.isReady().then(() => {
        app.mount("#app")
    })

    // --- Accessibility ---
    // Set viewport scalability depending on the platform
    if (isPlatform("desktop")) {
        const viewport = document.querySelector("meta[name=viewport]")

        if (viewport) {
            viewport.setAttribute(
                "content",
                "minimum-scale=1, maximum-scale=5, initial-scale=1, user-scalable=yes, viewport-fit=cover, width=device-width",
            )
        }
    }
})
