import { createRouter, createWebHistory } from '@ionic/vue-router';
import { RouteRecordRaw } from 'vue-router';
import HomePage from '../views/HomePage.vue'
import { useCookies } from 'vue3-cookies'
import { UserService } from '@/_generated/api-client';

const routes: Array<RouteRecordRaw> = [
  {
    path: '/',
    redirect: '/home'
  },
  {
    path: '/home',
    name: 'Home',
    component: HomePage,
    meta: { requiresAuth: true }
  },
  {
    path: '/profile',
    name: 'Profile',
    component: () => import('../views/ProfilePage.vue'), // Lazy load component
    meta: { requiresAuth: true}
  },
  {
    path: '/login',
    name: 'Login',
    component: () => import('../views/LoginPage.vue'), // Lazy load component
    meta: { requiresAuth: false}
  }
]

const {cookies} = useCookies();

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes
})


router.beforeEach((to, from) =>{
  
    if(to.meta.requiresAuth && !cookies.get('token')){
      return  { 
        path: '/login', 
        query: { redirect: to.fullPath } 
      }
    }
})

export default router
