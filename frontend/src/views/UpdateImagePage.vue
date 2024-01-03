<template>
    <base-layout page-title="Edit Image" :hide-back-button=false>

        <template #custom-buttons>
            <ion-button id="presentDelete">
                <ion-icon :icon="trashOutline"></ion-icon>
            </ion-button>
            <ion-alert trigger="presentDelete" header="Are you sure you want to delete this OneShot?"
                :buttons="alertButtons" class="delete-alert">
            </ion-alert>
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
                    <happiness-selector class="selector" :default-happiness="selectedHappiness?.toString()"
                        @update:selectedHappiness="handleNewHappiness">
                    </happiness-selector>
                </ion-col>
            </ion-row>
            <ion-row>
                <ion-col size="12">
                    <ion-textarea type="text" fill="outline" shape="round" placeholder="Enter your new description here"
                        :maxlength=600 :spellcheck=true :counter=true v-model="description">
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
import { IonAvatar, IonButton, IonGrid, IonRow, IonCol, IonIcon, IonTextarea, useIonRouter, IonAlert, toastController, IonTitle, IonImg } from '@ionic/vue';
import { trashOutline } from 'ionicons/icons';
import { defineComponent, ref } from 'vue';
import { OneShotService, UserService, OpenAPI, ApiError } from '@/_generated/api-client';
import { routerKey, useRoute } from 'vue-router';
import { useCameraService } from '@/composables/cameraService';
import { useImageService } from '@/composables/imageService';
import HappinessSelector from '@/components/HappinessSelector.vue';
import { HappinessDTO } from '@/_generated/api-client';
import { OneShotRespDTO } from '@/_generated/api-client';
import { blobStore, metadataStore } from '@/composables/store';
import { useThemeService } from '@/composables/themeService';

export default defineComponent({
    components: {
        IonAvatar,
        IonButton,
        IonGrid,
        IonRow,
        IonCol,
        IonIcon,
        IonTextarea,
        IonTitle,
        IonImg,
        HappinessSelector,
        IonAlert,
    },
    setup() {
        useThemeService(true) // Set theme to media preference

        const route = useRoute();
        const router = useIonRouter();
        const { takePhoto, pickPhoto, photos } = useCameraService();

        const imgDate = ref<string>(route.params.id as string);
        const imgSrc = ref<string>(URL.createObjectURL(blobStore.getBlob()));
        const metadata = metadataStore.getMetadata();
        const uploadedImage = ref<string>(imgSrc.value);
        const description = ref<string>(metadata?.text || '');
        const selectedHappiness = ref<HappinessDTO | null>(metadata?.happiness || null);

        switch (route.query.action) {
            case 'capture':
                takePhoto().then(() => {
                    uploadedImage.value = photos.value[0]?.webviewPath || '';
                    imgDate.value = new Date().toISOString().slice(0, 10);
                })
                break;
            case 'pick':
                pickPhoto().then(() => {
                    uploadedImage.value = photos.value[0]?.webviewPath || '';
                    imgDate.value = new Date().toISOString().slice(0, 10);
                })
                break;
            default:
                console.log('Unknown action');
                break;
        }

        const handleNewHappiness = (newHappiness: HappinessDTO) => {
            selectedHappiness.value = newHappiness;
        }

        const handleUpdate = () => {

            OneShotService.updateMetadataMetadataUpdatePost(
                imgDate.value,
                metadata?.time || 0,
                selectedHappiness.value,
                description.value,
            ).then((response) => {
                router.push('/home');
            })
        }

        const handleDelete = () => {
            OneShotService.deleteImageImageDeletePost(imgDate.value).then((response) => {
                router.push('/home');
            }, (error: ApiError) => {
                console.log("An error occurred while deleting the image");
            })
        }

        const alertButtons = [
            {
                text: 'Delete',
                //cssClass: 'alertButtonDelete', // Styling not working here
                handler: handleDelete,
            },
            {
                text: 'Cancel',
                role: 'cancel',
            },
        ];


        return {
            uploadedImage,
            imgDate,
            description,
            handleNewHappiness,
            handleUpdate,
            selectedHappiness,
            trashOutline,
            alertButtons,
        };
    },
});

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

  