import MainPage from '@/pages/MainPage.vue'
import LoginPage from '@/pages/LoginPage.vue'

import { createRouter, createWebHistory } from 'vue-router'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  linkActiveClass: "active",
  routes: [
    {
      path: '/',
      component: MainPage,
    },
    {
      path: '/login',
      component: LoginPage,
    },

  ],
})

export default router
