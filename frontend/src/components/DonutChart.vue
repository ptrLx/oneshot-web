<template>
    <div class="donut-container">
        <Doughnut class="donut" :data="happinessData" :options="options" :plugins="plugins" ref="doughnutChart" />
    </div>
</template>
  
<script lang="ts">
import { IonAccordion } from '@ionic/vue'
import { Chart as ChartJS, ArcElement, Tooltip, Legend } from 'chart.js'
import { computed, defineComponent, onMounted, ref } from 'vue'
import { Doughnut } from 'vue-chartjs'

ChartJS.register(ArcElement, Tooltip, Legend)

export default defineComponent({
    components: {
        Doughnut
    },
    props: {
        centerText: {
            type: String,
            default: ''
        },
        data: {
            type: Object,
            default: () => ({})
        },
    },
    setup(props) {
        const ionicFontFamily = getComputedStyle(document.documentElement).getPropertyValue('--ion-font-family').trim()
        const primaryContrast = getComputedStyle(document.documentElement).getPropertyValue('--ion-color-primary-contrast').trim()

        const donutLabel = {
            id: 'donut-label',
            beforeDatasetsDraw(chart: { getDatasetMeta?: any; ctx?: any; data?: any }, args: any, pluginOptions: any) {
                const { ctx, data } = chart;
                ctx.save();
                const xCoor = chart.getDatasetMeta(0).data[0].x;
                const yCoor = chart.getDatasetMeta(0).data[0].y;
                ctx.font = '20px ' + ionicFontFamily;
                ctx.fillStyle = primaryContrast;
                ctx.textAlign = 'center';
                ctx.textBaseline = 'middle';
                ctx.fillText(props.centerText, xCoor, yCoor);
            }
        }

        const happinessData = computed(() => {

            let data = [
                props.data.VERY_HAPPY || 0,
                props.data.HAPPY || 0,
                props.data.NEUTRAL || 0,
                props.data.SAD || 0,
                props.data.VERY_SAD || 0,
                props.data.NOT_SPECIFIED || 0
            ]

            const colors = [
                getComputedStyle(document.documentElement).getPropertyValue('--color-very-happy').trim(),
                getComputedStyle(document.documentElement).getPropertyValue('--color-happy').trim(),
                getComputedStyle(document.documentElement).getPropertyValue('--color-neutral').trim(),
                getComputedStyle(document.documentElement).getPropertyValue('--color-sad').trim(),
                getComputedStyle(document.documentElement).getPropertyValue('--color-very-sad').trim(),
                getComputedStyle(document.documentElement).getPropertyValue('--color-not-specified').trim(),
            ]

            return {
                labels: ['Very Happy', 'Happy', 'Neutral', 'Sad', 'Very Sad', 'Not Specified'],
                datasets: [
                    {
                        backgroundColor: colors,
                        data: data
                    }
                ]
            }
        })

        const options = {
            responsive: true,
            maintainAspectRatio: false,
            cutout: 90,
            borderColor: 'transparent',
            color: primaryContrast,
            spacing: 5,
            animation: {
                animateRotate: true,
                animationEasing: 'linear',
                duration: 5000,
            },

        }

        const plugins = [donutLabel]

        return {
            happinessData,
            options,
            plugins
        }
    }
})
</script>

<style scoped>
.donut-container {
    width: 90%;
    height: 90%;
    margin: 20px;
    align-items: center;
    justify-content: center;
}

.donut {
    width: 100%;
    height: 100%;
}
</style>
  