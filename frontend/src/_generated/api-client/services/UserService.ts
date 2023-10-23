/* generated using openapi-typescript-codegen -- do no edit */
/* istanbul ignore file */
/* tslint:disable */
/* eslint-disable */
import type { User } from '../models/User';

import type { CancelablePromise } from '../core/CancelablePromise';
import { OpenAPI } from '../core/OpenAPI';
import { request as __request } from '../core/request';

export class UserService {

    /**
     * Get User Me
     * @returns User Successful Response
     * @throws ApiError
     */
    public static getUserMeUserMeGet(): CancelablePromise<User> {
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
     * Change User Password
     * @param oldPassword
     * @param newPassword
     * @returns any Successful Response
     * @throws ApiError
     */
    public static changeUserPasswordUserchpwPost(
        oldPassword: any,
        newPassword: any,
    ): CancelablePromise<any> {
        return __request(OpenAPI, {
            method: 'POST',
            url: '/userchpw',
            query: {
                'old_password': oldPassword,
                'new_password': newPassword,
            },
            errors: {
                422: `Validation Error`,
            },
        });
    }

}
