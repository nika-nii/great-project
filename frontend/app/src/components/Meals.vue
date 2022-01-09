<template>
  <body>
    <my-header></my-header>
    <div class="container-fluid shadow-sm">
      <div class="container">
        <div class="row">
          <nav aria-label="breadcrumb">
            <ol class="breadcrumb mt-3">
              <li class="breadcrumb-item">
                <a href="#" class="link-secondary text-decoration-none"
                  ><font-awesome-icon :icon="['fas', 'home']" />&nbsp;</a
                >
              </li>
              <li class="breadcrumb-item active" aria-current="page">
                Питание
              </li>
            </ol>
          </nav>
        </div>
      </div>
    </div>

    <div class="container">
      <div class="row">
        <p class="fs-2 text-start pt-2">Питание</p>
        <div class="text-start">
          В данном разделе публикуются приёмы пищи детей на каждый день, чтобы
          каждый родитель мог знать, чем питается его ребенок.<br />Также можно
          просмотреть, чем обедал ученик в конкретный день недели (по умолчанию
          выводится сегодняшний обед).
        </div>
        <div class="row pt-2 justify-content-start">
          <div class="col-4">
            <p class="fw-bold">Выберите дату:</p>
            <date-picker
              format="DD.MM.YYYY"
              lang="ru"
              v-model="day"
              valueType="date"
              @pick="fetchData"
            ></date-picker>
          </div>
        </div>

        <div v-if="loading">
          <p> Загрузка </p>
        </div>

        <div v-else-if="error">
          <span class="text-danger">Произошла ошибка!</span>
          <p class="text-warning"> {{ error }} </p>
        </div>

        <div v-else-if="!meal">
          <p>На сегодня нет обедов</p>
        </div>

        <table v-else class="table mt-4">

          <thead>
            <tr>
              <th scope="col">Приём пищи</th>
              <th scope="col">Раздел</th>
              <th scope="col">Блюдо</th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <th rowspan="5">Завтрак</th>
              <td scope="row">Горячее блюдо</td>
              <td>{{meal.breakfast.hot_meal}}</td>
            </tr>
            <tr>
              <td scope="row">Горячий напиток</td>
              <td>{{meal.breakfast.hot_drink}}</td>
            </tr>
            <tr>
              <td scope="row">Фрукт</td>
              <td>{{meal.breakfast.fruit}}</td>
            </tr>
            <tr>
              <td scope="row">Молочный продукт</td>
              <td>{{meal.breakfast.bakery}}</td>
            </tr>
            <tr>
              <td scope="row">Выпечка</td>
              <td>{{meal.breakfast.bakery}}</td>
            </tr>
          </tbody>
          <tbody>
            <tr>
              <th rowspan="2">Полдник</th>
              <td scope="row">Горячий напиток</td>
              <td>{{meal.second_breakfast.hot_drink}}</td>
            </tr>
            <tr>
              <td scope="row">Закуска</td>
              <td>{{meal.second_breakfast.snack}}</td>
            </tr>
          </tbody>
          <tbody>
            <tr>
              <th rowspan="7">Обед</th>
              <td scope="row">Первое блюдо</td>
              <td>{{meal.dinner.hot_meal_first}}</td>
            </tr>
            <tr>
              <td scope="row">Второе блюдо</td>
              <td>{{meal.dinner.hot_meal_second}}</td>
            </tr>
            <tr>
              <td scope="row">Гарнир</td>
              <td>{{meal.dinner.garnish}}</td>
            </tr>
            <tr>
              <td scope="row">Напиток</td>
              <td>{{meal.dinner.drink}}</td>
            </tr>
            <tr>
              <td scope="row">Хлеб белый</td>
              <td>{{meal.dinner.bread_white}}</td>
            </tr>
            <tr>
              <td scope="row">Хлеб черный</td>
              <td>{{meal.dinner.bread_black}}</td>
            </tr>
            <tr>
              <td scope="row">Закуска</td>
              <td>{{meal.dinner.snack}}</td>
            </tr>
          </tbody>
        </table>
      </div>
    </div>
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
import DatePicker from "vue2-datepicker";
import "vue2-datepicker/index.css";

export default {
  name: "Meals",
  props: ["url"],
  components: {
    "my-header": Header,
    "my-footer": Footer,
    "my-org-webs": OrganizationsWebsites,
    DatePicker,
  },
  data() {
    var date = new Date()
    date.setHours(0, 0, 0, 0)
    return {
      day: date,
      meal: null,
      loading: null,
      error: null
    };
  },
  methods: {
    fetchData() {
      fetch(this.url + '/by_date/' + this.day.toISOString(), { //путь к api (обращение к серверу за данными)
            headers: { 'Content-type': 'application/json' },
            }).then(res=>res.json()).then((response) => {
                this.meal = response;
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
};
</script>