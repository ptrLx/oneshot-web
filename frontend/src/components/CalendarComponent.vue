<template>
    <ion-datetime ref="datetime" id="calendar" :class="{'datetime-dark': themeIsDark, 'datetime-light': !themeIsDark}"
     presentation="date" display-format="DDDD MMMM D, YYYY"
        picker-format="DDDD MMMM D, YYYY" placeholder="Select Date" size="cover" :highlightedDates="highlightedDates"
        v-model="selectedDate"></ion-datetime>
    <ion-button shape="round" @click="handleSelection">
        Select
    </ion-button>
</template>
  
<script lang="ts">
import { IonDatetime, IonButton } from "@ionic/vue"
import { defineComponent, ref, onMounted, computed } from "vue"
import { useRouter } from "vue-router"
import { CalendarService } from "@/_generated/api-client"
import { CalendarEntryRespDTO } from "@/_generated/api-client/models/CalendarEntryRespDTO"
import { HappinessDTO } from "@/_generated/api-client/models/HappinessDTO"
import { OneShotService } from "@/_generated/api-client"
import { theme } from "@/composables/store"

export default defineComponent({
    components: {
        IonDatetime,
        IonButton,
    },
    setup() {

        const router = useRouter()
        const selectedDate = ref<string>((new Date).toISOString())
        const displayedMonth = ref<string>("")
        const highlightedDates = ref<{ date: string; textColor: string, backgroundColor: string }[]>()
        const themeIsDark = computed(() => {
            if (theme.isSet()) {
                return theme.getTheme() === "dark"
            } else { // media preferred
                return window.matchMedia("(prefers-color-scheme: dark)").matches
            }
        })
            

        const observeCalendarChanges = () => {
            const targetNode = document.querySelector("ion-datetime#calendar")
            if (!targetNode) return

            const observerCallback = (mutationsList: MutationRecord[]) => {
                for (const mutation of mutationsList) {
                    if (mutation.type === "attributes") {
                        const calendar = document.querySelector("ion-datetime#calendar")
                        const label = calendar?.shadowRoot?.querySelector(".calendar-month-year ion-item ion-label")
                        const textContent = label?.textContent

                        if (textContent && textContent !== displayedMonth.value) {
                            displayedMonth.value = textContent
                            handleMonthChange(textContent)
                        }
                    }
                }
            }

            const observer = new MutationObserver(observerCallback)
            observer.observe(targetNode, { attributes: true, childList: true, subtree: true })
        }

        onMounted(observeCalendarChanges)

        const handleMonthChange = (dateText: string) => {
            const formattedDate = formatDisplayDate(dateText)
            CalendarService.getCalendarCalendarGet(formattedDate).then((response) => {
                highlightedDates.value = updateHighlightedDates(response)
            })
        }

        const formatDisplayDate = (dateText: string) => {
            const date = new Date(`1 ${dateText}`)
            const year = date.getFullYear()
            const month = date.getMonth() + 1
            return `${year}-${month.toString().padStart(2, "0")}`
        }

        const updateHighlightedDates = (response: CalendarEntryRespDTO[]) => {
            const result = response.map((item) => {
                let bgColor = ""
                const happinessState = item.oneshot?.happiness
                switch (happinessState) {
                    case HappinessDTO.VERY_HAPPY:
                        bgColor = "var(--color-very-happy)"
                        break
                    case HappinessDTO.HAPPY:
                        bgColor = "var(--color-happy)"
                        break
                    case HappinessDTO.NEUTRAL:
                        bgColor = "var(--color-neutral)"
                        break
                    case HappinessDTO.SAD:
                        bgColor = "var(--color-sad)"
                        break
                    case HappinessDTO.VERY_SAD:
                        bgColor = "var(--color-very-sad)"
                        break
                    case null: // Unspecified happiness
                        bgColor = "var(--color-unspecified)"
                        break
                    default:
                        bgColor = "var(--color-none)"
                        break
                }

                return {
                    date: item.date,
                    textColor: "var(--ion-color-light)",
                    backgroundColor: bgColor,
                }
            })

            return result
        }

        const handleSelection = async () => {
            const formattedDate = new Date(selectedDate.value).toLocaleDateString("en-CA")
            OneShotService.getMetadataMetadataGet(formattedDate).then(() => {
                router.push("/image/" + formattedDate)
            }, () => {
                console.log("No image for this date exists")
            })
        }

        return {
            highlightedDates,
            selectedDate,
            handleSelection,
            themeIsDark,
        }
    },
})
</script>
  
<style scoped>
.datetime-light{
    min-height: 0px;
    height: 100%;
    --ion-color-step-500: var(--ion-color-dark);
    --background: var(--ion-color-light);
    color: var(--ion-color-dark-tint);
    padding-bottom: 50px;
}

.datetime-dark {
    min-height: 0px;
    height: 100%;
    --ion-color-step-500: var(--ion-color-primary);
    --background: var(--ion-color-light);
    color: var(--ion-color-dark);
    padding-bottom: 50px;
}

ion-datetime::part(calendar-day today) {
    box-shadow: 0px 0px 0px 5px color-mix(in srgb, var(--ion-color-primary), transparent 66%);
}

ion-datetime::part(calendar-day active),
ion-datetime::part(calendar-day):focus {
    background: color-mix(in srgb, var(--ion-color-primary), transparent 66%);
    box-shadow: 0px 0px 0px 4px color-mix(in srgb, var(--ion-color-primary), transparent 66%);
}

ion-button {
    /* always on top */
    position: absolute;
    top: 84%;
    right: 4%;
}

/* 
  ion-datetime::part(calendar-day) {
    border: 1px dashed var(--ion-color-primary);
  } */
</style>
  