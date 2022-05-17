import Vue from 'vue'
import VueRouter from 'vue-router'
import App from './App.vue'
import Page from './components/Page.vue'
import Meals from './components/Meals.vue'
import Docs from './components/Docs.vue'
import About from './components/About.vue'
import Rules from './components/Rules.vue'
import Post from './components/Post.vue'
import "bootstrap/dist/css/bootstrap.min.css"
import "bootstrap"
import 'vue2-datepicker/locale/ru';

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
    faHome,
    faFilePdf
} from '@fortawesome/free-solid-svg-icons'

import {
    FontAwesomeIcon
} from '@fortawesome/vue-fontawesome'

import {
    baseUrl
} from "./config";

library.add(faVk, faInstagram, faEnvelope, faPhoneAlt, faMapMarkerAlt, faSchool, faInfo, faScroll, faCalendarAlt, faCamera, faDesktop, faHome, faFilePdf)

Vue.component('font-awesome-icon', FontAwesomeIcon)

Vue.use(VueRouter)

Vue.config.productionTip = false

const router = new VueRouter({
    routes: [
        {
            path: '/',
            component: Page,
            props: {
                url: baseUrl + '/news'
            }
        },
        {
            path: '/docs',
            component: Docs,
            props: {
                url: baseUrl + '/docs/'
            }
        },
        {
            path: '/meals',
            component: Meals,
            props: {
                url: baseUrl + '/meals'
            }
        },
        {
            path: '*',
            component: Page,
            props: {
                url: baseUrl + '/news'
            }
        },
        {
            path: '/about',
            component: About,
            props: {
                url: baseUrl + '/about'
            }
        },
        {
            path: '/rules',
            component: Rules,
            props: {
                url: baseUrl + '/rules'
            }
        },
        {
            path: '/news/:id',
            component: Post,
            props: route => ({
                url: baseUrl + '/news/' + route.params.id
            })
        }
    ]
})

new Vue({
    render: h => h(App),
    router
}).$mount('#app')