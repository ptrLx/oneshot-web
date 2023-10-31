import { createApp } from 'vue'
import App from './App.vue'
import router from './router';

import { IonicVue } from '@ionic/vue';

/* Core CSS required for Ionic components to work properly */
import '@ionic/vue/css/core.css';

/* Basic CSS for apps built with Ionic */
import '@ionic/vue/css/normalize.css';
import '@ionic/vue/css/structure.css';
import '@ionic/vue/css/typography.css';

/* Optional CSS utils that can be commented out */
import '@ionic/vue/css/padding.css';
import '@ionic/vue/css/float-elements.css';
import '@ionic/vue/css/text-alignment.css';
import '@ionic/vue/css/text-transformation.css';
import '@ionic/vue/css/flex-utils.css';
import '@ionic/vue/css/display.css';

/* Theme variables */
import './theme/variables.css';

/* Other imports */
import BaseLayout from './components/base/BaseLayout.vue';
import { globalCookiesConfig } from 'vue3-cookies'; 
import { OpenAPI } from '@/_generated/api-client';

globalCookiesConfig({
  expireTimes:"180DAYS", // define token expiration time
  //secure: true // true: only https works
});

// set base path for generated client
OpenAPI.BASE = 'http://localhost:8200';


const app = createApp(App)
  .use(IonicVue)
  .use(router)


app.component('base-layout', BaseLayout);
  
router.isReady().then(() => {
  app.mount('#app');
});