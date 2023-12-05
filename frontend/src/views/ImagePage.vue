<template>
    <base-layout :page-title="imageTitle" :hide-back-button=false>
        <template #custom-buttons>
            <ion-button>
                <ion-icon :icon="createOutline"></ion-icon>
            </ion-button>
        </template>
        <ion-img alt="Img" :src="imgSrc" class="fullscreen-image"></ion-img>
        <div :class="{ 'no-overlay': !isExpanded, 'overlay': isExpanded }"></div>
        <div :class="{ 'description': !isExpanded, 'description-expanded': isExpanded }" @click="expandDescription">
            {{ descriptionText }}
        </div>
    </base-layout>
</template>

<script lang="ts">
import { computed, defineComponent, ref } from 'vue';
import { IonCard, IonImg, IonCardSubtitle, IonCardTitle, IonButton, IonIcon } from '@ionic/vue';
import { useRoute } from 'vue-router'
import { useImageService } from '@/composables/imageService';
import { OneShotService } from '@/_generated/api-client';
import { createOutline } from 'ionicons/icons';

export default defineComponent({
    components: {
        IonCard,
        IonImg,
        IonCardSubtitle,
        IonCardTitle,
        IonButton,
        IonIcon,
    },
    setup() {
        const route = useRoute()
        const { downloadGalleryImg } = useImageService()

        const happinessMap = {
            VERY_HAPPY: '😁',
            HAPPY: '🙂',
            NEUTRAL: '😐',
            SAD: '😞',
            VERY_SAD: '😭',
            NOT_SPECIFIED: '❓'
        };
        const id = route.params.id as string // the image date in format YYYY-MM-DD
        const imgSrc = ref<string>('')
        const imageDate = ref<string>(id)
        const imageHappiness = ref<string>(happinessMap.NOT_SPECIFIED)
        const imageTitle = computed(() => `${imageDate.value} | ${imageHappiness.value}`);
        const descriptionText = ref<string>('')


        const isExpanded = ref<boolean>(false)
        const expandDescription = () => {
            isExpanded.value = !isExpanded.value
        }

        downloadGalleryImg(id).then((blob) => {
            imgSrc.value = URL.createObjectURL(blob)
        })

        OneShotService.getMetadataMetadataGet(id).then((response) => {
            if (response.happiness) {
                imageHappiness.value = happinessMap[response.happiness]
            }
            if (response.text) {
                descriptionText.value = response.text
            }
        })


        return {
            imgSrc,
            imageTitle,
            descriptionText,
            isExpanded,
            expandDescription,
            createOutline
        }
    }
});
</script>

<style scoped>
.fullscreen-image {
    width: 100%;
    height: auto;
}

.description {
    position: absolute;
    bottom: 15px;
    left: 3%;
    width: 94%;
    display: -webkit-box;
    -webkit-line-clamp: 2;
    -webkit-box-orient: vertical;
    overflow: hidden;
    text-overflow: 'ellipsis';
    color: white;
    transition: max-height 0.2s ease-out;
}

.description-expanded {
    position: absolute;
    bottom: 15px;
    left: 3%;
    width: 94%;
    max-height: 85%;
    overflow: auto;
    color: white;
    transition: max-height 0.2s ease-out;
}

.no-overlay {
    /* fill whole screen */
    position: absolute;
    bottom: 0;
    left: 0;
    width: 100%;
    height: 20%;
    background: linear-gradient(to top, rgba(0, 0, 0, 0.8) 10%, transparent);
}

.overlay {
    /* fill whole screen */
    position: absolute;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;

    /* semi-transparent background */
    background-color: rgba(0, 0, 0, 0.5);
    transition: background-color 0.2s ease-out;
}
</style>