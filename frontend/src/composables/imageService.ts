import FormData from 'form-data'
import axios, { AxiosRequestConfig } from 'axios';
import { OneShotRespDTO, OpenAPI } from '@/_generated/api-client';
import { useCookies } from 'vue3-cookies'

export const useImageService = () => {

    const { cookies } = useCookies();
    OpenAPI.TOKEN = cookies.get("token");

    const loadImg = async (src: string) => {

        const config: AxiosRequestConfig<any> = {
            url: src,
            method: "get",
            responseType: "blob",
            headers: {
                "Authorization": `Bearer ${OpenAPI.TOKEN}`
            }
        }
        const response = await axios.request(config)
        return response.data // the blob    
    }

    const uploadProfileImg = async (src: string) => {
        const endpoint = OpenAPI.BASE + "/user/profileimg";
        const fileName = 'profile.png';

        return await uploadImage(src, endpoint, fileName);
    };

    const downloadGalleryImg = async (date: string, preview = true) => {
        let endpoint = OpenAPI.BASE + "/image/download";

        const params = new URLSearchParams();

        params.append('date', date);
        params.append('preview', preview.toString());

        endpoint += `?${params.toString()}`

        return await loadImg(endpoint);
    }

    const uploadGalleryImg = async (src: string, data: Omit<OneShotRespDTO, 'file_name'>) => {
        let endpoint = OpenAPI.BASE + "/image/upload";
        const fileName = `${data.date}_${data.time}.png`;

        const params = new URLSearchParams();
        params.append('date', data.date);
        params.append('time', Math.floor(data.time).toString());
        if (data.happiness !== null){
            params.append('happiness', data.happiness?.toString() || '');
        }    
        params.append('text', data.text?.toString() || '');

        endpoint += `?${params.toString()}`

        return await uploadImage(src, endpoint, fileName);
    };

    const uploadImage = async (
        src: string,
        endpoint: string,
        fileName: string,
        headers: Record<string, string> = {}
    ) => {
        try {
            const file = await fetch(src).then(res => res.blob());
            const formData = new FormData();
            formData.append('file', file, fileName);

            const response = await axios.post(endpoint, formData, {
                headers: {
                    'Authorization': 'Bearer ' + OpenAPI.TOKEN,
                    'Content-Type': 'multipart/form-data',
                    ...headers,
                },
            });

            console.log('Image Upload successful');
            return response;
        } catch (error) {
            console.log('Error uploading image');
            return error;
        }
    };

    return {
        loadImg,
        uploadProfileImg,
        uploadGalleryImg,
        downloadGalleryImg
    }
}