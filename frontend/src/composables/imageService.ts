import FormData from 'form-data'
import axios, { AxiosRequestConfig } from 'axios';
import { OpenAPI } from '@/_generated/api-client';

export const useImageService = () => {

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

    const uploadImg = async (src: string) => {

        try {
            const file = await fetch(src).then(res => res.blob());
            console.log(file);
            const formData = new FormData();
            formData.append('file', file, 'profile.png');

            const endpoint = OpenAPI.BASE + "/user/profileimg";
            const response = await axios.post(endpoint, formData, {
                headers: {
                    'Content-Type': 'multipart/form-data',
                    'Authorization': 'Bearer ' + OpenAPI.TOKEN,
                }
            });
            console.log('Upload successful', response);
        }
        catch (error) {
            console.log('Error uploading image', error);
        }
    }

    return {
        loadImg,
        uploadImg
    }
}