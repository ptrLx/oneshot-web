<template>
    <card cardTitle="Capture Today">
        <ion-grid>
            <ion-row>
                <ion-col size="6">
                    <ion-button shape="round" @click="handleCapture">Capture</ion-button>
                </ion-col>
                <ion-col size="6">
                    <ion-button shape="round" @click="handleUpload">Upload</ion-button>
                </ion-col>
            </ion-row>
        </ion-grid>
    </card>
</template>

<script lang="ts">
    import { IonButton, IonTitle, IonGrid, IonRow, IonCol } from "@ionic/vue"
    import { defineComponent } from "vue"
    import Card from "@/components/Card.vue"
    import router from "@/router"

    export default defineComponent({
        components: {
            Card,
            IonButton,
            IonGrid,
            IonRow,
            IonCol,
        },
        setup() {
            const handleCapture = () => {
                router.push({
                    name: "UploadImage",
                    query: { action: "capture" },
                })
            }
            const handleUpload = () => {
                router.push({
                    name: "UploadImage",
                    query: { action: "pick" },
                })
            }
            return {
                handleCapture,
                handleUpload,
            }
        },
    })
</script>

<style scoped>
    .ion-title,
    ion-title {
        margin-top: 10px;
        font-size: 1rem;
        color: var(--ion-color-dark-contrast);
    }

    .ios ion-title {
        display: block;
        padding-inline: 0px;
        font-size: 1rem;
    }

    .ios ion-grid {
        margin-top: 0px;
    }

    .ion-button,
    ion-button {
        margin-top: 0px;
        transform: scale(1.2);
        width: 70%;
    }
</style>
