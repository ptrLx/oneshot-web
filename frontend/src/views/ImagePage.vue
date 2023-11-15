<template>
    <base-layout :page-title="imageTitle" :hide-back-button=false>

        <ion-img alt="Img" :src="imgSrc" class="fullscreen-image"></ion-img>
        <div :class="{ 'no-overlay': !isExpanded, 'overlay': isExpanded }"></div>
        <div :class="{ 'description': !isExpanded, 'description-expanded': isExpanded }" @click="expandDescription">
            {{ descriptionText }}
        </div>
    </base-layout>
</template>

<script lang="ts">
import { defineComponent, ref } from 'vue';
import { IonCard, IonImg, IonCardSubtitle, IonCardTitle } from '@ionic/vue';
import { useRoute } from 'vue-router'

export default defineComponent({
    components: {
        IonCard,
        IonImg,
        IonCardSubtitle,
        IonCardTitle,
    },
    setup() {
        const route = useRoute()
        const id = route.params.id

        // TODO: Replace with API Call to backend
        const url_base = ref<string>('https://placekitten.com/200/300?image=');
        const imgSrc = ref<string>(url_base.value + id)
        const imageDate = 'YYYY-MM-DD'
        const imageHappiness = '😄'
        const imageTitle = ref<string>(`${imageDate} |  ${imageHappiness}`)
        const descriptionText = ref<string>('Exorcizamus te omnis immundus spiritus omnis satanica potestas, omnis incursio infernalis adversarii, omnis legio, omnis congregatio et secta diabolica. Ergo draco maledicte et omnis legio diabolica adjuramus te. Cessa decipere humanas creaturas, eisque æternæ perditionìs venenum propinare. Vade, satana, inventor et magister omnis fallaciæ, hostis humanæ salutis. Humiliare sub potenti manu Dei; contremisce et effuge, invocato a nobis sancto et terribili nomine, quem inferi tremunt. Ab insidiis diaboli, libera nos, Domine. Ut Ecclesiam tuam secura tibi facias libertate servire, te rogamus, audi nos. Ut inimicos sanctæ Ecclesiæ humiliare digneris, te rogamus, audi nos. Terribilis Deus de sanctuario suo. Deus Israël ipse truderit virtutem et fortitudinem plebi suæ. Benedictus Deus. Gloria Patri. Sicut erat. Terribilis Deus de sanctuario suo. Deus Israël ipse truderit virtutem et fortitudinem plebi suæ. Benedictus Deus. Gloria Patri. Sicut erat. Terribilis Deus de sanctuario suo. Deus Israël ipse truderit virtutem et fortitudinem plebi suæ. Benedictus Deus. Gloria Patri. Sicut erat. Terribilis Deus de sanctuario suo. Deus Israël ipse truderit virtutem et fortitudinem plebi suæ. Benedictus Deus. Gloria Patri. Sicut erat. Terribilis Deus de sanctuario suo. Deus Israël ipse truderit virtutem et fortitudinem plebi suæ. Benedictus Deus. Gloria Patri. Sicut erat. ')
        const isExpanded = ref<boolean>(false)
        const expandDescription = () => {
            isExpanded.value = !isExpanded.value
        }

        return {
            imgSrc,
            imageTitle,
            descriptionText,
            isExpanded,
            expandDescription
        }
    }
});
</script>

<style scoped>
.fullscreen-image {
    width: 100%;
    height: auto;
}

.description {
    position: absolute;
    bottom: 15px;
    left: 3%;
    width: 94%;
    display: -webkit-box;
    -webkit-line-clamp: 2;
    -webkit-box-orient: vertical;
    overflow: hidden;
    text-overflow: ellipsis;
    color: white;
    transition: max-height 0.2s ease-out;
}

.description-expanded {
    position: absolute;
    bottom: 15px;
    left: 3%;
    width: 94%;
    max-height: 85%;
    overflow: auto;
    color: white;
    transition: max-height 0.2s ease-out;
}

.no-overlay {
    /* fill whole screen */
    position: absolute;
    bottom: 0;
    left: 0;
    width: 100%;
    height: 20%;
    background: linear-gradient(to top, rgba(0, 0, 0, 0.8) 10%, transparent);
}

.overlay {
    /* fill whole screen */
    position: absolute;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;

    /* semi-transparent background */
    background-color: rgba(0, 0, 0, 0.5);
    transition: background-color 0.2s ease-out;
}
</style>