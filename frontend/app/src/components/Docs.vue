<template>
  <body>
    <my-header></my-header>
    <nav aria-label="breadcrumb">
        <ol class="breadcrumb">
            <li class="breadcrumb-item"><a href="#"><font-awesome-icon :icon="['fas', 'fa-home']" />&nbsp;</a></li>
            <li class="breadcrumb-item active" aria-current="page">Library</li>
        </ol>
    </nav>
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
import OrganizationsWebsites from "./OrganizationsWebsites.vue";

export default {
  name: 'Docs',
  props: ['url'],
  components:{
    'my-header':Header,
    'my-footer':Footer,
    'my-org-webs':OrganizationsWebsites
  }
}
</script>
