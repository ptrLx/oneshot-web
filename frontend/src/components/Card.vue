<template>
    <ion-card class="full-width-card">

        <ion-card-header v-if="cardTitle || cardSubtitle">
            <ion-card-title> {{ cardTitle }} </ion-card-title>
            <ion-card-subtitle> {{ cardSubtitle }}</ion-card-subtitle>
        </ion-card-header>

        <slot></slot>

    </ion-card>
</template>
<script lang="ts">
import { defineComponent } from "vue"
import { IonCard, IonCardHeader, IonCardSubtitle, IonCardTitle } from "@ionic/vue"

import "swiper/css"
import "@ionic/vue/css/ionic-swiper.css"

export default defineComponent({
    props: {
        cardTitle: {
            type: String,
            required: false,
        },
        cardSubtitle: {
            type: String,
            required: false,
        },
    },
    components: {
        IonCard,
        IonCardHeader,
        IonCardSubtitle,
        IonCardTitle,
    },
})
</script>

<style scoped>
.full-width-card {
    width: 100%;
    height: 95%;
    background-color: var(--ion-color-light);
    border-radius: 20px;
}

.ios ion-card-title {
    font-size: 1.0rem;
}

ion-card-subtitle {
    --color: var(--ion-color-primary);
}
</style>
  