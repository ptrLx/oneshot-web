/* generated using openapi-typescript-codegen -- do no edit */
/* istanbul ignore file */
/* tslint:disable */
/* eslint-disable */
import type { Body_upload_image_image_upload_post } from '../models/Body_upload_image_image_upload_post';
import type { Happiness } from '../models/Happiness';
import type { OneShot } from '../models/OneShot';

import type { CancelablePromise } from '../core/CancelablePromise';
import { OpenAPI } from '../core/OpenAPI';
import { request as __request } from '../core/request';

export class OneShotService {

    /**
     * Upload Image
     * @param date
     * @param time
     * @param formData
     * @param happiness
     * @param text
     * @returns string Successful Response
     * @throws ApiError
     */
    public static uploadImageImageUploadPost(
        date: string,
        time: number,
        formData: Body_upload_image_image_upload_post,
        happiness?: (Happiness | null),
        text?: (string | null),
    ): CancelablePromise<string> {
        return __request(OpenAPI, {
            method: 'POST',
            url: '/image/upload',
            query: {
                'date': date,
                'time': time,
                'happiness': happiness,
                'text': text,
            },
            formData: formData,
            mediaType: 'multipart/form-data',
            errors: {
                422: `Validation Error`,
            },
        });
    }

    /**
     * Download Image
     * @param fileName
     * @param date
     * @returns any Successful Response
     * @throws ApiError
     */
    public static downloadImageImageDownloadGet(
        fileName?: (string | null),
        date?: (string | null),
    ): CancelablePromise<any> {
        return __request(OpenAPI, {
            method: 'GET',
            url: '/image/download',
            query: {
                'file_name': fileName,
                'date': date,
            },
            errors: {
                422: `Validation Error`,
            },
        });
    }

    /**
     * Delete Image
     * @param date
     * @returns string Successful Response
     * @throws ApiError
     */
    public static deleteImageImageDeletePost(
        date?: (string | null),
    ): CancelablePromise<string> {
        return __request(OpenAPI, {
            method: 'POST',
            url: '/image/delete',
            query: {
                'date': date,
            },
            errors: {
                422: `Validation Error`,
            },
        });
    }

    /**
     * Download Image
     * @param date
     * @returns any Successful Response
     * @throws ApiError
     */
    public static downloadImagePreviewGet(
        date?: (string | null),
    ): CancelablePromise<any> {
        return __request(OpenAPI, {
            method: 'GET',
            url: '/preview/',
            query: {
                'date': date,
            },
            errors: {
                422: `Validation Error`,
            },
        });
    }

    /**
     * Download Image
     * @param date
     * @returns OneShot Successful Response
     * @throws ApiError
     */
    public static downloadImageMetadataGet(
        date?: (string | null),
    ): CancelablePromise<OneShot> {
        return __request(OpenAPI, {
            method: 'GET',
            url: '/metadata/',
            query: {
                'date': date,
            },
            errors: {
                422: `Validation Error`,
            },
        });
    }

}
