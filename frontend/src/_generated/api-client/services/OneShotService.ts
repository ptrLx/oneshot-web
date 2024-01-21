/* generated using openapi-typescript-codegen -- do no edit */
/* istanbul ignore file */
/* tslint:disable */
/* eslint-disable */
import type { Body_upload_image_image_upload_post } from "../models/Body_upload_image_image_upload_post"
import type { FlashbackDTO } from "../models/FlashbackDTO"
import type { HappinessDTO } from "../models/HappinessDTO"
import type { OneShotRespDTO } from "../models/OneShotRespDTO"

import type { CancelablePromise } from "../core/CancelablePromise"
import { OpenAPI } from "../core/OpenAPI"
import { request as __request } from "../core/request"

export class OneShotService {
    /**
     * Upload Image
     * @param date
     * @param time
     * @param formData
     * @param happiness
     * @param text
     * @returns OneShotRespDTO Successful Response
     * @throws ApiError
     */
    public static uploadImageImageUploadPost(
        date: string,
        time: number,
        formData: Body_upload_image_image_upload_post,
        happiness?: HappinessDTO | null,
        text?: string | null,
    ): CancelablePromise<OneShotRespDTO> {
        return __request(OpenAPI, {
            method: "POST",
            url: "/image/upload",
            query: {
                date: date,
                time: time,
                happiness: happiness,
                text: text,
            },
            formData: formData,
            mediaType: "multipart/form-data",
            errors: {
                422: `Validation Error`,
            },
        })
    }

    /**
     * Download Image
     * @param fileName
     * @param date
     * @param preview
     * @returns any Successful Response
     * @throws ApiError
     */
    public static downloadImageImageDownloadGet(
        fileName?: string | null,
        date?: string | null,
        preview: boolean = false,
    ): CancelablePromise<any> {
        return __request(OpenAPI, {
            method: "GET",
            url: "/image/download",
            query: {
                file_name: fileName,
                date: date,
                preview: preview,
            },
            errors: {
                422: `Validation Error`,
            },
        })
    }

    /**
     * Delete Image
     * @param date
     * @returns string Successful Response
     * @throws ApiError
     */
    public static deleteImageImageDeletePost(date?: string | null): CancelablePromise<string> {
        return __request(OpenAPI, {
            method: "POST",
            url: "/image/delete",
            query: {
                date: date,
            },
            errors: {
                422: `Validation Error`,
            },
        })
    }

    /**
     * Paginate Gallery
     * @param page
     * @param maxPageSize
     * @returns OneShotRespDTO Successful Response
     * @throws ApiError
     */
    public static paginateGalleryImageGalleryGet(
        page?: number,
        maxPageSize: number = 20,
    ): CancelablePromise<Array<OneShotRespDTO>> {
        return __request(OpenAPI, {
            method: "GET",
            url: "/image/gallery",
            query: {
                page: page,
                max_page_size: maxPageSize,
            },
            errors: {
                422: `Validation Error`,
            },
        })
    }

    /**
     * Get Metadata
     * @param date
     * @returns OneShotRespDTO Successful Response
     * @throws ApiError
     */
    public static getMetadataMetadataGet(date?: string | null): CancelablePromise<OneShotRespDTO> {
        return __request(OpenAPI, {
            method: "GET",
            url: "/metadata/",
            query: {
                date: date,
            },
            errors: {
                422: `Validation Error`,
            },
        })
    }

    /**
     * Update Metadata
     * @param date
     * @param time
     * @param happiness
     * @param text
     * @returns OneShotRespDTO Successful Response
     * @throws ApiError
     */
    public static updateMetadataMetadataUpdatePost(
        date: string,
        time?: number | null,
        happiness?: HappinessDTO | null,
        text?: string | null,
    ): CancelablePromise<OneShotRespDTO> {
        return __request(OpenAPI, {
            method: "POST",
            url: "/metadata/update",
            query: {
                date: date,
                time: time,
                happiness: happiness,
                text: text,
            },
            errors: {
                422: `Validation Error`,
            },
        })
    }

    /**
     * Get Flashbacks
     * @returns FlashbackDTO Successful Response
     * @throws ApiError
     */
    public static getFlashbacksFlashbackGet(): CancelablePromise<FlashbackDTO> {
        return __request(OpenAPI, {
            method: "GET",
            url: "/flashback/",
        })
    }
}
