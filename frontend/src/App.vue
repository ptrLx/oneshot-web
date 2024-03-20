<template>
    <ion-app>
        <ion-router-outlet />
    </ion-app>
</template>

<script setup lang="ts">
    import { IonApp, IonRouterOutlet } from "@ionic/vue"
    import { useHead } from "@vueuse/head"

    // --- Search Engine Optimization ---
    useHead({
        title: "OneShot",
        meta: [
            {
                name: "description",
                content:
                    "OneShot is made to remind you of the special moments.\
                    Because every day has at least one. And that's what counts in life!\
                    So make it your habit and remember the happy days!",
            },
            {
                name: "theme-color",
                content: "#feba4b",
            },
        ],
    })
</script>
