<template>
  <swiper :slidesPerView="1.2" :centeredSlides="true" :spaceBetween="5">

    <slot></slot>

  </swiper>
</template>

<script lang="ts">
import { defineComponent } from 'vue';
import { Swiper, SwiperSlide } from 'swiper/vue';


import 'swiper/css';
import '@ionic/vue/css/ionic-swiper.css';

export default defineComponent({
  components: {
    Swiper,
  },
});
</script>

<style scoped>
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