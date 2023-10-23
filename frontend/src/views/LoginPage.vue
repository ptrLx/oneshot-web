<template>
    <base-layout page-title="Login" :hide-back-button=true>

        <div class="logo">
            <ion-avatar>
                <img alt="Silhouette of a person's head" src="https://ionicframework.com/docs/img/demos/avatar.svg" />
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
                    <ion-button @click="handleLogin" shape="round">Login</ion-button>
                </ion-col>
            </ion-row>
        </ion-grid>
    </base-layout>
</template>
  
<script lang="ts">
import { IonAvatar, IonButton, IonGrid, IonRow, IonCol, IonIcon, IonInput, useIonRouter, IonToast, toastController } from '@ionic/vue';
import { cameraOutline } from 'ionicons/icons';
import { defineComponent, ref } from 'vue';
import { ImageService, LoginService, UserService, Token, OpenAPI, ApiError } from '@/_generated/api-client';
import { useCookies } from 'vue3-cookies'
import { routerKey } from 'vue-router';

export default defineComponent({
    components: {
        IonAvatar,
        IonButton,
        IonGrid,
        IonRow,
        IonCol,
        IonIcon,
        IonInput
    },
    methods: {
        handleLogin() {

            // if (process.env === 'development') {
            OpenAPI.BASE = 'http://localhost:8200';
            // }
            // if (process.env === 'production') {
            //     OpenAPI.BASE = '/api';
            // }

            // var token: undefined | Token = undefined;

            LoginService.loginForAccessTokenLoginPost(
                {
                    username: this.username,
                    password: this.password
                }
            ).then((t) => {
                this.cookies.set("token", t.access_token);
                OpenAPI.TOKEN = t.access_token;
                this.requestUserInfo() // TODO: remove, for debugging
                console.log(t.access_token) // TODO: remove, for debugging

                this.router.push('/home');
            }).catch((e: ApiError) => {

                switch (e.status) {
                    case 401:
                        console.log("Unauthorized")

                        //TODO: change user/passwd field to red and play access denied animation
                        this.showToast()
                        break;
                    default:
                        console.log("Unknown error")
                        break;
                }
            })
        },
        requestUserInfo() {
            UserService.getUserMeUserMeGet().then((user) => {
                console.log(user.username)
            })
        },
        showToast() {
            toastController.create({
                message: 'Unknown username or password',
                duration: 2000,
                color: 'danger'
            }).then((toast) => {
                toast.present();
            });
        }

    },
    setup() {
        const { cookies } = useCookies();
        const username = ref<string>("");
        const password = ref<string>("");
        const router = useIonRouter();

        return {
            cameraOutline,
            cookies,
            username,
            password,
            router
        };
    },
});

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

  