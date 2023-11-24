<template>
    <base-layout page-title="Change Password">

        <div class="logo">
            <ion-icon :icon="warningOutline"></ion-icon>
        </div>
        <!-- Login Section -->
        <ion-grid class="ion-text-center">
            <ion-row>
                <ion-col size="12">
                    <ion-input type="password" label="Old password" label-placement="floating" fill="outline" shape="round"
                        v-model="oldpw" placeholder="Enter old password">
                    </ion-input>
                </ion-col>
            </ion-row>
            <ion-row>
                <ion-col size="12">
                    <ion-input type="password" label="New password" label-placement="floating" fill="outline" shape="round"
                        v-model="newpw" placeholder="Enter new password">
                    </ion-input>
                </ion-col>
            </ion-row>
            <ion-row>
                <ion-col size="12">
                    <ion-button @click="handlechangePw()" shape="round" color="danger">Change Password</ion-button>
                </ion-col>
            </ion-row>
        </ion-grid>
    </base-layout>
</template>
  
<script lang="ts">
import { IonAvatar, IonButton, IonGrid, IonRow, IonCol, IonIcon, IonInput, useIonRouter, IonToast, toastController, IonText } from '@ionic/vue';
import { warningOutline } from 'ionicons/icons';
import { defineComponent, popScopeId, ref } from 'vue';
import { OneShotService, UserService, Token, OpenAPI, ApiError } from '@/_generated/api-client';
import { useCookies } from 'vue3-cookies'
import { routerKey } from 'vue-router';

export default defineComponent({
    components: {
        IonAvatar,
        IonButton,
        IonGrid,
        IonRow,
        IonCol,
        IonIcon,
        IonInput,
        IonText,
        IonToast
    },
    setup() {
        const { cookies } = useCookies();
        const oldpw = ref<string>("");
        const newpw = ref<string>("");
        const router = useIonRouter();

        const requestUserInfo = () => {
            UserService.getUserMeUserMeGet().then((user) => {
                console.log(user.username)
            })
        }

        const showToastSuccess = () => {
            toastController.create({
                message: 'Password changed successfully',
                duration: 2000,
                color: 'success'
            }).then((toast) => {
                toast.present();
            });
        }

        const showToastFail = (msg: string) => {
            toastController.create({
                message: msg,
                duration: 2000,
                color: 'danger'
            }).then((toast) => {
                toast.present();
            });
        }

        const handlechangePw = () => {

            UserService.changeUserPasswordUserChpwPost(oldpw.value, newpw.value).then(() => {
                showToastSuccess();
                router.back();
            }, (e: ApiError) => {
                showToastFail(e.body.detail);
            })
        }

        return {
            warningOutline,
            cookies,
            router,
            oldpw,
            newpw,
            handlechangePw
        };
    },
});

</script>

<style scoped>
.logo {
    display: flex;
    justify-content: center;
    align-items: center;
    margin: 60px;
    scale: 2.0;
}


ion-button {
    width: 80%;
    height: 50px;
    margin-top: 20px;
}

ion-icon {
    scale: 2.0;
}
</style>

  