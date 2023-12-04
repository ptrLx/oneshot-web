/* generated using openapi-typescript-codegen -- do no edit */
/* istanbul ignore file */
/* tslint:disable */
/* eslint-disable */

import type { HappinessDTO } from './HappinessDTO';

/**
 * Output model for a OneShot.
 */
export type OneShotRespDTO = {
    date: string;
    time: number;
    happiness?: (HappinessDTO | null);
    text?: (string | null);
    file_name: string;
};

