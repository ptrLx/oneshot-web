<template>
    <base-layout :page-title="imageTitle" :hide-back-button=false>
        <template #custom-buttons>
            <ion-button @click="handleEditClick">
                <ion-icon :icon="createOutline"></ion-icon>
            </ion-button>
        </template>
        <ion-img alt="Img" :src="imgSrc" class="fullscreen-image"></ion-img>
        <div :class="{ 'no-overlay': !isExpanded, 'overlay': isExpanded }"></div>
        <div ref="descriptionRef" :class="{
            'description': !isExpanded,
            'description-expanded': isExpanded,
        }" @click="expandDescription">
            {{ descriptionText }}
        </div>
    </base-layout>
</template>

<script lang="ts">
import { computed, defineComponent, nextTick, ref, watch } from "vue"
import { IonImg, IonButton, IonIcon } from "@ionic/vue"
import { useRoute } from "vue-router"
import { useImageService } from "@/composables/imageService"
import { OneShotService } from "@/_generated/api-client"
import { createOutline } from "ionicons/icons"
import router from "@/router"
import { blobStore, metadataStore } from "@/composables/store"
import { useThemeService } from "@/composables/themeService"

export default defineComponent({
    components: {
        IonImg,
        IonButton,
        IonIcon,
    },
    setup() {
        useThemeService(true) // Set theme to media preference

        const route = useRoute()
        const { downloadGalleryImg } = useImageService()

        const happinessMap = {
            VERY_HAPPY: "😁",
            HAPPY: "🙂",
            NEUTRAL: "😐",
            SAD: "😞",
            VERY_SAD: "😭",
            NOT_SPECIFIED: "❓"
        }
        const id = route.params.id as string // the image date in format YYYY-MM-DD
        const imgSrc = ref<string>("")
        const imageDate = ref<string>(id)
        const imageHappiness = ref<string>(happinessMap.NOT_SPECIFIED)
        const imageTitle = computed(() => `${imageDate.value} | ${imageHappiness.value}`)
        const descriptionText = ref<string>("")
        const descriptionRef = ref<HTMLDivElement | null>(null)

        const isExpanded = ref<boolean>(false)
        const isOverflowing = computed(() => {
            if (descriptionRef.value) {
                return descriptionRef.value.scrollHeight > descriptionRef.value.clientHeight
            }
            return false
        })

        const updateDescriptionClass = () => {
            nextTick(() => {
                const method = isExpanded.value ? "remove" : "add"
                descriptionRef.value?.classList[method]("description-overflowing")
            })
        }

        const expandDescription = () => {
            if (isOverflowing.value) {
                isExpanded.value = !isExpanded.value
                updateDescriptionClass()
            }
        }

        // Initial update of css class when description is set
        watch(descriptionText, () => {
            nextTick(() => {
                // update css class of description
                if (isOverflowing.value) {
                    descriptionRef.value?.classList.add("description-overflowing")
                }
            })
        })


        downloadGalleryImg(id, false).then((blob) => {

            blobStore.setBlob(blob) // store image in local storage in case user wants to edit it
            imgSrc.value = URL.createObjectURL(blob)
        })

        OneShotService.getMetadataMetadataGet(id).then((response) => {
            metadataStore.setMetadata(response) // store metadata in local storage in case user wants to edit it
            if (response.happiness) {
                imageHappiness.value = happinessMap[response.happiness]
            }
            if (response.text) {
                descriptionText.value = response.text
            }
        })

        const handleEditClick = () => {

            router.push(`/image/${id}/edit`)
        }

        return {
            imgSrc,
            imageTitle,
            descriptionText,
            isExpanded,
            expandDescription,
            createOutline,
            isOverflowing,
            descriptionRef,
            id,
            handleEditClick,
        }
    }
})
</script>

<style scoped>
.fullscreen-image {
    width: 100%;
    height: 100%;
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
    text-overflow: 'clip';
    color: white;
    transition: max-height 0.2s ease-out;
}

.description-overflowing {
    position: absolute;
    bottom: 15px;
    left: 3%;
    width: 94%;
    display: -webkit-box;
    -webkit-line-clamp: 2;
    -webkit-box-orient: vertical;
    overflow: hidden;
    text-overflow: 'clip';
    color: white;
    transition: max-height 0.2s ease-out;
}


.description-overflowing::after {
    content: '... (Click to expand)';
    position: absolute;

    bottom: 0;
    right: 0;
    width: 100%;
    background: linear-gradient(to left, rgb(0, 0, 0) 5%, rgba(0, 0, 0, 0) 100%);
    color: var(--ion-color-primary);

    padding-left: 10px;
    text-align: right;
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