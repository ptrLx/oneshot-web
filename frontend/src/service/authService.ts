import { OpenAPI } from "@/_generated/api-client"
import { CapacitorCookies } from "@capacitor/core"

export async function getTokenFromCookie() {
    const cookies = await CapacitorCookies.getCookies()
    return cookies.token
}

export async function getApiUrlFromCookie() {
    const cookies = await CapacitorCookies.getCookies()
    return cookies.apiURL
}

export async function setApiUrl(apiURL: string) {
    await CapacitorCookies.setCookie({
        key: "apiURL",
        value: apiURL,
    })
    OpenAPI.BASE = apiURL
}

export async function setToken(token: string) {
    const date = new Date()
    const days = 180
    date.setTime(date.getTime() + days * 24 * 60 * 60 * 1000)
    await CapacitorCookies.setCookie({
        key: "token",
        value: token,
        expires: date.toUTCString(),
    })
    OpenAPI.TOKEN = token
}

export async function deleteToken() {
    await CapacitorCookies.deleteCookie({
        key: "token",
    })
    OpenAPI.TOKEN = undefined
}

//// const setCapacitorCookie = async () => {
////     await CapacitorCookies.setCookie({
////         url: "http://example.com",
////         key: "language",
////         value: "en",
////     })
//// }

//// const deleteCookie = async () => {
////     await CapacitorCookies.deleteCookie({
////         url: "https://example.com",
////         key: "language",
////     })
//// }

//// const clearCookiesOnUrl = async () => {
////     await CapacitorCookies.clearCookies({
////         url: "https://example.com",
////     })
//// }

//// const clearAllCookies = async () => {
////     await CapacitorCookies.clearAllCookies()
//// }
