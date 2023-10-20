<template>
  <swiper :slidesPerView="1.2" :centeredSlides="true" :spaceBetween="5">

    <swiper-slide>
      <ion-card class="full-width-card">
        <ion-card-header>
          <ion-card-title>Card Title</ion-card-title>
          <ion-card-subtitle>Card Subtitle</ion-card-subtitle>
        </ion-card-header>
      </ion-card>

    </swiper-slide>

    <swiper-slide>
      <ion-card class="full-width-card">
        <ion-card-header>
          <ion-card-title>Card Title</ion-card-title>
          <ion-card-subtitle>Card Subtitle</ion-card-subtitle>
        </ion-card-header>
      </ion-card>
    </swiper-slide>

  </swiper>
</template>

<script lang="ts">
import { defineComponent } from 'vue';
import { Swiper, SwiperSlide } from 'swiper/vue';
import { IonCard, IonCardHeader, IonCardSubtitle, IonCardTitle } from '@ionic/vue';

import 'swiper/css';
import '@ionic/vue/css/ionic-swiper.css';

export default defineComponent({
  components: {
    Swiper,
    SwiperSlide,
    IonCard,
    IonCardHeader,
    IonCardSubtitle,
    IonCardTitle,
  },
});
</script>

<style scoped>
.full-width-card {
  width: 100%;
  height: 95%;
  background-color: var(--ion-color-light-shade);
  border-radius: 20px;
}

.swiper-slide-active {
  transform: scale(1.05, 1.05);
}

.swiper-slide {
  transition: 400ms all ease-in-out;
}

.swiper {
  padding-top: 2%;
}
</style>