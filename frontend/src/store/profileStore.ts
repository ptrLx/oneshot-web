import { defineStore } from "pinia"

export const useProfileStore = defineStore("profile", {
    state: () => ({
        userName: undefined as string | undefined,
    }),
    getters: {},
    actions: {},
})
