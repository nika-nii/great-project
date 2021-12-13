import Vue from 'vue'
import App from './App.vue'
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
} from '@fortawesome/free-solid-svg-icons'
import {
    FontAwesomeIcon
} from '@fortawesome/vue-fontawesome'

library.add(faVk, faInstagram, faEnvelope, faPhoneAlt, faMapMarkerAlt, faSchool, faInfo, faScroll, faCalendarAlt, faCamera, faDesktop)

Vue.component('font-awesome-icon', FontAwesomeIcon)

Vue.config.productionTip = false

new Vue({
    render: h => h(App),
}).$mount('#app')