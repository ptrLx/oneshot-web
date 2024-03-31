import { toastController } from "@ionic/vue"

export function showToastSuccess(msg: string) {
    toastController
        .create({
            message: msg,
            duration: 2000,
            color: "success",
        })
        .then((toast) => {
            toast.present()
        })
}

export function showToastFail(msg: string) {
    toastController
        .create({
            message: msg,
            duration: 2000,
            color: "danger",
        })
        .then((toast) => {
            toast.present()
        })
}
