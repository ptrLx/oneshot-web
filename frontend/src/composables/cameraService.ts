
import { ref, defineComponent } from 'vue';
import { Camera, CameraResultType, CameraSource, Photo } from '@capacitor/camera';
import { Filesystem, Directory } from '@capacitor/filesystem';
import { Preferences } from '@capacitor/preferences';


export interface UserPhoto {
    filepath: string,
    webviewPath?: string;
}


export const useCameraService = () => {
    const photos = ref<UserPhoto[]>([]);
    const takePhoto = async () => {
        const photo = await Camera.getPhoto({
            resultType: CameraResultType.Uri,
            source: CameraSource.Camera,
            quality: 100
        });
        const fileName = Date.now() + '.jpeg';
        const savedFileImage = {
            filepath: fileName,
            webviewPath: photo.webPath
        }
        photos.value = [savedFileImage, ...photos.value]
    }
    const pickPhoto = async () => {
        const photo = await Camera.pickImages({
            limit: 1,
            quality: 100
        });
        const savedFileImage = {
            filepath: photo.photos[0].path ?? Date.now() + '.jpeg',
            webviewPath: photo.photos[0].webPath
        }
        photos.value = [savedFileImage, ...photos.value]
    }

    return {
        takePhoto,
        pickPhoto,
        photos
    }

}

