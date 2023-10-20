<template>
    <base-layout page-title="Profile" default-back-link="/home">

        <div class="profile-avatar">
            <ion-avatar>
                <img alt="Silhouette of a person's head" src="https://ionicframework.com/docs/img/demos/avatar.svg" />
                <div>
                    <ion-button class="change-profile-pic-button" shape="round">
                        <ion-icon slot="icon-only" :icon="cameraOutline"></ion-icon>
                    </ion-button>
                </div>
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
                    <ion-button shape="round">Log out</ion-button>
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
import { IonAvatar, IonButton, IonGrid, IonRow, IonCol, IonIcon } from '@ionic/vue';
import { cameraOutline } from 'ionicons/icons';
import { defineComponent } from 'vue';

export default defineComponent({
    components: {
        IonAvatar,
        IonButton,
        IonGrid,
        IonRow,
        IonCol,
        IonIcon
    },
    setup() {
        return { cameraOutline };
    },
});
</script>

<style scoped>
.profile-avatar {
    display: flex;
    justify-content: center;
    align-items: center;
    margin: 60px;
    scale: 2.0;
}

.change-profile-pic-button {
    position: absolute;
    top: 15px;
    right: 840px;
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

  