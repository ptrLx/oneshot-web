import { HappinessDTO } from "@/_generated/api-client";
import { useImageService } from "./imageService";
import { OneShotUpdate } from '@/types/OneShotUpdate';

export const useImportExportService = () => {
    const {uploadGalleryImg} = useImageService();


    const openFileDialog = (elemId: string) => {
        console.log("Open file dialog");
        const fileUpload = document.getElementById(elemId);
        fileUpload?.click();
    }

    const importDatabase = async (event: Event) => {
        console.log("Import database");
        const input = event.target as HTMLInputElement;
        const files = input.files;
        const imageFiles = [];
        let json = null;

        if (files && files.length > 0) {
            // Make sure to get json data first
            for(let i = 0; i < files.length; i++) {
                console.log(files[i].name);
                if (isJson(files[i])) {
                    json = await parseJson(files[i]);
                }
                else {
                    imageFiles.push(files[i]);
                }             
            }
            
            if (!json) {
                throw new Error("Database import failed: no json file found.");
            }

            if (imageFiles.length === 0) {
                throw new Error("Database import failed: no image files found");
            }

            for (const image of imageFiles) {
                console.log(image);
                const matchingJsonObj = findMatchingJsonObj(json, image.name);
                if (matchingJsonObj) {
                    
                    // set happiness, if happiness is NOT_SPECIFIED, set to null
                    let happiness : HappinessDTO | null = null;
                    if (matchingJsonObj.happiness !== "NOT_SPECIFIED") {
                        happiness = matchingJsonObj.happiness;
                    }
                
                    const oneShotUpdate : OneShotUpdate = {
                        date: new Date(matchingJsonObj.date).toISOString().slice(0, 10),
                        time: matchingJsonObj.created,
                        happiness: happiness,
                        text: matchingJsonObj.textContent,
                    };

                    // Get webviewPath of image
                    const imgurl = URL.createObjectURL(image);

                    uploadGalleryImg(imgurl, oneShotUpdate);
                }
            }      
        }
    }

    const findMatchingJsonObj = (json: any, fileName: string) => {
        return json.find((obj: any) => obj.relativePath === fileName);
    }

    const isJson = (file: File) => {
        return file.type === "application/json";
    }

    const parseJson = (file: File): Promise<any> => {
        return new Promise((resolve, reject) => {
            const fileReader = new FileReader();
            fileReader.onload = (e) => {
                const result = e.target?.result;
                if (result) {
                    try {
                        const json = JSON.parse(result.toString());
                        resolve(json);
                    }
                    catch (err) {
                        reject(err);
                    }
                }
            };  
            fileReader.onerror = (err) => {
                reject(err);
            };
            fileReader.readAsText(file);
        })
    }

    return {
        openFileDialog,
        importDatabase
    }
}