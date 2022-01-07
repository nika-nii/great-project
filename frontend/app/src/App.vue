<template>
  <div id="app">
    <!-- <Page v-bind:url="baseUrl + '/news'"/> -->
    <Docs v-bind:url="baseUrl + '/docs'"/>
  </div>
</template>

<script>
//import Page from "./components/Page.vue";
import Docs from "./components/Docs.vue";
import { baseUrl } from "./config";

export default {
  name: "App",
  components: {
    //Page,
    Docs
  },
  data() {
    return {
      baseUrl: baseUrl
    }
  },
};
</script>
