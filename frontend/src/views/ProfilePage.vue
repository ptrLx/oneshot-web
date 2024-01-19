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
        <div class="ios-container">
            <ion-title class="ion-text-center">
                <h1>{{ username }}</h1>
            </ion-title>
        </div>


        <!-- Buttons Section -->
        <ion-grid class="ion-text-center">
            <ion-row>
                <ion-col size="12">
                    <ion-button shape="round" @click="toggleTheme">Toggle theme</ion-button>
                </ion-col>
            </ion-row>
            <ion-row>
                <ion-col size="12">
                    <ion-button shape="round" @click="$router.push('/change-password')">Change password</ion-button>
                </ion-col>
            </ion-row>
            <ion-row>
                <ion-col size="12">
                    <ion-button shape="round" @click="openFileDialog('file-upload')">Import database</ion-button>
                </ion-col>
                <input type="file" id="file-upload" style="display: none;" webkitdirectory @change="handleImportDatabase" />
            </ion-row>
            <ion-row>
                <ion-col size="12">
                    <ion-button @click="handleLogout" shape="round">Log out</ion-button>
                </ion-col>
            </ion-row>
            <ion-row>
            </ion-row>
            <ion-row>
                <ion-col size="12">
                    <ion-button id="open-modal" shape="round">Open Source Licence</ion-button>
                </ion-col>
            </ion-row>
        </ion-grid>

        <ion-modal trigger="open-modal" :initial-breakpoint="1" :breakpoints="[0, 1]">
            <base-layout pageTitle="Open Source Licence" hide-back-button="true" fullscreen="false">
                <div style="padding: 20px;">
                    <p>OneShot-Web is free software released under GPLv3 and comes with absolutely no warranty.</p>
                    <p>Thanks to following open source projects that where used as dependencies:</p>
                    <p>Python (PSF)</p>
                    <p>Fastapi (MIT)</p>
                    <p>Pydantic (MIT)</p>
                    <p>Uvicorn (BSD 3-Clause)</p>
                    <p>python-jose (MIT)</p>
                    <p>passlib (BSD)</p>
                    <p>python-multipart (Apache)</p>
                    <p>aiofiles (Apache)</p>
                    <p>InquirerPy (MIT)</p>
                    <p>Prisma Client Python (Apache)</p>
                    <p>Pillow (HPND)</p>
                    <p>Capacitor (MIT)</p>
                    <p>Ionic (MIT)</p>
                    <p>Vue (MIT)</p>
                    <p>openapi-typescript-codegen (MIT)</p>
                    <p>Axios (MIT)</p>
                    <p>Swiper (MIT)</p>
                    <p>Vite (MIT)</p>
                </div>

            </base-layout>
        </ion-modal>

        <ion-action-sheet trigger="changeProfilePic" header="Change profile picture"
            :buttons="actionSheetButtons"></ion-action-sheet>
    </base-layout>
</template>
  
<script lang="ts">
import { IonAvatar, IonButton, IonGrid, IonRow, IonCol, IonIcon, IonTitle, useIonRouter, IonImg, IonActionSheet, IonModal, toastController } from "@ionic/vue"
import { UserService, OpenAPI, ApiError } from "@/_generated/api-client"
import { cameraOutline } from "ionicons/icons"
import { defineComponent, onMounted, ref } from "vue"
import { useCookies } from "vue3-cookies"
import { useCameraService } from "@/composables/cameraService"
import { useImageService } from "@/composables/imageService"
import { store } from "@/composables/store"
import { useThemeService } from "@/composables/themeService"
import { useImportExportService } from "@/composables/importExportService"

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
        IonActionSheet,
        IonModal,
    },
    setup() {
        const router = useIonRouter()
        const { cookies } = useCookies()
        OpenAPI.TOKEN = cookies.get("token")
        const username = ref<string>("")
        const profilePic = ref<string | null>(null)
        const blobUrl = ref<string>("https://ionicframework.com/docs/img/demos/avatar.svg")
        const { takePhoto, pickPhoto, photos } = useCameraService()
        const { loadImg, uploadProfileImg } = useImageService()
        const { toggleTheme } = useThemeService(true)
        const { importDatabase, openFileDialog } = useImportExportService()

        const actionSheetButtons = [
            {
                text: "Camera",
                role: "destructive",
                handler: () => {
                    takePhoto().then(() => {
                        blobUrl.value = photos.value[0]?.webviewPath || ""
                        uploadProfileImg(blobUrl.value)
                        store.notifyProfilePicUpdate()
                    })
                }
            },
            {
                text: "Gallery",
                role: "destructive",
                handler: () => {
                    pickPhoto().then(() => {
                        blobUrl.value = photos.value[0]?.webviewPath || ""
                        uploadProfileImg(blobUrl.value).then(() => {
                            store.notifyProfilePicUpdate()
                        })
                    })
                }
            },
            {
                text: "Cancel",
                role: "cancel",
                handler: () => {
                    console.log("Cancel clicked")
                }
            }
        ]

        const handleImportDatabase = (event: Event) => {
            importDatabase(event)
                .then(() => {
                    return toastController.create({
                        message: "Database imported successfully",
                        duration: 2000,
                        color: "success"
                    })
                })
                .catch((error) => {
                    return toastController.create({
                        message: error.message,
                        duration: 2000,
                        color: "danger"
                    })
                })
                .then((toast) => {
                    toast.present()
                })
        }

        const handleLogout = () => {
            cookies.remove("token")
            router.push("/login")
        }

        UserService.getUserMeUserMeGet().then((response) => {
            username.value = response.username
        }, (e: ApiError) => {
            console.log(e)
        })


        onMounted(async () => {
            const queryString = OpenAPI.BASE + "/user/profileimg"
            loadImg(queryString).then(blob => {

                blobUrl.value = URL.createObjectURL(blob)
            }).catch(() => {
                console.log("Profile image not found")
            })
        })

        return {
            cameraOutline,
            router,
            cookies,
            profilePic,
            blobUrl,
            handleLogout,
            toggleTheme,
            handleImportDatabase,
            openFileDialog,
            username,
            actionSheetButtons,
        }
    },
})

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
    border: 1px solid var(--ion-color-primary);
}

.change-profile-pic-button {
    position: absolute;
    top: 18px;
    left: 18px;
    scale: 0.3;
    height: 70px;
    width: 70px;
}

.ios .change-profile-pic-button {
    top: 5px;
    left: 5px;
}

.ios .ios-container {
    margin-top: 0px;
    height: 50px;
}

.ios ion-title {
    position: inherit;
}

ion-button {
    width: 80%;
    height: 50px;
}

ion-icon {
    scale: 2.0;
}

ion-modal {
    --height: 80%;
    --border-radius: 16px;
    --box-shadow: 0 10px 15px -3px rgb(0 0 0 / 0.1), 0 4px 6px -4px rgb(0 0 0 / 0.1);
}

ion-modal::part(backdrop) {
    background: var(--ion-color-dark);
    opacity: 1;
}
</style>

  