import { OpenAPI } from "@/_generated/api-client"
import { getApiUrlFromCookie, getTokenFromCookie, setApiUrl } from "@/service/authService"

export default async function setup_api_client() {
    const token = await getTokenFromCookie()
    let url = await getApiUrlFromCookie()

    //// let enforceHTTPS = true

    if (url == undefined || url === "") {
        // Set base URL for backend API calls
        const nodeEnv = process.env.NODE_ENV
        if (nodeEnv === "development") {
            // Development (using the vite dev server)
            url = "http://localhost:8200"
            //// enforceHTTPS = false
        } else {
            // VITE_DEPLOYMENT_MODE decides whether to use the local backend or the remote backend.
            const VITE_DEPLOYMENT_MODE = import.meta.env.VITE_DEPLOYMENT_MODE || "SAME_HOST"
            if (VITE_DEPLOYMENT_MODE === "ANDROID_EMULATOR") {
                // Development (using the android emulator)

                // See https://stackoverflow.com/questions/5528850/how-do-you-connect-localhost-in-the-android-emulator
                // For local connection of the android app it has to connect to the IP 10.0.2.2.
                url = "http://10.0.2.2:8200"
                //// enforceHTTPS = false
            } else if (VITE_DEPLOYMENT_MODE === "ANDROID_PROD") {
                // Production
                // url has to be set in the LoginPage
            } else {
                // VITE_DEPLOYMENT_MODE === SAME_HOST
                //Production

                // Default is '/api' as this will connect to the same host where the frontend is served from and nginx will redirect to the backend.
                url = "/api"
            }
        }

        setApiUrl(url)
    }

    OpenAPI.BASE = url // Base URL is either set now or null (will be set on login page)
    OpenAPI.TOKEN = token // Token is either set or null (will be set on login page)

    //// globalCookiesConfig({
    ////     expireTimes: "180DAYS", // Token expiration time
    ////     secure: enforceHTTPS, // true: only https works
    //// })
}
