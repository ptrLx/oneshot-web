<template>
    <base-layout page-title="Edit Image" :hide-back-button=false>


        <ion-grid class="ion-text-center">
            <ion-row>
                <ion-title>{{ imgDate }}</ion-title>
            </ion-row>
            <ion-row>
                <ion-col size="12">
                    <ion-img :src="uploadedImage"></ion-img>
                </ion-col>
            </ion-row>
            <ion-row>
                <ion-col size="12">
                    <happiness-selector class="selector" @update:selectedHappiness="handleNewHappiness">
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
                    <ion-button shape="round" @click="handleUpload">Upload</ion-button>
                </ion-col>
            </ion-row>
        </ion-grid>
    </base-layout>
</template>
  
<script lang="ts">
import { IonAvatar, IonButton, IonGrid, IonRow, IonCol, IonIcon, IonTextarea, useIonRouter, IonToast, toastController, IonTitle, IonImg } from '@ionic/vue';

import { defineComponent, ref } from 'vue';
import { OneShotService, UserService, OpenAPI, ApiError } from '@/_generated/api-client';
import { routerKey, useRoute } from 'vue-router';
import { useCameraService } from '@/composables/cameraService';
import { useImageService } from '@/composables/imageService';
import HappinessSelector from '@/components/HappinessSelector.vue';
import { HappinessDTO } from '@/_generated/api-client';
import { OneShotUpdate } from '@/types/OneShotUpdate';

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
        HappinessSelector
    },
    setup() {

        const route = useRoute();
        const router = useIonRouter();
        const { takePhoto, pickPhoto, photos } = useCameraService();
        const { uploadGalleryImg } = useImageService();

        const imgDate = ref<string>(route.params.id as string);
        const uploadedImage = ref<string>("");
        const description = ref<string>("");

        let selectedHappiness = HappinessDTO.NEUTRAL // Default value

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
            selectedHappiness = newHappiness;
        }

        const handleUpload = () => {

            const oneShotUpdate: OneShotUpdate = {
                date: imgDate.value,
                time: Date.now() / 1000, //TODO: read from image exif data instead
                happiness: selectedHappiness,
                text: description.value,
            };

            uploadGalleryImg(uploadedImage.value, oneShotUpdate).then((respose) => {
                router.push('/home');
            }).catch((error) => {
                console.log(error);
                //TODO: show error message to user
            });
        }

        return {
            uploadedImage,
            imgDate,
            description,
            handleNewHappiness,
            handleUpload
        };
    },
});

</script>

<style scoped>
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
</style>

  