<template>
  <ion-page>
    <ion-header :translucent="true">
      <ion-toolbar>
        <ion-title>OneShot</ion-title>
        <ion-title size="small">Remember the happy days!</ion-title>

        <profile-component slot="end"></profile-component>
      </ion-toolbar>
    </ion-header>

    <ion-content :fullscreen="true">

      <row-component style="height: 70%;">
        <swiper-slide>
          <card card-title="card1" card-subtitle="card1sub">
          </card>
        </swiper-slide>
        <swiper-slide>
          <card card-title="card2" card-subtitle="card2sub">
          </card>
        </swiper-slide>
      </row-component>
      <row-component style="height: 20%;">
        <swiper-slide>
          <card card-title="card1" card-subtitle="card1sub">
          </card>
        </swiper-slide>
        <swiper-slide>
          <card card-title="card2" card-subtitle="card2sub">
          </card>
        </swiper-slide>
      </row-component>
      <row-component style="height: 50%;">
        <swiper-slide>
          <card card-title="card1" card-subtitle="card1sub">
          </card>
        </swiper-slide>
        <swiper-slide>
          <card card-title="card2" card-subtitle="card2sub">
          </card>
        </swiper-slide>
      </row-component>
      <row-component style="height: 70%;">
        <swiper-slide>
          <card card-title="card1" card-subtitle="card1sub">
          </card>
        </swiper-slide>
        <swiper-slide>
          <card card-title="card2" card-subtitle="card2sub">
          </card>
        </swiper-slide>
        <swiper-slide>
          <card card-title="card3" card-subtitle="card3sub">
          </card>
        </swiper-slide>
      </row-component>


    </ion-content>
  </ion-page>
</template>

<script setup lang="ts">
import { IonContent, IonHeader, IonPage, IonTitle, IonToolbar } from '@ionic/vue';
import { SwiperSlide } from 'swiper/vue';
import RowComponent from '@/components/RowComponent.vue';
import ProfileComponent from '@/components/ProfileComponent.vue';
import Card from '@/components/Card.vue';


</script>

<style scoped>
#container {
  text-align: center;

  position: absolute;
  left: 0;
  right: 0;
  top: 50%;
  transform: translateY(-50%);
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
