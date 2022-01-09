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
              format="DD/MM/YYYY"
              lang="ru"
              v-model="time1"
              valueType="format"
            ></date-picker>
          </div>
        </div>

        <table class="table mt-4">
          <!-- <thead>
            <tr>
              <th scope="col">Прием пищи</th>
              <th scope="col">Раздел</th>
              <th scope="col">Блюдо</th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <th scope="row">Завтрак</th>
              <td>Mark</td>
              <td>Otto</td>
            </tr>
            <tr>
              <th scope="row">Полдник</th>
              <td>Jacob</td>
              <td>Thornton</td>
            </tr>
            <tr>
              <th scope="row">Обед</th>
              <td>Jacob</td>
              <td>Thornton</td>
            </tr>
          </tbody> -->

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
              <td>A2</td>
            </tr>
            <tr>
              <td scope="row">Горячий напиток</td>
              <td>A1</td>
            </tr>
            <tr>
              <td scope="row">Фрукт</td>
              <td>A3</td>
            </tr>
            <tr>
              <td scope="row">Молочный продукт</td>
              <td>A3</td>
            </tr>
            <tr>
              <td scope="row">Выпечка</td>
              <td>A3</td>
            </tr>
          </tbody>
          <tbody>
            <tr>
              <th rowspan="2">Полдник</th>
              <td scope="row">Горячий напиток</td>
              <td>A1</td>
            </tr>
            <tr>
              <td scope="row">Закуска</td>
              <td>A2</td>
            </tr>
          </tbody>
          <tbody>
            <tr>
              <th rowspan="7">Обед</th>
              <td scope="row">Первое блюдо</td>
              <td>A1</td>
            </tr>
            <tr>
              <td scope="row">Второе блюдо</td>
              <td>A2</td>
            </tr>
            <tr>
              <td scope="row">Гарнир</td>
              <td>A2</td>
            </tr>
            <tr>
              <td scope="row">Напиток</td>
              <td>A2</td>
            </tr>
            <tr>
              <td scope="row">Хлеб белый</td>
              <td>A2</td>
            </tr>
            <tr>
              <td scope="row">Хлеб черный</td>
              <td>A2</td>
            </tr>
            <tr>
              <td scope="row">Закуска</td>
              <td>A2</td>
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
    return {
      time1: null,
      time2: null,
      time3: null,
    };
  },
};
</script>