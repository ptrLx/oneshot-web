<template>
    <div>
        <ion-radio-group v-model="selectedHappiness">
            <ion-row>
                <ion-col v-for="happiness in happinessOptions" :key="happiness" size="2">
                    <ion-radio :value="happiness" label-placement="stacked">
                        <ion-label :class="{ 'selected-emoji': selectedHappiness === happiness }"
                            :style="{ fontSize: selectedHappiness === happiness ? '36px' : '30px', border: selectedHappiness === happiness ? '2px solid var(--ion-color-primary)' : '2px solid transparent' }">
                            {{ happiness }}
                        </ion-label>
                    </ion-radio>
                </ion-col>
            </ion-row>
        </ion-radio-group>
    </div>
</template>
  
<script lang="ts">
import { defineComponent, ref } from 'vue';
import { IonRadio, IonRadioGroup, IonRow, IonCol, IonLabel } from '@ionic/vue';

export default defineComponent({
    components: {
        IonRadio,
        IonRadioGroup,
        IonRow,
        IonCol,
        IonLabel,
    },
    setup() {
        const selectedHappiness = ref<string | null>(null);
        const happinessOptions = ['😄', '😃', '😐', '😞', '😢'];

        return {
            selectedHappiness,
            happinessOptions,
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
  