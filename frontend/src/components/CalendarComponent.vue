<template>
    <ion-datetime class="datetime" presentation="date" display-format="DDDD MMMM D, YYYY" picker-format="DDDD MMMM D, YYYY"
        placeholder="Select Date" size="cover" :highlightedDates=highlightedDates></ion-datetime>
</template>
  
<script lang="ts">

import { IonCard, IonButton, IonTitle, IonGrid, IonRow, IonCol, IonDatetime, IonItem, IonList } from '@ionic/vue';
import { defineComponent } from 'vue';
import { Happiness } from '@/types/Happiness';
import { def } from '@vue/shared';
import { DatetimeHighlight } from '@ionic/core';


export default defineComponent({
    components: {
        IonCard,
        IonButton,
        IonTitle,
        IonGrid,
        IonRow,
        IonCol,
        IonDatetime,
        IonItem,
        IonList,
    },
    setup() {
        let highlightedDates: DatetimeHighlight[];

        // Dummy data until api call is implemented
        const api_response =
            [
                {
                    "date": "2023-11-16",
                    "happiness_state": "VERY_HAPPY",
                },
                {
                    "date": "2023-11-17",
                    "happiness_state": "HAPPY",
                },
                {
                    "date": "2023-11-18",
                    "happiness_state": "NEUTRAL",
                },
                {
                    "date": "2023-11-19",
                    "happiness_state": "SAD",
                },
                {
                    "date": "2023-11-20",
                    "happiness_state": "VERY_SAD",
                },
                {
                    "date": "2023-11-21",
                    "happiness_state": "NOT_SPECIFIED",
                },
            ]

        highlightedDates = api_response.map((item) => {
            backgroundColor: ['#41B883', '#A1C349', '#ccffcc', '#F2C94C', '#cc0000']
            let bgColor = "";
            switch (item.happiness_state as Happiness) {
                case Happiness.VERY_HAPPY:
                    bgColor = "#41B883";
                    break;
                case Happiness.HAPPY:
                    bgColor = "#A1C349";
                    break;
                case Happiness.NEUTRAL:
                    bgColor = "#ccffcc";
                    break;
                case Happiness.SAD:
                    bgColor = "#F2C94C";
                    break;
                case Happiness.VERY_SAD:
                    bgColor = "#cc0000";
                    break;
                case Happiness.NOT_SPECIFIED:
                    bgColor = "rgba(169, 169, 169, 0.2)";
                    break;
                default:
                    bgColor = "rgba(169, 169, 169, 0.2)";
                    break;
            }

            return {
                date: item.date,
                backgroundColor: bgColor
            }
        });




        return {

            highlightedDates
        }
    }
});

</script>
<style scoped>
.datetime {
    min-height: 0px;
    height: 100%;
}

ion-datetime {
    --background: var(--ion-color-light);
}

ion-datetime::part(calendar-day active),
ion-datetime::part(calendar-day):focus {
    background: color-mix(in srgb, var(--ion-color-primary), transparent 66%);
    box-shadow: 0px 0px 0px 4px color-mix(in srgb, var(--ion-color-primary), transparent 66%);
}

/* 
ion-datetime::part(calendar-day) {
    border: 1px dashed var(--ion-color-primary);
} */
</style>



