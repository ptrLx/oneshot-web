<template>
    <ion-page>
        <ion-header>
            <ion-toolbar>
                <ion-buttons slot="start">
                    <ion-back-button :default-href="defaultBackLink"></ion-back-button>
                </ion-buttons>
                <ion-title> {{ pageTitle }}</ion-title>
            </ion-toolbar>
        </ion-header>
        <ion-content fullscreen="true">
            <slot />
        </ion-content>
    </ion-page>
</template>

<script lang="ts">
import {
    IonPage,
    IonHeader,
    IonTitle,
    IonToolbar,
    IonContent,
    IonBackButton,
    IonButtons
} from '@ionic/vue';
import { defineComponent } from 'vue';

export default defineComponent({
    props: ['pageTitle', "defaultBackLink"],
    components: {
        IonPage,
        IonHeader,
        IonTitle,
        IonToolbar,
        IonContent,
        IonBackButton,
        IonButtons
    },
});
</script>

<style scoped>
ion-toolbar {
    --background: transparent;
    --ion-color-base: transparent !important;
}
</style>

