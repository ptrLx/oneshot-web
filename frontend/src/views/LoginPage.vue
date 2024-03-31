<template>
    <base-layout page-title="Login" :hide-back-button="true">
        <ion-grid class="ion-text-center">
            <div class="logo">
                <ion-avatar>
                    <img alt="OneShot logo" src="/icons/512.png" />
                </ion-avatar>
            </div>
            <ion-row>
                <ion-col size="12">
                    <ion-input
                        v-if="openAPIBaseURL == undefined || openAPIBaseURL === ''"
                        type="text"
                        label="Link to API"
                        label-placement="floating"
                        fill="outline"
                        shape="round"
                        v-model="apiURL"
                        placeholder="oneshot.example.com/api"
                    />
                </ion-col>
                <ion-col size="12">
                    <ion-input
                        type="text"
                        label="Username"
                        label-placement="floating"
                        fill="outline"
                        shape="round"
                        v-model="username"
                    />
                </ion-col>
            </ion-row>
            <ion-row>
                <ion-col size="12">
                    <ion-input
                        type="password"
                        label="Password"
                        label-placement="floating"
                        fill="outline"
                        shape="round"
                        v-model="password"
                    />
                </ion-col>
            </ion-row>
            <ion-row>
                <ion-col size="12">
                    <ion-button @click="handleLogin()" shape="round">Login</ion-button>
                </ion-col>
            </ion-row>
        </ion-grid>
    </base-layout>
</template>

<style scoped>
    .logo {
        display: flex;
        justify-content: center;
        align-items: center;
        margin: 60px;
        scale: 2;
    }

    ion-button {
        width: 80%;
        height: 50px;
        margin-top: 20px;
    }

    ion-icon {
        scale: 2;
    }
</style>

<script lang="ts">
    import {
        IonAvatar,
        IonButton,
        IonGrid,
        IonRow,
        IonCol,
        IonInput,
        useIonRouter,
        toastController,
    } from "@ionic/vue"
    import { cameraOutline } from "ionicons/icons"
    import { defineComponent, ref } from "vue"
    import { OpenAPI, ApiError } from "@/_generated/api-client"
    import { useThemeService } from "@/composables/themeService"
    import { loginUser, setApiUrl } from "@/service/authService"

    export default defineComponent({
        components: {
            IonAvatar,
            IonButton,
            IonGrid,
            IonRow,
            IonCol,
            IonInput,
        },
        setup() {
            const apiURL = ref<string | undefined>(OpenAPI.BASE)
            const username = ref<string | undefined>(undefined)
            const password = ref<string | undefined>(undefined)
            const router = useIonRouter()

            const openAPIBaseURL = ref<string>(OpenAPI.BASE)

            useThemeService(true) // Set theme to media preference

            if (OpenAPI.BASE != undefined && OpenAPI.BASE !== "" && OpenAPI.TOKEN != undefined) {
                router.push("/home")
            }

            const showToastFail = (msg: string) => {
                toastController
                    .create({
                        message: msg,
                        duration: 2000,
                        color: "danger",
                    })
                    .then((toast) => {
                        toast.present()
                    })
            }

            function handleLogin() {
                if (apiURL.value == undefined) {
                    showToastFail("Api URL is required")
                } else if (username.value == undefined || password.value == undefined) {
                    showToastFail("Username and password is required")
                } else {
                    loginUser(apiURL.value, username.value, password.value).then(
                        () => {
                            router.push("/home")
                        },
                        (e: ApiError) => {
                            if (typeof e.body === "string") {
                                showToastFail(e.body) // Most likely a internal server error (e.g. the database not reachable)
                            } else if (Array.isArray(e.body.detail)) {
                                showToastFail("Username and password is required") // Field is missing
                            } else {
                                showToastFail(e.body.detail) // Incorrect username or password
                            }
                        },
                    )
                }
            }
            return {
                cameraOutline,
                username,
                password,
                router,
                handleLogin,
                openAPIBaseURL,
                apiURL,
            }
        },
    })
</script>
