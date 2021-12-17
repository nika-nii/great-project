<template>
  <div id="app">
    <Page url="http://localhost:8000/api/items"/>
  </div>
</template>

<script>
import Page from "./components/Page.vue";

export default {
  name: "App",
  components: {
    Page,
  },
};
</script>
