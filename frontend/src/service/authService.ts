import { OpenAPI, UserService } from "@/_generated/api-client"
import { useProfileStore } from "@/store/profileStore"
import { CapacitorCookies } from "@capacitor/core"

export async function loginUser(apiURL: string, username: string, password: string) {
    const profileStore = useProfileStore()

    setApiUrl(apiURL)

    return UserService.loginForAccessTokenLoginPost({
        username: username,
        password: password,
    }).then((t) => {
        profileStore.userName = username
        setToken(t.access_token)
    })
}

export async function changeUserPw(oldPw: string, newPw: string) {
    const p = UserService.changeUserPasswordUserChpwPost(oldPw, newPw)
    deleteToken()
    return p
}

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

async function setToken(token: string) {
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
