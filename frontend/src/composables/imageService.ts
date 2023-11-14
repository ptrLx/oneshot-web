import FormData from 'form-data'
import axios, { AxiosRequestConfig } from 'axios';
import { OpenAPI } from '@/_generated/api-client';
import { OneShotUpdate } from '@/types/OneShotUpdate';
import { Happiness } from '@/types/Happiness';
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
    
    const uploadGalleryImg = async (src: string, data: OneShotUpdate) => {
        let endpoint = OpenAPI.BASE + "/image/upload";
        const fileName = `${data.date}_${data.time}.png`;

        const params = new URLSearchParams();
        params.append('date', data.date);
        params.append('time', Math.floor(data.time).toString());
        params.append('happiness', data.happiness);
        params.append('text', data.text);

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
    
            console.log('Upload successful', response);
            return response;
        } catch (error) {
            console.log('Error uploading image', error);
            return error;
        }
    };
    
    

    return {
        loadImg,
        uploadProfileImg,
        uploadGalleryImg
    }
}