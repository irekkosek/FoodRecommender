import { createApp } from 'vue'
import { createPinia } from 'pinia'
import PrimeVue from 'primevue/config'
import LottieAnimation from 'lottie-web-vue'

import App from './App.vue'
import router from './router'

import './assets/app.scss'
import 'primevue/resources/themes/lara-light-indigo/theme.css'
import 'primevue/resources/primevue.min.css'
import 'primeicons/primeicons.css'

export const app = createApp(App)

localStorage.userID = 1 // should be stored somewhere else - after site reload there is no access

app.use(createPinia())
app.use(router)
app.use(PrimeVue)

app.mount('#app')
