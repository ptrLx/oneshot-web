/* generated using openapi-typescript-codegen -- do no edit */
/* istanbul ignore file */
/* tslint:disable */
/* eslint-disable */
import type { StatisticDTO } from "../models/StatisticDTO"

import type { CancelablePromise } from "../core/CancelablePromise"
import { OpenAPI } from "../core/OpenAPI"
import { request as __request } from "../core/request"

export class StatisticsService {
    /**
     * Get Statistics
     * @returns StatisticDTO Successful Response
     * @throws ApiError
     */
    public static getStatisticsStatsGet(): CancelablePromise<StatisticDTO> {
        return __request(OpenAPI, {
            method: "GET",
            url: "/stats/",
        })
    }
}
