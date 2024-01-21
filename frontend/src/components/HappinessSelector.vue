<template>
    <div>
        <ion-radio-group v-model="selectedHappiness">
            <ion-row>
                <ion-col v-for="happiness in happinessOptions" :key="happiness.emoji" size="2">
                    <ion-radio :value="happiness.value" label-placement="stacked">
                        <ion-label
                            :class="{ 'selected-emoji': isSelected(happiness) }"
                            :style="{
                                fontSize: isSelected(happiness) ? '36px' : '30px',
                                border: isSelected(happiness)
                                    ? '2px solid var(--ion-color-primary)'
                                    : '2px solid transparent',
                            }"
                        >
                            {{ happiness.emoji }}
                        </ion-label>
                    </ion-radio>
                </ion-col>
            </ion-row>
        </ion-radio-group>
    </div>
</template>

<script lang="ts">
    import { defineComponent, ref, watch } from "vue"
    import { IonRadio, IonRadioGroup, IonRow, IonCol, IonLabel } from "@ionic/vue"
    import { HappinessDTO } from "@/_generated/api-client"

    export default defineComponent({
        components: {
            IonRadio,
            IonRadioGroup,
            IonRow,
            IonCol,
            IonLabel,
        },
        props: {
            defaultHappiness: {
                type: String,
                required: false,
            },
        },
        setup(props, { emit }) {
            const happinessOptions = [
                { emoji: "😄", value: HappinessDTO.VERY_HAPPY },
                { emoji: "😃", value: HappinessDTO.HAPPY },
                { emoji: "😐", value: HappinessDTO.NEUTRAL },
                { emoji: "😞", value: HappinessDTO.SAD },
                { emoji: "😢", value: HappinessDTO.VERY_SAD },
            ]

            const selectedHappiness = ref<HappinessDTO | null>(
                (props.defaultHappiness as HappinessDTO) || null,
            )

            watch(selectedHappiness, (newValue) => {
                emit("update:selectedHappiness", newValue)
            })

            const isSelected = (happiness: { value: HappinessDTO }) =>
                selectedHappiness.value === happiness.value

            return {
                selectedHappiness,
                happinessOptions,
                isSelected,
            }
        },
    })
</script>

<style scoped>
    .selected-emoji {
        font-size: 26px;
        border: 2px solid var(--ion-color-primary);
        border-radius: 50%;
        padding: 10px;

        display: flex;
        align-items: center;
        justify-content: center;
        width: 50px;
        height: 50px;
    }

    ion-radio::part(container),
    ion-radio::part(mark) {
        display: none;
    }

    ion-row {
        justify-content: space-evenly;
    }
</style>
