<template>
  <body>
    <my-header></my-header>
    <my-carousel></my-carousel>
    <my-fast-links></my-fast-links>
    <my-news v-bind:url="url"></my-news>
    <my-org-webs></my-org-webs>
    <my-footer></my-footer>
  </body>
</template>

<style>
@import "./style.css";
</style>

<script>
import Header from "./Header.vue";
import Footer from "./Footer.vue";
import FastLinks from "./FastLinks.vue";
import Carousel from "./Carousel.vue";
import News from "./News.vue";
import OrganizationsWebsites from "./OrganizationsWebsites.vue";

export default {
  name: 'Page',
  props: ['url'],
  components:{
    'my-header':Header,
    'my-footer':Footer,
    'my-fast-links':FastLinks,
    'my-carousel':Carousel,
    'my-news':News,
    'my-org-webs':OrganizationsWebsites
  }
}
</script>
