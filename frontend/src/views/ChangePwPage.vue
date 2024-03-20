<template>
    <base-layout page-title="Change Password">
        <div class="logo">
            <ion-icon :icon="warningOutline"></ion-icon>
        </div>
        <ion-grid class="ion-text-center">
            <ion-row>
                <ion-col size="12">
                    <ion-input
                        type="password"
                        label="Old password"
                        label-placement="floating"
                        fill="outline"
                        shape="round"
                        v-model="oldPw"
                    />
                </ion-col>
            </ion-row>
            <ion-row>
                <ion-col size="12">
                    <ion-input
                        type="password"
                        label="New password"
                        label-placement="floating"
                        fill="outline"
                        shape="round"
                        v-model="newPw"
                    />
                </ion-col>
            </ion-row>
            <ion-row>
                <ion-col>
                    <ion-button
                        @click="handleChangePw()"
                        shape="round"
                        color="danger"
                        :disabled="oldPw == undefined || newPw == undefined"
                    >
                        Change password
                    </ion-button>
                </ion-col>
            </ion-row>
        </ion-grid>
    </base-layout>
</template>

<script lang="ts">
    import { IonButton, IonGrid, IonRow, IonCol, IonIcon, IonInput, useIonRouter } from "@ionic/vue"
    import { warningOutline } from "ionicons/icons"
    import { defineComponent, ref } from "vue"
    import { ApiError } from "@/_generated/api-client"
    import { useThemeService } from "@/composables/themeService"
    import { deleteToken } from "@/service/authService"
    import { changeUserPw } from "@/service/profileService"
    import { showToastFail, showToastSuccess } from "@/function/notifyUser"

    export default defineComponent({
        components: {
            IonButton,
            IonGrid,
            IonRow,
            IonCol,
            IonIcon,
            IonInput,
        },
        setup() {
            const oldPw = ref<string | undefined>(undefined)
            const newPw = ref<string | undefined>(undefined)
            const router = useIonRouter()

            useThemeService(true) // Set theme to media preference

            function handleChangePw() {
                if (oldPw.value != undefined && newPw.value != undefined) {
                    changeUserPw(oldPw.value, newPw.value).then(
                        (msg) => {
                            showToastSuccess("Password changed successfully")
                            deleteToken()
                            router.back()
                        },
                        (e: ApiError) => {
                            showToastFail(e.body.detail)
                        },
                    )
                }
            }

            return {
                warningOutline,
                router,
                oldPw,
                newPw,
                handleChangePw,
            }
        },
    })
</script>

<style scoped>
    .logo {
        display: flex;
        justify-content: center;
        align-items: center;
        margin: 60px;
        scale: 2;
    }

    ion-button {
        width: 80%;
        height: 50px;
        margin-top: 20px;
    }

    ion-icon {
        scale: 2;
    }
</style>
