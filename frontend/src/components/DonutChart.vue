<template>
    <div class="donut-container">
        <Doughnut class="donut" :data="data" :options="options" :plugins="plugins" ref="doughnutChart" />
    </div>
</template>
  
<script lang="ts">
import { IonAccordion } from '@ionic/vue'
import { Chart as ChartJS, ArcElement, Tooltip, Legend } from 'chart.js'
import { defineComponent, onMounted, ref } from 'vue'
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
        }
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

        const data = {
            labels: ['Very Happy', 'Happy', 'Neutral', 'Sad', 'Very Sad'],
            datasets: [
                {
                    backgroundColor: ['#41B883', '#A1C349', '#ccffcc', '#F2C94C', '#cc0000'],
                    data: [40, 20, 80, 10, 2]
                }
            ]
        }

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
            data,
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
  