<template>
    <card>
        <ion-title>Capture Today</ion-title>
        <ion-grid>
            <ion-row>
                <ion-col size="6">
                    <ion-button shape="round">Capture</ion-button>
                </ion-col>
                <ion-col size="6">
                    <ion-button shape="round">Upload</ion-button>
                </ion-col>
            </ion-row>
        </ion-grid>
    </card>
</template>

<script lang="ts">

import { IonCard, IonButton, IonTitle, IonGrid, IonRow, IonCol } from '@ionic/vue';
import { defineComponent } from 'vue';
import Card from '@/components/Card.vue';

export default defineComponent({
    components: {
        Card,
        IonCard,
        IonButton,
        IonTitle,
        IonGrid,
        IonRow,
        IonCol
    }
});

</script>

<style scoped>
.ion-title,
ion-title {
    margin-top: 10px;
    font-size: 1rem;
    color: var(--ion-color-primary-contrast);
}

.ion-button,
ion-button {
    margin-top: 30px;
    transform: scale(1.2);
    width: 70%;
}
</style>

