<template>
    <base-layout page-title="Gallery" :hide-back-button="false">
        <ion-grid>
            <ion-row v-for="(row, rowIndex) in galleryRows" :key="rowIndex">
                <ion-col v-for="(image, colIndex) in row" :key="colIndex" size="6">
                    <gallery-image :id="(image.date).toString()" :imagetitle="(image.date).toString()" :imgsrc="image.url"
                        :emoji="image.happiness">
                    </gallery-image>
                </ion-col>
            </ion-row>
            <ion-infinite-scroll @ionInfinite="loadMoreImages">
                <ion-infinite-scroll-content loadingText="Please wait..." loadingSpinner="bubbles">
                </ion-infinite-scroll-content>
            </ion-infinite-scroll>
        </ion-grid>
    </base-layout>
</template>
  
<script lang="ts">
import {
    IonGrid,
    IonRow,
    IonCol,
    IonInfiniteScroll,
    IonInfiniteScrollContent
} from '@ionic/vue';

import { defineComponent, ref, onMounted, nextTick } from 'vue';
import { OneShotService } from '@/_generated/api-client';
import { useImageService } from '@/composables/imageService';
import GalleryImage from '@/components/GalleryImage.vue';
import { images } from 'ionicons/icons';

export default defineComponent({
    components: {
        IonGrid,
        IonRow,
        IonCol,
        IonInfiniteScroll,
        IonInfiniteScrollContent,
        GalleryImage
    },
    setup() {
        const { downloadGalleryImg } = useImageService();
        const galleryRows = ref<{ date: string; url: string; happiness: string }[][]>([]);
        let imgPage = 0;
        let imgPageSize = 10; // initial load / batch size when loading more images

        // mapping of happiness values to emojis
        // VERY_HAPPY, HAPPY, NEUTRAL, SAD, VERY_SAD
        const happinessMap = {
            VERY_HAPPY: '😁',
            HAPPY: '🙂',
            NEUTRAL: '😐',
            SAD: '😞',
            VERY_SAD: '😭',
            NOT_SPECIFIED: '❓'
        };



        const loadGalleryImages = async () => {
            const images = await OneShotService.paginateGalleryImageGalleryGet(imgPage, imgPageSize);
            const galleryImages = await Promise.all(
                images.map(async (image) => {
                    const blob = await downloadGalleryImg(image.date);
                    const url = URL.createObjectURL(blob);
                    let hapinessEmoji = happinessMap["NOT_SPECIFIED"];
                    if (image.happiness) {
                        hapinessEmoji = happinessMap[image.happiness];
                    }

                    return {
                        date: image.date,
                        url: url,
                        happiness: hapinessEmoji
                    };
                })
            );
            galleryRows.value.push(galleryImages);
        };

        const loadMoreImages = async (event?: CustomEvent<void>) => {
            console.log('Loading more images ... ');
            await loadGalleryImages();
            imgPage++;
            if (event) {
                (event?.target as HTMLIonInfiniteScrollElement).complete();
            }
        };

        /**
         * Make sure infinite scroll is triggered at least once,
         * even if content does not fill the viewport. (example: imgPageSize = 2)
         * Without this, content would not be loaded dynamically if the initial
         * set does not fill the viewport.
         */
        const checkFillViewport = async () => {
            await nextTick();
            const ionGrid = document.querySelector('ion-grid');
            const ionContent = document.querySelector('ion-content');
            if (ionGrid && ionContent && ionGrid.clientHeight < ionContent.clientHeight + 100) {
                await loadMoreImages();
                setTimeout(checkFillViewport, 0);
            }
        };

        onMounted(() => {
            // Initial load 
            setTimeout(checkFillViewport, 0);
        });

        return {
            galleryRows,
            loadMoreImages
        };
    }
});
</script>
  
<style scoped></style>
  