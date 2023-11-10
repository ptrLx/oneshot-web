<template>
    <div>
        <ion-radio-group v-model="selectedHappiness">
            <ion-row>
                <ion-col v-for="happiness in happinessOptions" :key="happiness.emoji" size="2">
                    <ion-radio :value="happiness.value" label-placement="stacked">
                        <ion-label :class="{ 'selected-emoji': isSelected(happiness) }" :style="{
                            fontSize: isSelected(happiness) ? '36px' : '30px',
                            border: isSelected(happiness) ? '2px solid var(--ion-color-primary)' : '2px solid transparent'
                        }">
                            {{ happiness.emoji }}
                        </ion-label>
                    </ion-radio>
                </ion-col>
            </ion-row>
        </ion-radio-group>
    </div>
</template>
  
<script lang="ts">
import { defineComponent, ref, watch } from 'vue';
import { IonRadio, IonRadioGroup, IonRow, IonCol, IonLabel } from '@ionic/vue';
import { Happiness } from '@/types/Happiness';
import { computed } from '@vue/reactivity';

export default defineComponent({
    components: {
        IonRadio,
        IonRadioGroup,
        IonRow,
        IonCol,
        IonLabel,
    },
    setup(props, { emit }) {
        const selectedHappiness = ref<Happiness>(Happiness.NOT_SPECIFIED);
        const happinessOptions = [
            { emoji: '😄', value: Happiness.VERY_HAPPY },
            { emoji: '😃', value: Happiness.HAPPY },
            { emoji: '😐', value: Happiness.NEUTRAL },
            { emoji: '😞', value: Happiness.SAD },
            { emoji: '😢', value: Happiness.VERY_SAD },
        ];

        watch(selectedHappiness, (newValue) => {
            console.log('selectedHappiness changed to', newValue);
            emit('update:selectedHappiness', newValue)
        });

        const isSelected = (happiness: { value: Happiness; }) =>
            selectedHappiness.value === happiness.value;

        return {
            selectedHappiness,
            happinessOptions,
            isSelected
        };
    },
});
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
  