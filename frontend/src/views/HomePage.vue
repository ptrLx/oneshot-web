<template>
  <ion-page>
    <ion-header :translucent="true">
      <ion-toolbar>
        <ion-title>
          <div>
            <span class="title-main">OneShot</span>
            <br>
            <span class="title-sub">Remember the happy days!</span>
          </div>
        </ion-title>

        <profile-component slot="end"></profile-component>
      </ion-toolbar>
    </ion-header>

    <ion-content :fullscreen="true">
      <ion-refresher slot="fixed" @ionRefresh="handleRefresh($event)">
        <ion-refresher-content refreshing-spinner="crescent">
        </ion-refresher-content>
      </ion-refresher>
      <row-component row-height="360px" sectionHeaderTitle="Gallery" :button-func="() => router.push('/gallery')">
        <swiper-slide v-if="hasImage('random_happy')">
          <router-link :to="`/image/${flashbackImgs['random_happy']?.meta.date}`">
            <div class="flashback-container">
              <ion-img :src="flashbackImgs['random_happy']?.url" alt="Image of a random happy day." class="rounded-image"
                fetchpriority="high">
              </ion-img>
              <div class="flashback-title"> Random Happy Day</div>
            </div>
          </router-link>
        </swiper-slide>
        <swiper-slide v-else>
          <card card-title="Your Flashbacks" card-subtitle="Nothing here yet - Upload images to see them appear here!">

            <ion-img src="/icons/512.png" alt="OneShot logo" class="rounded-image"
              style="width: 200px; position: relative; top: 0px; margin-top: 0px; margin-bottom: 0px; margin-left: auto; margin-right: auto;">
            </ion-img>

          </card>
        </swiper-slide>
        <swiper-slide v-if="hasImage('last_very_happy_day')">
          <router-link :to="`/image/${flashbackImgs['last_very_happy_day']?.meta.date}`">
            <div class="flashback-container">
              <ion-img :src="flashbackImgs['last_very_happy_day']?.url" alt="Image of the last very happy day."
                class="rounded-image">
              </ion-img>
              <div class="flashback-title"> Last Very Happy Day</div>
            </div>
          </router-link>
        </swiper-slide>
        <swiper-slide v-if="hasImage('same_day_last_month')">
          <router-link :to="`/image/${flashbackImgs['same_day_last_month']?.meta.date}`">
            <div class="flashback-container">
              <ion-img :src="flashbackImgs['same_day_last_month']?.url" alt="Image of the same day last month."
                class="rounded-image">
              </ion-img>
              <div class="flashback-title"> Same Day Last Month</div>
            </div>
          </router-link>
        </swiper-slide>
        <swiper-slide v-for="(image, index) in getSameDateLastYearsImages(flashbackImgs)" :key="index">
          <router-link :to="`/image/${image.meta.date}`">
            <div class="flashback-container">
              <ion-img :src="image.url" :alt="`Image of the day ${index} years ago.`" class="rounded-image">
              </ion-img>
              <div class="flashback-title"> {{ getCardTitle(image.meta.date) }}</div>
            </div>
          </router-link>
        </swiper-slide>
      </row-component>
      <row-component row-height="150px" :enableSectionHeader=false>
        <swiper-slide>
          <capture-today-slide></capture-today-slide>
        </swiper-slide>
      </row-component>
      <row-component row-height="400px" sectionHeaderTitle="Calendar" :enable-button=false>
        <swiper-slide>
          <card>
            <calendar-component></calendar-component>
          </card>
        </swiper-slide>
      </row-component>
      <row-component row-height="360px" sectionHeaderTitle="Statistics" :enable-button=false>
        <swiper-slide>
          <card>
            <donut-chart center-text="Happiness Week" :data="stats?.happiness_current_week"></donut-chart>
          </card>
        </swiper-slide>
        <swiper-slide>
          <card>
            <donut-chart center-text="Happiness Month" :data="stats?.happiness_current_month"></donut-chart>
          </card>
        </swiper-slide>
        <swiper-slide>
          <card>
            <donut-chart center-text="Happiness Year" :data="stats?.happiness_current_year"></donut-chart>
          </card>
        </swiper-slide>
      </row-component>

    </ion-content>
  </ion-page>
</template>

<script setup lang="ts">
import { IonContent, IonHeader, IonPage, IonTitle, IonToolbar, IonImg, IonRefresher, IonRefresherContent } from '@ionic/vue';
import { SwiperSlide } from 'swiper/vue';
import RowComponent from '@/components/RowComponent.vue';
import ProfileComponent from '@/components/ProfileComponent.vue';
import Card from '@/components/Card.vue';
import CaptureTodaySlide from '@/components/CaptureTodaySlide.vue';
import DonutChart from '@/components/DonutChart.vue';
import CalendarComponent from '@/components/CalendarComponent.vue';
import { useRouter } from 'vue-router';
import { StatisticsService, StatisticDTO } from '@/_generated/api-client';
import { onBeforeMount, onMounted, ref } from 'vue';
import { useFlashbackService, FlashbackUrlAndMeta } from '@/composables/flashbackService';
import { useThemeService } from '@/composables/themeService';

useThemeService(true) // Set theme to media preference

const router = useRouter();
const { getFlashbacks } = useFlashbackService();

const flashbackImgs = ref<{ [key: string]: FlashbackUrlAndMeta }>({});

const stats = ref<StatisticDTO | null>(null);


onBeforeMount(() => {
  updateActions();
});


const handleRefresh = (event: CustomEvent) => {
  updateActions(event);
}

const getSameDateLastYearsImages = (flashbackImgs: { [key: string]: FlashbackUrlAndMeta }) => {
  return Object.keys(flashbackImgs)
    .filter(key => key.startsWith('same_date_last_years_'))
    .map(key => flashbackImgs[key]);
}

const getCardTitle = (flashbackDate: string) => {
  const currentDate = new Date();
  const flashbackYear = new Date(flashbackDate).getFullYear();
  const currentYear = currentDate.getFullYear();
  const differenceInYears = currentYear - flashbackYear;

  const toWords = (number: number) => {
    const words = [
      'One', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Eleven', 'Twelve'
    ];
    return words[number] || number.toString();
  }

  if (differenceInYears === 0) {
    return 'One Year Ago';
  }

  return `${toWords(differenceInYears)} Years Ago`;
}

const hasImage = (key: string) => {
  return flashbackImgs.value[key]?.url;
};

const updateActions = (event: CustomEvent = { detail: { complete: () => { } } } as CustomEvent) => {
  getFlashbacks().then((flashbacks) => {
    flashbackImgs.value = flashbacks;
    event.detail.complete();
  }).catch(() => {
    console.log("Could not retrieve flashbacks");
    event.detail.complete();
  });

  StatisticsService.getStatisticsStatsGet().then((response) => {
    stats.value = response;
  }).catch(() => {
    console.log("Could not retrieve stats");
  });
}

</script>

<style scoped>
.flashback-container {
  position: relative;
  display: flex;
  justify-content: center;
  align-items: center;
  flex-direction: column;
}

.flashback-title {
  position: absolute;
  bottom: 50px;
  z-index: 1;
  background-color: rgba(0, 0, 0, 0.5);
  color: white;
  padding: 8px;
  border-radius: 20px;
}

.rounded-image {

  max-height: 350px;
  max-width: 100%;
  border-radius: 20px;
  margin: 35px;
  overflow: hidden;
}

ion-toolbar {
  line-height: 0.9;
}

.title-main {
  font-size: 18px;
}

.title-sub {
  font-size: 12px;
  color: var(--ion-color-primary-tint);
}

#container {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  height: 100vh;
}

#container strong {
  font-size: 20px;
  line-height: 26px;
}

#container p {
  font-size: 16px;
  line-height: 22px;

  color: #8c8c8c;

  margin: 0;
}

#container a {
  text-decoration: none;
}
</style>
                      