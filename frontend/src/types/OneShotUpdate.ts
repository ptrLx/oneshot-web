import { HappinessDTO } from "@/_generated/api-client";

export interface OneShotUpdate {
    date: string,
    time: number,
    happiness: HappinessDTO,
    text: string
}

