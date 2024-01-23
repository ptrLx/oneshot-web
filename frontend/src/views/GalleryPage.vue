<template>
    <base-layout page-title="Gallery" :hide-back-button="false">
        <ion-grid>
            <ion-row v-for="(row, rowIndex) in galleryRows" :key="rowIndex">
                <ion-col v-for="(image, colIndex) in row" :key="colIndex" size="6">
                    <gallery-image
                        :id="image.date.toString()"
                        :imagetitle="image.date.toString()"
                        :imgsrc="image.url"
                        :emoji="image.happiness"
                    >
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
        IonInfiniteScrollContent,
        onIonViewDidLeave,
        onIonViewDidEnter,
    } from "@ionic/vue"

    import { defineComponent, ref, onMounted } from "vue"
    import { OneShotService } from "@/_generated/api-client"
    import { useImageService } from "@/composables/imageService"
    import GalleryImage from "@/components/GalleryImage.vue"
    import { useThemeService } from "@/composables/themeService"

    export default defineComponent({
        components: {
            IonGrid,
            IonRow,
            IonCol,
            IonInfiniteScroll,
            IonInfiniteScrollContent,
            GalleryImage,
        },
        setup() {
            useThemeService(true) // Set theme to media preference

            const { downloadGalleryImg } = useImageService()
            const galleryRows = ref<{ date: string; url: string; happiness: string }[][]>([])
            let imgPage = 0

            // if this set is too small, dynamic loading will not work (ion-infinite event will not trigger)
            const imgPageSize = 10 // initial load / batch size when loading more images

            const happinessMap = {
                NOT_SPECIFIED: "😶",
                VERY_SAD: "😭",
                SAD: "😞",
                NEUTRAL: "😐",
                HAPPY: "🙂",
                VERY_HAPPY: "😁",
            }
            const loadGalleryImages = async () => {
                const images = await OneShotService.paginateGalleryImageGalleryGet(
                    imgPage,
                    imgPageSize,
                )
                const galleryImages = await Promise.all(
                    images.map(async (image) => {
                        const blob = await downloadGalleryImg(image.date)
                        const url = URL.createObjectURL(blob)
                        let hapinessEmoji = happinessMap["NOT_SPECIFIED"]
                        if (image.happiness) {
                            hapinessEmoji = happinessMap[image.happiness]
                        }

                        return {
                            date: image.date,
                            url: url,
                            happiness: hapinessEmoji,
                        }
                    }),
                )
                galleryRows.value.push(galleryImages)
            }

            const loadMoreImages = async (event?: CustomEvent<void>) => {
                console.log("Loading more images ... ")
                await loadGalleryImages()
                imgPage++
                if (event) {
                    ;(event.target as HTMLIonInfiniteScrollElement).complete()
                }
            }

            onIonViewDidLeave(() => {
                galleryRows.value = []
                imgPage = 0
            })

            onIonViewDidEnter(() => {
                loadMoreImages()
            })

            return {
                galleryRows,
                loadMoreImages,
            }
        },
    })
</script>

<style scoped></style>
