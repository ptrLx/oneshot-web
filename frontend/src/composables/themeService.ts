import { theme } from "@/composables/store"
import { onMounted } from "vue"

export const useThemeService = (mediaPreferred = true) => {
    onMounted(() => {
        if (mediaPreferred) {
            setInitialTheme()
        }
    })

    const setInitialTheme = () => {
        const savedTheme = theme.getTheme()
        if (theme.isSet()) {
            console.log("theme is set")
            document.body.classList[savedTheme === "dark" ? "add" : "remove"]("dark")
        } else {
            // No theme set, use media preferred theme
            if (window.matchMedia && window.matchMedia("(prefers-color-scheme: dark)").matches) {
                document.body.classList.add("dark")
            }
        }
    }

    const toggleTheme = () => {
        const isDark = document.body.classList.toggle("dark")
        theme.setTheme(isDark ? "dark" : "light")
        console.log("theme: ", theme.getTheme())
    }

    return {
        setInitialTheme,
        toggleTheme,
    }
}
