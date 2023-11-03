<template>
    <base-layout page-title="Profile" default-back-link="/home">

        <div class="flex-container">
            <ion-avatar class="profile-avatar">
                <ion-img v-if="blobUrl" :src="blobUrl" />
                <ion-button id="changeProfilePic" class="change-profile-pic-button" shape="round">
                    <ion-icon slot="icon-only" :icon="cameraOutline"></ion-icon>
                </ion-button>
            </ion-avatar>
        </div>
        <ion-title class="ion-text-center">
            <h1>{{ username }}</h1>
        </ion-title>

        <!-- Buttons Section -->
        <ion-grid class="ion-text-center">
            <ion-row>
                <ion-col size="12">
                    <ion-button shape="round">Toggle theme</ion-button>
                </ion-col>
            </ion-row>
            <ion-row>
                <ion-col size="12">
                    <ion-button shape="round">Export database</ion-button>
                </ion-col>
            </ion-row>
            <ion-row>
                <ion-col size="12">
                    <ion-button shape="round">Import database</ion-button>
                </ion-col>
            </ion-row>
            <ion-row>
                <ion-col size="12">
                    <ion-button shape="round" @click="$router.push('/change-password')">Change password</ion-button>
                </ion-col>
            </ion-row>
            <ion-row>
                <ion-col size="12">
                    <ion-button @click="handleLogout" shape="round">Log out</ion-button>
                </ion-col>
            </ion-row>
            <ion-row>
                <ion-col size="12">
                    <ion-button shape="round">Feedback</ion-button>
                </ion-col>
            </ion-row>
            <ion-row>
                <ion-col size="12">
                    <ion-button shape="round">Open Source Licence</ion-button>
                </ion-col>
            </ion-row>
        </ion-grid>

        <ion-action-sheet trigger="changeProfilePic" header="Change profile picture"
            :buttons="actionSheetButtons"></ion-action-sheet>
    </base-layout>
</template>
  
<script lang="ts">
import { IonAvatar, IonButton, IonGrid, IonRow, IonCol, IonIcon, IonTitle, useIonRouter, IonImg, IonActionSheet } from '@ionic/vue';
import { ImageService, LoginService, UserService, Token, OpenAPI, ApiError } from '@/_generated/api-client';
import { cameraOutline, chatboxEllipsesOutline, constructOutline, image } from 'ionicons/icons';
import { computed, defineComponent, onMounted, ref } from 'vue';
import { useCookies } from 'vue3-cookies'
import ProfileComponent from '@/components/ProfileComponent.vue';
import axios, { AxiosRequestConfig } from 'axios';
import { useCameraService, UserPhoto } from '@/composables/cameraService';


export default defineComponent({
    components: {
        IonAvatar,
        IonButton,
        IonGrid,
        IonRow,
        IonCol,
        IonIcon,
        IonTitle,
        IonImg,
        IonActionSheet
    },
    setup() {

        const router = useIonRouter();
        const { cookies } = useCookies();
        OpenAPI.TOKEN = cookies.get("token");
        const username = ref<string>("");
        const profilePic = ref<string | null>(null);
        const blobUrl = ref<string>("");
        const { takePhoto, pickPhoto, photos } = useCameraService();

        const actionSheetButtons = [
            {
                text: 'Camera',
                role: 'destructive',
                handler: () => {
                    takePhoto().then(() => {
                        blobUrl.value = photos.value[0]?.webviewPath || '';
                        // TODO: upload profile pic to server
                    });
                }
            },
            {
                text: 'Gallery',
                role: 'destructive',
                handler: () => {
                    pickPhoto().then(() => {
                        blobUrl.value = photos.value[0]?.webviewPath || '';
                        // TODO: upload profile pic to server
                    });
                    console.log('Gallery clicked');
                }
            },
            {
                text: 'Cancel',
                role: 'cancel',
                handler: () => {
                    console.log('Cancel clicked');
                }
            }
        ]


        UserService.getUserMeUserMeGet().then((response) => {
            username.value = response.username;
        }).catch((error: ApiError) => {
            console.log(error);
        });


        const handleLogout = () => {
            cookies.remove("token");
            router.push('/login');
        }

        const loadImg = async (src: string) => {
            const config: AxiosRequestConfig<any> = { url: src, method: "get", responseType: "blob" }
            const response = await axios.request(config)
            return response.data // the blob    
        }


        onMounted(async () => {
            const queryString = OpenAPI.BASE + "/user/profileimg";
            loadImg(queryString).then(blob => {

                blobUrl.value = URL.createObjectURL(blob);
            })
        });

        return {
            cameraOutline,
            router,
            cookies,
            profilePic,
            blobUrl,
            handleLogout,
            username,
            actionSheetButtons,
        };
    },
});

</script>

<style scoped>
.flex-container {
    display: flex;
    justify-content: center;
    align-items: center;
}

.profile-avatar {
    margin: 60px;
    scale: 2.0;
}

.change-profile-pic-button {
    position: absolute;
    top: 18px;
    left: 18px;
    scale: 0.3;
    height: 70px;
    width: 70px;
}

ion-button {
    width: 80%;
    height: 50px;
}

ion-icon {
    scale: 2.0;
}
</style>

  