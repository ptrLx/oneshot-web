<template>
    <card class="image-card">
        <router-link :to="`/image/${id}`">
            <ion-img :src="imgsrc" alt="Image" class="gallery-image"></ion-img>
        </router-link>
        <div class="title-container">
            <p class="image-title">{{ imagetitle || 'Your Title' }}</p>
        </div>
        <div class="emoji-container">
            <p class="emoji">{{ emoji || '❓' }}</p>
        </div>
    </card>
</template>
  
<script lang="ts">
import { defineComponent } from 'vue';
import { IonImg } from '@ionic/vue';
import Card from '@/components/Card.vue';
import { RouterLink } from 'vue-router';


export default defineComponent({
    props: {
        id: {
            type: String,
            required: true,
        },
        imgsrc: {
            type: String,
            required: true,
        },
        imagetitle: {
            type: String,
            required: false,
        },
        emoji: {
            type: String,
            required: false,
        },
    },
    components: {
        Card,
        IonImg,
        RouterLink
    },
});
</script>
  
<style scoped>
.gallery-image {
    width: 100%;
    height: 100%;
    object-fit: cover;
    transition: transform 0.3s ease;
    position: relative;
}

.image-card {
    height: 200px;
    margin: 0;
    overflow: hidden;
    position: relative;
}

/* Add a zoom effect on hover, only works on mouse over */
.image-card:hover .gallery-image {
    transform: scale(1.1);
    /* Increase the scale on hover (adjust the value as needed) */
}

.title-container {
    position: absolute;
    bottom: -5px;
    left: 10px;
    color: var(--ion-color-primary-contrast);
    font-size: 1.0rem;
    text-shadow: 2px 2px 2px rgba(0, 0, 0, 0.5);
    text-align: left;
}

.emoji-container {
    position: absolute;
    bottom: -16px;
    right: 10px;
    font-size: 1.5rem;
}
</style>
  