/* generated using openapi-typescript-codegen -- do no edit */
/* istanbul ignore file */
/* tslint:disable */
/* eslint-disable */
import type { Body_login_for_access_token_login__post } from '../models/Body_login_for_access_token_login__post';
import type { Body_upload_user_profile_img_user_profileimg_post } from '../models/Body_upload_user_profile_img_user_profileimg_post';
import type { TokenDTO } from '../models/TokenDTO';
import type { UserDTO } from '../models/UserDTO';

import type { CancelablePromise } from '../core/CancelablePromise';
import { OpenAPI } from '../core/OpenAPI';
import { request as __request } from '../core/request';

export class UserService {

    /**
     * Get User Me
     * @returns UserDTO Successful Response
     * @throws ApiError
     */
    public static getUserMeUserMeGet(): CancelablePromise<UserDTO> {
        return __request(OpenAPI, {
            method: 'GET',
            url: '/user/me',
        });
    }

    /**
     * Get User Profile Img
     * @returns any Successful Response
     * @throws ApiError
     */
    public static getUserProfileImgUserProfileimgGet(): CancelablePromise<any> {
        return __request(OpenAPI, {
            method: 'GET',
            url: '/user/profileimg',
        });
    }

    /**
     * Upload User Profile Img
     * @param formData
     * @returns string Successful Response
     * @throws ApiError
     */
    public static uploadUserProfileImgUserProfileimgPost(
        formData: Body_upload_user_profile_img_user_profileimg_post,
    ): CancelablePromise<string> {
        return __request(OpenAPI, {
            method: 'POST',
            url: '/user/profileimg',
            formData: formData,
            mediaType: 'multipart/form-data',
            errors: {
                422: `Validation Error`,
            },
        });
    }

    /**
     * Change User Password
     * @param oldPassword
     * @param newPassword
     * @returns string Successful Response
     * @throws ApiError
     */
    public static changeUserPasswordUserChpwPost(
        oldPassword: any,
        newPassword: any,
    ): CancelablePromise<string> {
        return __request(OpenAPI, {
            method: 'POST',
            url: '/user/chpw',
            query: {
                'old_password': oldPassword,
                'new_password': newPassword,
            },
            errors: {
                422: `Validation Error`,
            },
        });
    }

    /**
     * Login For Access Token
     * @param formData
     * @returns TokenDTO Successful Response
     * @throws ApiError
     */
    public static loginForAccessTokenLoginPost(
        formData: Body_login_for_access_token_login__post,
    ): CancelablePromise<TokenDTO> {
        return __request(OpenAPI, {
            method: 'POST',
            url: '/login/',
            formData: formData,
            mediaType: 'application/x-www-form-urlencoded',
            errors: {
                422: `Validation Error`,
            },
        });
    }

}
