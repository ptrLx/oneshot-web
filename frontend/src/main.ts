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
import { isPlatform } from '@ionic/vue';
import { createHead } from '@vueuse/head'
import { defineCustomElements } from '@ionic/pwa-elements/loader';

defineCustomElements(window);


globalCookiesConfig({
  expireTimes: "180DAYS", // define token expiration time
  //secure: true // true: only https works
});

// Set base URL for backend API calls
const nodeEnv = process.env.NODE_ENV;
if (nodeEnv === 'development') {
  // development
  OpenAPI.BASE = 'http://localhost:8200';
  console.log('Running oneshot-web in development mode');
}
else {
  // production
  OpenAPI.BASE = 'http://localhost:8080/api';
  console.log('Running oneshot-web in production mode');
}

const app = createApp(App)
  .use(IonicVue)
  .use(router)
  .use(createHead());


// make base layout component known to all components
app.component('base-layout', BaseLayout);


router.isReady().then(() => {
  app.mount('#app');
});

// --- Accessibility ---
// Set viewport scalability dependiong on the platform
if (isPlatform('desktop')) {
  const viewport = document.querySelector('meta[name=viewport]');

  if (viewport) {
    viewport.setAttribute('content', 'minimum-scale=1, maximum-scale=5, initial-scale=1, user-scalable=yes, viewport-fit=cover, width=device-width');
  }
}


