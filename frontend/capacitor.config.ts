import { CapacitorConfig } from "@capacitor/cli"

const config: CapacitorConfig = {
    appId: "de.ptrlx.oneshotweb",
    appName: "OneShot Web",
    webDir: "dist",
    server: {
        androidScheme: "http", // do not change this to https. Otherwise the connection (android emulator - local api) will not work anymore.
        hostname: "localhost",
    },

    plugins: {
        CapacitorCookies: {
            enabled: true,
        },
    },
}

export default config
