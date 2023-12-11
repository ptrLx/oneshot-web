<template>
    <ion-datetime id="calendar" class="datetime" presentation="date" display-format="DDDD MMMM D, YYYY"
        picker-format="DDDD MMMM D, YYYY" placeholder="Select Date" size="cover" :highlightedDates="highlightedDates"
        :value="selectedDate.toISOString()"></ion-datetime>
</template>
  
<script lang="ts">
import { IonDatetime, onIonViewDidEnter } from '@ionic/vue';
import { defineComponent, ref, onMounted, watch, nextTick } from 'vue';
import { CalendarService } from '@/_generated/api-client';
import { CalendarEntryRespDTO } from '@/_generated/api-client/models/CalendarEntryRespDTO';
import { HappinessDTO } from '@/_generated/api-client/models/HappinessDTO';

export default defineComponent({
    components: {
        IonDatetime,
    },
    setup() {


        const selectedDate = new Date();
        const displayedMonth = ref<string>('');
        const highlightedDates = ref<{ date: string; textColor: string, backgroundColor: string }[]>();
        const observeCalendarChanges = () => {
            const targetNode = document.querySelector('ion-datetime#calendar');
            if (!targetNode) return;

            const observerCallback = (mutationsList: MutationRecord[]) => {
                for (const mutation of mutationsList) {
                    if (mutation.type === 'attributes') {
                        const calendar = document.querySelector('ion-datetime#calendar');
                        const label = calendar?.shadowRoot?.querySelector('.calendar-month-year ion-item ion-label');
                        const textContent = label?.textContent;

                        if (textContent && textContent !== displayedMonth.value) {
                            displayedMonth.value = textContent
                            handleMonthChange(textContent);
                            console.log(textContent);
                        }
                    }
                }
            };

            const observer = new MutationObserver(observerCallback);
            observer.observe(targetNode, { attributes: true, childList: true, subtree: true });
        };

        onMounted(observeCalendarChanges);

        const handleMonthChange = (dateText: string) => {
            selectedDate.setMonth(new Date(`1 ${dateText}`).getMonth());
            const formattedDate = formatDisplayDate(dateText);
            CalendarService.getCalendarCalendarGet(formattedDate).then((response) => {
                highlightedDates.value = updateHighlightedDates(response);
            });
        };

        const formatDisplayDate = (dateText: string) => {
            const date = new Date(`1 ${dateText}`);
            const year = date.getFullYear();
            const month = date.getMonth() + 1;
            return `${year}-${month.toString().padStart(2, '0')}`;
        };

        const updateHighlightedDates = (response: CalendarEntryRespDTO[]) => {
            let result = response.map((item) => {
                let bgColor = '';
                const happinessState = item.oneshot?.happiness;
                switch (happinessState) {
                    case HappinessDTO.VERY_HAPPY:
                        bgColor = 'var(--color-very-happy)';
                        break;
                    case HappinessDTO.HAPPY:
                        bgColor = 'var(--color-happy)';
                        break;
                    case HappinessDTO.NEUTRAL:
                        bgColor = 'var(--color-neutral)';
                        break;
                    case HappinessDTO.SAD:
                        bgColor = 'var(--color-sad)';
                        break;
                    case HappinessDTO.VERY_SAD:
                        bgColor = 'var(--color-very-sad)';
                        break;
                    default:
                        bgColor = 'var(--color-unspecified)';
                        break;
                }

                return {
                    date: item.date,
                    textColor: 'var(--ion-color-light)',
                    backgroundColor: bgColor,
                };
            });

            return result;
        };

        return {
            highlightedDates,
            selectedDate,
        };
    },
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
  