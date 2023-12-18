<template>
  <router-link to="/profile">
    <ion-avatar class="avatar-icon">
      <ion-img v-if="blobUrl" :src="blobUrl" />
      <div class="avatar-overlay"></div>
    </ion-avatar>
  </router-link>
</template>

<script lang="ts">
import { IonAvatar, IonImg, onIonViewDidEnter } from '@ionic/vue';
import { defineComponent, ref, onMounted, watch } from 'vue';
import axios, { AxiosRequestConfig } from 'axios';
import { OpenAPI } from '@/_generated/api-client'
import { useImageService } from '@/composables/imageService';
import { store } from '@/composables/store';

export default defineComponent({
  components: {
    IonAvatar,
    IonImg
  },
  setup() {

    const blobUrl = ref<string>("");
    const { loadImg } = useImageService();

    const updateProfilePic = () => {
      const queryString = OpenAPI.BASE + "/user/profileimg";
      loadImg(queryString).then(blob => {
        blobUrl.value = URL.createObjectURL(blob);
      })
    }

    onMounted(async () => {
      updateProfilePic();
    });

    watch(() => store.profilePicUpdate, () => {
      updateProfilePic();
    });

    return { blobUrl };
  }
});

</script>

<style scoped>
.avatar-icon {
  padding: 1%;
  transform: scale(0.8);
  border: 3px solid var(--ion-color-primary);
  position: relative;
  cursor: pointer;
}

.avatar-overlay {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  border-radius: 50%;
  background: rgba(0, 0, 0, 0.3);
  display: none;
  justify-content: center;
  align-items: center;
  transition: background 0.2s, display 0.2s;
}

.avatar-icon:hover .avatar-overlay {
  display: flex;
}
</style>

