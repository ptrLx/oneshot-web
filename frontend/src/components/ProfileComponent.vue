<template>
  <ion-button router-link="/profile" fill="clear" class="avatar-button">
    <ion-avatar class="avatar-icon">
      <img alt="Silhouette of a person's head" src="https://ionicframework.com/docs/img/demos/avatar.svg" />
    </ion-avatar>
  </ion-button>
</template>

<script setup lang="ts">
import { IonButton } from '@ionic/vue';

</script>

<style scoped>
.avatar-icon {
  padding: 1%;
  transform: scale(0.8);
  border: none;

}

.avatar-button {
  padding: 0;
  margin: 0;
  border: none
}
</style>
