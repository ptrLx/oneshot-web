<template>
    <ion-page>
        <ion-header>
            <ion-toolbar>
                <ion-buttons slot="start">
                    <ion-back-button v-if="hideBackButton == false" :default-href="defaultBackLink" />
                </ion-buttons>
                <ion-title> {{ pageTitle }}</ion-title>
                <ion-buttons slot="end">
                    <slot name="custom-buttons"></slot>
                </ion-buttons>
            </ion-toolbar>
        </ion-header>
        <ion-content :fullscreen="fullscreen">
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
    props: {
        pageTitle: {
            type: String,
            required: false
        },
        defaultBackLink: {
            type: String,
            default: '/home'
        },
        hideBackButton: {
            type: Boolean,
            default: false
        },
        fullscreen: {
            type: Boolean,
            default: true
        }
    },
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

