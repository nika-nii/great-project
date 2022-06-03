<template>
  <body>
    <my-header></my-header>
    <div class="container-fluid shadow-sm">
      <div class="container">
        <div class="row">
          <nav aria-label="breadcrumb">
            <ol class="breadcrumb mt-3">
              <li class="breadcrumb-item">
                <router-link to="/page" class="text-dark text-decoration-none"><font-awesome-icon :icon="['fas', 'home']" />&nbsp;</router-link>
              </li>
              <li class="breadcrumb-item">Новости</li>
              <li class="breadcrumb-item active" aria-current="page">
                {{ post.title }}
              </li>
            </ol>
          </nav>
        </div>
      </div>
    </div>
    <div class="container">
      <div class="row">
        <p class="fs-2 text-start pt-3">{{ post.title }}</p>
        <div class="text-start">
          <p class="text-secondary">{{ post.category }}</p>
        <div
            id="carouselPictures"
            class="carousel slide carousel-my"
            data-bs-ride="carousel"
        >
        <div class="carousel-inner">
            <div class="carousel-item active">
                <img src="../assets/01.jpg" class="d-block w-100" alt="..." />
            </div>
            <div class="carousel-item">
                <img src="../assets/02.jpg" class="d-block w-100" alt="..." />
            </div>
            <div class="carousel-item">
                <img src="../assets/03.jpg" class="d-block w-100" alt="..." />
            </div>
        </div>
      <button
        class="carousel-control-prev"
        type="button"
        data-bs-target="#carouselPictures"
        data-bs-slide="prev"
      >
        <span class="carousel-control-prev-icon" aria-hidden="true"></span>
        <span class="visually-hidden">Назад</span>
      </button>
      <button
        class="carousel-control-next"
        type="button"
        data-bs-target="#carouselPictures"
        data-bs-slide="next"
      >
        <span class="carousel-control-next-icon" aria-hidden="true"></span>
        <span class="visually-hidden">Вперед</span>
      </button>
        </div>
        <p class="pt-2">{{ post.text }}</p>
        </div>
    </div>
    </div>
    <div class="mine-footer">
      <my-org-webs></my-org-webs>
      <my-footer></my-footer>
    </div>
  </body>
</template>

<style>
@import "./style.css";
</style>

<script>
import Header from "./Header.vue";
import Footer from "./Footer.vue";
import OrganizationsWebsites from "./OrganizationsWebsites.vue";
//import moment from 'moment';

export default {
    name: 'Post',
    props: ['url'],
    components: {
    "my-header": Header,
    "my-footer": Footer,
    "my-org-webs": OrganizationsWebsites
    },
    data() {
        return {
            post: {},
            loading: null,
            error: null,
        }
    },
    methods: {
        fetchData() {
            fetch(this.url, { //путь к api (обращение к серверу за данными)
                headers: { 'Content-type': 'application/json' },
                }).then(res=>res.json()).then((response) => {
                    this.post = response;
                }).then(() => {
                    this.loading = false
                }).catch( (error) => {
                    this.error = error;
                    this.loading = false;
                });
        }
    },
  mounted() {
    this.loading = true
    this.fetchData();
  }
}
</script>    