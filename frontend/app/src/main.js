import Vue from 'vue'
import VueRouter from 'vue-router'
import App from './App.vue'
//import Meals from './components/Meals.vue'
import Docs from './components/Docs.vue'
import "bootstrap/dist/css/bootstrap.min.css"
import "bootstrap"
import {
    library
} from '@fortawesome/fontawesome-svg-core'
import {
    faVk,
    faInstagram
} from '@fortawesome/free-brands-svg-icons'
import {
    faEnvelope,
    faMapMarkerAlt,
    faPhoneAlt,
    faSchool,
    faInfo,
    faScroll,
    faCalendarAlt,
    faCamera,
    faDesktop,
    faHome
} from '@fortawesome/free-solid-svg-icons'
import {
    FontAwesomeIcon
} from '@fortawesome/vue-fontawesome'

library.add(faVk, faInstagram, faEnvelope, faPhoneAlt, faMapMarkerAlt, faSchool, faInfo, faScroll, faCalendarAlt, faCamera, faDesktop, faHome)

Vue.component('font-awesome-icon', FontAwesomeIcon)

Vue.use(VueRouter)

Vue.config.productionTip = false

const router = new VueRouter({
    routes: [
        //{ path: '/meals', component: Meals},
        { path: '/docs', omponent: Docs}
    ]
})

new Vue({
    render: h => h(App),
    router
}).$mount('#app')