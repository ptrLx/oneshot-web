<template>
  <section-header v-if="enableSectionHeader" :title="sectionHeaderTitle" :enableButton="enableButton"
    :buttonFunc="handleButtonClick"></section-header>
  <swiper :slidesPerView="'auto'" :centeredSlides="true" :effect="'coverflow'" :modules="modules" :lazy="true"
    :style="{ height: rowHeight }">
    <slot></slot>
  </swiper>
</template>

<script lang="ts">
import { defineComponent } from 'vue';
import { Swiper } from 'swiper/vue';
import SectionHeader from '@/components/SectionHeader.vue';
import { EffectCoverflow, Pagination } from 'swiper/modules';
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
    },
    buttonFunc: {
      type: Function,
      default: () => { }
    },
    enableButton: {
      type: Boolean,
      default: true
    }
  },
  setup(props) {

    const handleButtonClick = () => {
      props.buttonFunc();
    }

    return {
      handleButtonClick,
      modules: [EffectCoverflow, Pagination]
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