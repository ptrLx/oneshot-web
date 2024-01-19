import { FlashbackDTO, OneShotRespDTO, OneShotService } from "@/_generated/api-client"
import { useImageService } from "@/composables/imageService"

/**
 * Type which contains the url to the image blob and the meta data of the flashback
 */
export interface FlashbackUrlAndMeta {
    url: string;
    meta: OneShotRespDTO
}

export const useFlashbackService = () => {

    const { downloadGalleryImg } = useImageService()

    // key: string is the category of the flashback, e.g. "random_happy", "last_very_happy_day" etc.
    const getFlashbacks = async (): Promise<{ [key: string]: FlashbackUrlAndMeta }> =>  {

        const isPreview = true
        const flashbackImgs : { [key: string]: FlashbackUrlAndMeta } = {}

        await OneShotService.getFlashbacksFlashbackGet().then( async (res) => {
            const flashbacks = res
            
            // loop through all flashbacks and download the images
            for (const key of Object.keys(flashbacks)) {
                const flashback = flashbacks[key as keyof FlashbackDTO]
        
                if (Array.isArray(flashback)) {
        
                    // Handly array type
                    for (const item of flashback) {
                        await downloadGalleryImg(item.date, isPreview).then((blob) => {
                            const img = URL.createObjectURL(blob)
                            // create new key for each item in the array <key>_0, <key>_1, ...
                            // and add the image url and meta data to the object
                            const newKey = `${key}_${flashback.indexOf(item)}`
                            flashbackImgs[newKey] = {
                                url: img,
                                meta: item as OneShotRespDTO
                            }
                        }, () => {
                            return // Skip this item if it can't be downloaded
                        })
                    }
                }
                else {
                    if (flashback === null) {
                        continue
                    }

                    // Handle single OneShotRespDTO type
                    await downloadGalleryImg(flashback?.date ?? "", isPreview).then((blob) => {
                        const img = URL.createObjectURL(blob)
                        flashbackImgs[key] = {
                            url: img,
                            meta: flashback as OneShotRespDTO
                        }
                    }, () => {
                        return // Skip this item if it can't be downloaded
                    })
                }
            }

        }, () => {
            console.log("Error retrieving flashbacks")
        })

        return flashbackImgs
    }

    

    return {
        getFlashbacks
    }
}