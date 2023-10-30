<template>
    <base-layout page-title="Profile" default-back-link="/home">

        <div class="flex-container">
            <ion-avatar class="profile-avatar">
                <ion-img src="https://ionicframework.com/docs/img/demos/avatar.svg"></ion-img>
                <ion-button class="change-profile-pic-button" shape="round">
                    <ion-icon slot="icon-only" :icon="cameraOutline"></ion-icon>
                </ion-button>
            </ion-avatar>
        </div>
        <ion-title class="ion-text-center">
            <h1>Username</h1>
        </ion-title>

        <!-- Buttons Section -->
        <ion-grid class="ion-text-center">
            <ion-row>
                <ion-col size="12">
                    <ion-button shape="round">Toggle theme</ion-button>
                </ion-col>
            </ion-row>
            <ion-row>
                <ion-col size="12">
                    <ion-button shape="round">Export database</ion-button>
                </ion-col>
            </ion-row>
            <ion-row>
                <ion-col size="12">
                    <ion-button shape="round">Import database</ion-button>
                </ion-col>
            </ion-row>
            <ion-row>
                <ion-col size="12">
                    <ion-button shape="round">Change password</ion-button>
                </ion-col>
            </ion-row>
            <ion-row>
                <ion-col size="12">
                    <ion-button @click="handleLogout" shape="round">Log out</ion-button>
                </ion-col>
            </ion-row>
            <ion-row>
                <ion-col size="12">
                    <ion-button shape="round">Feedback</ion-button>
                </ion-col>
            </ion-row>
            <ion-row>
                <ion-col size="12">
                    <ion-button shape="round">Open Source Licence</ion-button>
                </ion-col>
            </ion-row>
        </ion-grid>


    </base-layout>
</template>
  
<script lang="ts">
import { IonAvatar, IonButton, IonGrid, IonRow, IonCol, IonIcon, IonTitle, useIonRouter, IonImg } from '@ionic/vue';
import { ImageService, LoginService, UserService, Token, OpenAPI, ApiError } from '@/_generated/api-client';
import { cameraOutline, constructOutline, image } from 'ionicons/icons';
import { defineComponent, ref } from 'vue';
import { useCookies } from 'vue3-cookies'
import ProfileComponent from '@/components/ProfileComponent.vue';

export default defineComponent({
    components: {
        IonAvatar,
        IonButton,
        IonGrid,
        IonRow,
        IonCol,
        IonIcon,
        IonTitle,
        IonImg
    },
    setup() {

        const router = useIonRouter();
        const { cookies } = useCookies();
        OpenAPI.TOKEN = cookies.get("token");

        const handleLogout = () => {
            cookies.remove("token");
            router.push('/login');
        }

        //TODO Get profile picture from UserService.getUserProfileImgUserProfileimgGet 

        return {
            cameraOutline,
            router,
            cookies,
            handleLogout
        };
    },
});

</script>

<style scoped>
.flex-container {
    display: flex;
    justify-content: center;
    align-items: center;
}

.profile-avatar {
    margin: 60px;
    scale: 2.0;
}

.change-profile-pic-button {
    position: absolute;
    top: 18px;
    left: 18px;
    scale: 0.3;
    height: 70px;
    width: 70px;
}

ion-button {
    width: 80%;
    height: 50px;
}

ion-icon {
    scale: 2.0;
}
</style>

  