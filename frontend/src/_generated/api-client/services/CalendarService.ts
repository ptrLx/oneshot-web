/* generated using openapi-typescript-codegen -- do no edit */
/* istanbul ignore file */
/* tslint:disable */
/* eslint-disable */
import type { CalendarEntryRespDTO } from "../models/CalendarEntryRespDTO"

import type { CancelablePromise } from "../core/CancelablePromise"
import { OpenAPI } from "../core/OpenAPI"
import { request as __request } from "../core/request"

export class CalendarService {
    /**
     * Get Calendar
     * @param month
     * @returns CalendarEntryRespDTO Successful Response
     * @throws ApiError
     */
    public static getCalendarCalendarGet(
        month: string,
    ): CancelablePromise<Array<CalendarEntryRespDTO>> {
        return __request(OpenAPI, {
            method: "GET",
            url: "/calendar/",
            query: {
                month: month,
            },
            errors: {
                422: `Validation Error`,
            },
        })
    }
}
