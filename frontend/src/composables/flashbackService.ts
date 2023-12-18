import { ApiError, FlashbackDTO, OneShotRespDTO, OneShotService } from '@/_generated/api-client';
import { useImageService } from '@/composables/imageService';

export const useFlashbackService = () => {

    const { downloadGalleryImg } = useImageService();

    const getFlashbacks = async (): Promise<{ [key: string]: string }> =>  {

        const flashbackImgs : { [key: string]: string } = {};

        await OneShotService.getFlashbacksFlashbackGet().then( async (res) => {

            // Dummy data, replace with next line when backend is implemented
            // const flashbacks = res;
            const flashbacks = {
                "random_happy": {
                "date": "2023-12-03",
                "time": 0,
                "happiness": "VERY_HAPPY",
                "text": "string",
                "file_name": "string"
                },
                "last_very_happy_day": {
                "date": "2023-12-04",
                "time": 0,
                "happiness": "VERY_HAPPY",
                "text": "string",
                "file_name": "string"
                },
                "same_day_last_month": {
                "date": "2023-12-05",
                "time": 0,
                "happiness": "VERY_HAPPY",
                "text": "string",
                "file_name": "string"
                },
                "same_date_last_years": [
                {
                    "date": "2023-12-06",
                    "time": 0,
                    "happiness": "VERY_HAPPY",
                    "text": "string",
                    "file_name": "string"
                }
                ]
            };
        
            // loop through all flashbacks and download the images
            for (const key of Object.keys(flashbacks)) {
                const flashback = flashbacks[key as keyof FlashbackDTO];
        
                if (Array.isArray(flashback)) {
        
                // Handly array type
                for (const item of flashback) {
                    const blob = await downloadGalleryImg(item.date);
                    const img = URL.createObjectURL(blob);
                    flashbackImgs[key] = img;
                }
                }
                else {
                // Handle single OneShotRespDTO type
                const blob = await downloadGalleryImg(flashback?.date ?? '');
                const img = URL.createObjectURL(blob);
                flashbackImgs[key] = img;
                }
            }
                
            }, (e: ApiError) => {
                console.log("Error retrieving flashbacks");
            });

            return flashbackImgs;
    }

    

    return {
        getFlashbacks
    }
};