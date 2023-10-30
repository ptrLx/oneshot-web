<template>
  <section-header v-if="enableSectionHeader" :title="sectionHeaderTitle"></section-header>
  <swiper :slidesPerView="1.2" :centeredSlides="true" :spaceBetween="5" :style="{ height: rowHeight }">
    <slot></slot>

  </swiper>
</template>

<script lang="ts">
import { defineComponent } from 'vue';
import { Swiper, SwiperSlide } from 'swiper/vue';
import SectionHeader from '@/components/SectionHeader.vue';

import 'swiper/css';
import '@ionic/vue/css/ionic-swiper.css';

export default defineComponent({
  components: {
    Swiper,
    SectionHeader
  },
  props: {
    rowHeight: {
      type: String,
      default: '100%'
    },
    enableSectionHeader: {
      type: Boolean,
      default: true
    },
    sectionHeaderTitle: {
      type: String,
      default: 'Title'
    }
  }
});
</script>

<style scoped>
.swiper-slide-active {
  transform: scale(1.05, 1.05);
}

.swiper-slide {
  transition: 400ms all ease-in-out;
}
</style>