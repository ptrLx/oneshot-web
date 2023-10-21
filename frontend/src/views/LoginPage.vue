<template>
    <base-layout page-title="Login" hide-back-button="true">

        <div class="logo">
            <ion-avatar>
                <img alt="Silhouette of a person's head" src="https://ionicframework.com/docs/img/demos/avatar.svg" />
            </ion-avatar>
        </div>
        <!-- Login Section -->
        <ion-grid class="ion-text-center">
            <ion-row>
                <ion-col size="12">
                    <ion-input label="Username" label-placement="floating" fill="outline" shape="round"
                        placeholder="Enter Username"></ion-input>
                </ion-col>
            </ion-row>
            <ion-row>
                <ion-col size="12">
                    <ion-input label="Password" label-placement="floating" fill="outline" shape="round"
                        placeholder="Enter Password"></ion-input>
                </ion-col>
            </ion-row>
            <ion-row>
                <ion-col size="12">
                    <ion-button shape="round">Login</ion-button>
                </ion-col>
            </ion-row>
        </ion-grid>


    </base-layout>
</template>
  
<script lang="ts">
import { IonAvatar, IonButton, IonGrid, IonRow, IonCol, IonIcon, IonInput } from '@ionic/vue';
import { cameraOutline } from 'ionicons/icons';
import { defineComponent } from 'vue';

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
    setup() {
        return { cameraOutline };
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

  