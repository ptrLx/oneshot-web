<template>
    <base-layout page-title="Login" :hide-back-button=true>

        <div class="logo">
            <ion-avatar>
                <img alt="OneShot logo" src="/icons/512.png" />
            </ion-avatar>
        </div>
        <!-- Login Section -->
        <ion-grid class="ion-text-center">
            <ion-row>
                <ion-col size="12">
                    <ion-input type="text" label="Username" label-placement="floating" fill="outline" shape="round"
                        v-model="username" placeholder="Enter Username">
                    </ion-input>
                </ion-col>
            </ion-row>
            <ion-row>
                <ion-col size="12">
                    <ion-input type="password" label="Password" label-placement="floating" fill="outline" shape="round"
                        v-model="password" placeholder="Enter Password">
                    </ion-input>
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
  
<script lang="ts">
import { IonAvatar, IonButton, IonGrid, IonRow, IonCol, IonInput, useIonRouter, toastController } from "@ionic/vue"
import { cameraOutline } from "ionicons/icons"
import { defineComponent, ref } from "vue"
import { UserService, OpenAPI, ApiError } from "@/_generated/api-client"
import { useCookies } from "vue3-cookies"
import { useThemeService } from "@/composables/themeService"

export default defineComponent({
    components: {
        IonAvatar,
        IonButton,
        IonGrid,
        IonRow,
        IonCol,
        IonInput
    },
    setup() {
        const { cookies } = useCookies()
        const username = ref<string>("")
        const password = ref<string>("")
        const router = useIonRouter()

        useThemeService(true) // Set theme to media preference

        const showToastFail = (msg: string) => {
            toastController.create({
                message: msg,
                duration: 2000,
                color: "danger"
            }).then((toast) => {
                toast.present()
            })
        }

        const handleLogin = () => {
            // if (process.env === 'development') {

            // }
            // if (process.env === 'production') {
            //     OpenAPI.BASE = '/api';
            // }

            // var token: undefined | Token = undefined;

            UserService.loginForAccessTokenLoginPost(
                {
                    username: username.value,
                    password: password.value
                }
            ).then((t) => {
                cookies.set("token", t.access_token)
                OpenAPI.TOKEN = t.access_token

                router.push("/home")
            }, (e: ApiError) => {
                if (typeof e.body === "string") {
                    showToastFail(e.body) // Most likely a internal server error (e.g. the database not reachable)
                } else if (Array.isArray(e.body.detail)) {
                    showToastFail("Username and password is required") // Field is missing
                }
                else {
                    showToastFail(e.body.detail) // Incorrect username or password
                }
            })
        }

        return {
            cameraOutline,
            cookies,
            username,
            password,
            router,
            handleLogin
        }
    },
})

</script>

<style scoped>
.logo {
    display: flex;
    justify-content: center;
    align-items: center;
    margin: 60px;
    scale: 2.0;
}

ion-button {
    width: 80%;
    height: 50px;
    margin-top: 20px;
}

ion-icon {
    scale: 2.0;
}
</style>

  