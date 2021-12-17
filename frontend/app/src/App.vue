<template>
  <div id="app">
    <Page v-bind:url="baseUrl + '/news'"/>
  </div>
</template>

<script>
import Page from "./components/Page.vue";
import { baseUrl } from "./config";

export default {
  name: "App",
  components: {
    Page,
  },
  data() {
    return {
      baseUrl: baseUrl
    }
  },
};
</script>
