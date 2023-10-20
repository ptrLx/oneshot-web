<template>
  <router-link to="/profile">
    <ion-avatar class="avatar-icon">
      <img alt="Silhouette of a person's head" src="https://ionicframework.com/docs/img/demos/avatar.svg" />
    </ion-avatar>
  </router-link>
</template>

<script lang="ts">
import { IonAvatar } from '@ionic/vue';
import { defineComponent } from 'vue';

export default defineComponent({
  components: {
    IonAvatar
  },
});
</script>

<style scoped>
.avatar-icon {
  padding: 1%;
  transform: scale(0.8);
  border: none;
}
</style>
