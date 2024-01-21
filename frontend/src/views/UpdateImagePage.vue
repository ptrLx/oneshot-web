<template>
    <base-layout page-title="Edit Image" :hide-back-button="false">
        <template #custom-buttons>
            <ion-button id="presentDelete" @click="showDeleteAlert">
                <ion-icon :icon="trashOutline"></ion-icon>
            </ion-button>
        </template>
        <ion-grid class="ion-text-center">
            <ion-row>
                <ion-title>
                    <div class="ios-container">
                        {{ imgDate }}
                    </div>
                </ion-title>
            </ion-row>
            <ion-row>
                <ion-col size="12">
                    <ion-img :src="uploadedImage"></ion-img>
                </ion-col>
            </ion-row>
            <ion-row>
                <ion-col size="12">
                    <happiness-selector
                        class="selector"
                        :default-happiness="selectedHappiness?.toString()"
                        @update:selectedHappiness="handleNewHappiness"
                    >
                    </happiness-selector>
                </ion-col>
            </ion-row>
            <ion-row>
                <ion-col size="12">
                    <ion-textarea
                        type="text"
                        fill="outline"
                        shape="round"
                        placeholder="Enter your new description here"
                        :maxlength="600"
                        :spellcheck="true"
                        :counter="true"
                        v-model="description"
                    >
                    </ion-textarea>
                </ion-col>
            </ion-row>
            <ion-row>
                <ion-col size="12">
                    <ion-button shape="round" @click="handleUpdate">Update</ion-button>
                </ion-col>
            </ion-row>
        </ion-grid>
    </base-layout>
</template>

<script lang="ts">
    import {
        IonButton,
        IonGrid,
        IonRow,
        IonCol,
        IonIcon,
        IonTextarea,
        useIonRouter,
        IonAlert,
        IonTitle,
        IonImg,
        onIonViewDidLeave,
        alertController,
    } from "@ionic/vue"
    import { trashOutline } from "ionicons/icons"
    import { defineComponent, ref } from "vue"
    import { OneShotService } from "@/_generated/api-client"
    import { useRoute, useRouter } from "vue-router"
    import HappinessSelector from "@/components/HappinessSelector.vue"
    import { HappinessDTO } from "@/_generated/api-client"
    import { blobStore, metadataStore } from "@/composables/store"
    import { useThemeService } from "@/composables/themeService"

    export default defineComponent({
        components: {
            IonButton,
            IonGrid,
            IonRow,
            IonCol,
            IonIcon,
            IonTextarea,
            IonTitle,
            IonImg,
            HappinessSelector,
        },
        setup() {
            useThemeService(true) // Set theme to media preference

            const route = useRoute()
            const router = useRouter()

            const imgDate = ref<string>(route.params.id as string)
            const imgSrc = ref<string>(URL.createObjectURL(blobStore.getBlob()))
            const metadata = metadataStore.getMetadata()
            const uploadedImage = ref<string>(imgSrc.value)
            const description = ref<string>(metadata?.text || "")
            const selectedHappiness = ref<HappinessDTO | null>(metadata?.happiness || null)

            const handleNewHappiness = (newHappiness: HappinessDTO) => {
                selectedHappiness.value = newHappiness
            }

            const handleUpdate = () => {
                OneShotService.updateMetadataMetadataUpdatePost(
                    imgDate.value,
                    metadata?.time || 0,
                    selectedHappiness.value,
                    description.value,
                ).then(() => {
                    router.back()
                })
            }

            const handleDelete = () => {
                OneShotService.deleteImageImageDeletePost(imgDate.value).then(
                    () => {
                        // go back to gallery / go back twice
                        router.go(-2)
                    },
                    () => {
                        console.log("An error occurred while deleting the image")
                    },
                )
            }

            const showDeleteAlert = async () => {
                const alert = await alertController.create({
                    header: "Are you sure you want to delete this OneShot?",
                    buttons: [
                        {
                            text: "Delete",
                            handler: handleDelete,
                        },
                        {
                            text: "Cancel",
                            role: "cancel",
                        },
                    ],
                    cssClass: "delete-alert",
                })
                await alert.present()
            }

            onIonViewDidLeave(() => {
                imgDate.value = ""
                imgSrc.value = ""
                uploadedImage.value = ""
                description.value = ""
                selectedHappiness.value = null
            })

            return {
                uploadedImage,
                imgDate,
                description,
                handleNewHappiness,
                handleUpdate,
                selectedHappiness,
                trashOutline,
                showDeleteAlert,
            }
        },
    })
</script>

<style scoped>
    .ios .ios-container {
        margin-top: 20px;
        height: 10%;
        width: 100%;
    }

    .ios ion-title {
        position: inherit;
    }

    ion-textarea {
        height: 250px;
        width: 80%;
        --placeholder-opacity: 0.5;
        text-align: left;
        margin-top: 20px;
        margin-bottom: 20px;
        margin-left: 10%;
        margin-right: 10%;
    }

    ion-button {
        width: 80%;
        height: 50px;
        margin-top: 20px;
    }

    .ios ion-button {
        margin-top: 0px;
        height: inherit;
    }

    ion-img {
        width: 60%;
        height: 250px;
        margin-top: 10px;
        margin-bottom: 10px;
        margin-left: 20%;
        margin-right: 20%;
    }

    ion-img::part(image) {
        border-radius: 50px;
        border: 1px dashed var(--ion-color-primary);
        overflow: hidden;
        object-fit: cover;
    }

    .selector {
        width: 80%;
        height: 40px;
        margin-top: 5px;
        margin-bottom: 5px;
        margin-left: 10%;
        margin-right: 10%;
    }

    ion-alert.delete-alert {
        --backdrop-opacity: 0.7;
    }
</style>
