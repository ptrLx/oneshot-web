<template>
    <base-layout page-title="Gallery" :hide-back-button=false>
        <ion-grid>
            <ion-grid>
                <ion-row v-for="(row, rowIndex) in galleryRows" :key="rowIndex">
                    <ion-col v-for="(image, colIndex) in row" :key="colIndex" size="6">
                        <gallery-image :imgsrc="image.url" :emoji="image.happiness">

                        </gallery-image>
                    </ion-col>
                </ion-row>
                <ion-infinite-scroll @ionInfinite="loadMoreImages">
                    <ion-infinite-scroll-content loadingText="Please wait..."
                        loadingSpinner="bubbles"></ion-infinite-scroll-content>
                </ion-infinite-scroll>
            </ion-grid>
        </ion-grid>
    </base-layout>
</template>
  
<script lang="ts">
import { IonAvatar, IonButton, IonGrid, IonRow, IonCol, IonIcon, IonTextarea, useIonRouter, IonInfiniteScrollContent, IonInfiniteScroll, IonTitle, IonImg } from '@ionic/vue';

import { defineComponent, ref } from 'vue';
import { ImageService, LoginService, UserService, Token, OpenAPI, ApiError } from '@/_generated/api-client';
import GalleryImage from '@/components/GalleryImage.vue';
import { image } from 'ionicons/icons';

export default defineComponent({
    components: {
        IonButton,
        IonGrid,
        IonRow,
        IonCol,
        IonIcon,
        IonTitle,
        IonImg,
        IonInfiniteScroll,
        IonInfiniteScrollContent,
        GalleryImage
    },
    setup() {
        const galleryRows = ref<{ url: string, happiness: string }[][]>([]);
        const url_base = ref<string>('https://placekitten.com/200/300?image=');

        let index = 0;

        // Simulated data
        const happinessOptions = ['😄', '😃', '😐', '😞', '😢'];
        const initialImages = Array.from({ length: 10 }, () => ({
            url: url_base.value + index++,
            happiness: happinessOptions[Math.floor(Math.random() * happinessOptions.length)],
        }));



        // Initialize gallery with the initial images
        galleryRows.value.push(initialImages);

        const loadMoreImages = async (event: CustomEvent<void>) => {
            console.log('Loading more images called..');
            // Simulated asynchronous data fetching
            const newImages = Array.from({ length: 2 }, () => ({
                url: url_base.value + index++,
                happiness: happinessOptions[Math.floor(Math.random() * happinessOptions.length)]
            }));
            if (newImages.length > 0) {
                // Add new images to the gallery
                galleryRows.value.push(newImages);
                (event.target as HTMLIonInfiniteScrollElement).complete(); // Inform infinite-scroll that loading is complete
            } else {
                (event.target as HTMLIonInfiniteScrollElement).disabled = true; // Disable infinite-scroll if no more images
            }
        };

        return {
            galleryRows,
            loadMoreImages,
        };
    },
});

</script>

<style scoped></style>

  