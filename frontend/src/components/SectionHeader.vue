<template>
    <ion-grid class="section-header">
        <ion-row class="row">
            <ion-col size="1"> </ion-col>
            <ion-col size="5">
                <ion-title class="title" slot="">{{ title }}</ion-title>
            </ion-col>
            <ion-col size="5" class="ion-text-end">
                <ion-button
                    v-if="enableButton"
                    class="button"
                    aria-label="See all"
                    @click="handleButtonClick"
                >
                    <ion-icon slot="icon-only" :icon="arrowForwardOutline"></ion-icon>
                </ion-button>
            </ion-col>
            <ion-col size="1"> </ion-col>
        </ion-row>
    </ion-grid>
</template>

<script lang="ts">
    import { IonButton, IonGrid, IonRow, IonCol, IonTitle, IonIcon } from "@ionic/vue"
    import { defineComponent } from "vue"
    import { arrowForwardOutline } from "ionicons/icons"

    export default defineComponent({
        components: {
            IonButton,
            IonGrid,
            IonRow,
            IonCol,
            IonTitle,
            IonIcon,
        },
        props: {
            title: {
                type: String,
                default: "Title",
            },
            buttonFunc: {
                type: Function,
                default: () => {},
            },
            enableButton: {
                type: Boolean,
                default: true,
            },
        },
        setup(props) {
            const handleButtonClick = () => {
                props.buttonFunc()
            }

            return {
                arrowForwardOutline,
                handleButtonClick,
            }
        },
    })
</script>

<style scoped>
    .section-header {
        margin-top: 10px;
        margin-bottom: 5px;
        padding: 0px;
        height: 30px;
    }

    .row {
        height: 20px;
    }

    .title {
        font-size: 1.2rem;
        padding-top: 10px;
        padding-bottom: 10px;
        padding-inline: 0px;
    }

    .ios .title {
        padding-inline: 0px;
    }

    .button {
        font-size: 0.5rem;
        --background: transparent;
        --color: var(--ion-color-primary);
        --box-shadow: none;
    }

    .button:hover {
        --background: transparent;
        --color: var(--ion-color-primary);
        --box-shadow: none;
        /* slightly scale up */
        transform: scale(1.4);
    }
</style>
