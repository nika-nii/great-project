<template>
    <div class="container">
      <div class="row justify-items-center">
        <p class="fs-2 text-center text-uppercase">Новости</p>
      </div>
      <div class="row">
        <div v-if="loading">
          Загрузка...
        </div>
        <div v-else-if="error">
          <span class="text-danger">Произошла ошибка!</span>
          <p class="text-warning"> {{ error }} </p>
        </div>
        <div
          class="col-12 col-lg-6"
          v-else
          v-for="item in news"
          v-bind:key="item.id"
        >
          <div class="card card-resize my-3">
            <div class="card-body">
              <h5 class="card-title">{{ item.title }}</h5>
              <h6 class="card-subtitle mb-2 text-muted">{{ item.category }}</h6>
              <p class="card-text">{{ item.text }}</p>
              <a href="#" class="card-link"><router-link to="/news/post" class="text-decoration-none">Продолжить чтение</router-link></a>
            </div>
          </div>
        </div>
      </div>
    </div>
</template>

<script>
export default {
    name: 'News',
    props: ['url'],
    data() {
        return {
            news: [],
            loading: null,
            error: null,
        }
    },
    methods: {
        fetchData() {
            fetch(this.url, { //путь к api (обращение к серверу за данными)
                headers: { 'Content-type': 'application/json' },
                }).then(res=>res.json()).then((response) => {
                    this.news = response;
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

<style>
    @import "./style.css";
</style>