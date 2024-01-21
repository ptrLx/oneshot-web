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

/* Other imports */
import BaseLayout from "./components/base/BaseLayout.vue"
import { globalCookiesConfig } from "vue3-cookies"
import { OpenAPI } from "@/_generated/api-client"
import { isPlatform } from "@ionic/vue"
import { createHead } from "@vueuse/head"
import { defineCustomElements } from "@ionic/pwa-elements/loader"

defineCustomElements(window)

globalCookiesConfig({
    expireTimes: "180DAYS", // define token expiration time
    //secure: true // true: only https works
})

// Set base URL for backend API calls
const nodeEnv = process.env.NODE_ENV
if (nodeEnv === "development") {
    // development (using the vite dev server)
    OpenAPI.BASE = "http://localhost:8200"
} else {
    // production

    // VITE_DEPLOYMENT_MODE decides whether to use the local backend or the remote backend.
    const VITE_DEPLOYMENT_MODE = import.meta.env.VITE_DEPLOYMENT_MODE || "SAME_HOST"
    if (VITE_DEPLOYMENT_MODE === "ANDROID_EMULATOR") {
        // See https://stackoverflow.com/questions/5528850/how-do-you-connect-localhost-in-the-android-emulator
        // For local connection of the android app it has to connect to the IP 10.0.2.2.
        OpenAPI.BASE = "http://10.0.2.2:8200"
    } else if (VITE_DEPLOYMENT_MODE === "ANDROID_REMOTE") {
        // todo remove this and let user configure this in the login screen
        OpenAPI.BASE = "https://osweb.ptrlx.de/api"
    } else {
        // SAME_HOST
        // Default is '/api' as this will connect to the same host where the frontend is served from and nginx will redirect to the backend.
        OpenAPI.BASE = "/api"
    }
}

const app = createApp(App).use(IonicVue).use(router).use(createHead())

// make base layout component known to all components
app.component("base-layout", BaseLayout)

router.isReady().then(() => {
    app.mount("#app")
})

// --- Accessibility ---
// Set viewport scalability dependiong on the platform
if (isPlatform("desktop")) {
    const viewport = document.querySelector("meta[name=viewport]")

    if (viewport) {
        viewport.setAttribute(
            "content",
            "minimum-scale=1, maximum-scale=5, initial-scale=1, user-scalable=yes, viewport-fit=cover, width=device-width",
        )
    }
}
