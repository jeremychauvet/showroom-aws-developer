import { createApp } from 'vue'
import App from './App.vue'
import axios from 'axios'

export const HTTP = axios.create(
  {
    baseURL: process.env.BACKEND_URL
  }
)


createApp(App).mount('#app')
