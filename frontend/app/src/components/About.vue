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
                О лицее
              </li>
            </ol>
          </nav>
        </div>
      </div>
    </div>

    <div class="container">
      <div class="row">
        <p class="fs-2 text-start pt-3">О лицее</p>
        <div class="text-start">
          <h4>Муниципальное бюджетное общеобразовательное учреждение "Лицей №32" г. Белгорода</h4>
          Лицей реализует Федеральные государственные образовательные стандарты на уровне начального общего, основного общего и среднего общего образования.
          <h4 class="pt-2">История лицея</h4>
          Здание лицея построено и открыто в 1972 году.<br>В 1982 году средней школе присвоен статус гимназии, в 2002 году — статус лицея.
          <div class="text-center">
            <img src="../assets/115.jpg" class="img-fluid rounded pt-2 pb-2"  alt="...">
          </div>
          Лицей осуществляет непрерывное образование, включающее:
          <ul>
            <li>начальную школу (1-4 классы);</li>
            <li>пролицейские классы (5-7 классы);</li>
            <li>лицей (8-11 классы):</li>
            <ol>
              <li>математический профиль</li>
              <li>химико-биологический профиль</li>
            </ol>
          </ul>
          <h4 class="">Миссия лицея</h4>
          <ul>
            <li>Активное участие в процессе формирования интеллектуального потенциала страны, становление и развитие высших потребностей личности, гражданского и духовного её возрождения;</li>
            <li>Выявление наиболее способных и одарённых детей, создание условий для развития индивидуальных способностей каждой личности на основе расширения базового компонента, формирования потребностей к саморазвитию и самообразованию;</li>
            <li>Подготовка учащихся к получению высшего образования, творческому труду в различных сферах научной и практической деятельности;</li>
            <li>Реализация идеи общего интеллектуально-нравственного развития личности средствами гуманитаризации среднего образования.</li>
          </ul>
          <h4>Кодекс чести лицеиста:</h4>
          <ul>
            <li>Любить Россию, верить России, помогать России, помнить, что ты — гражданин Белгородчины.</li>
            <li>Учиться знанию, учиться памяти, учиться совести.</li>
            <li>Истина, добро, красота правят миром! Служить этим идеалам дело чести каждого лицеиста.</li>
            <li>Благородство, порядочность, обязательность — главные достоинства лицеиста.</li>
            <li>Любить свой лицей, заботиться о нём, чтить учителя твоего.</li>
            <li>Быть уверенным в себе, никогда не падать духом.</li>
            <li>Стремиться, действовать, добиваться успеха, но только за счёт собственного ума.</li>
            <li>Быть верным братству лицеистов.</li>
            <li>Знай: учёба в лицее — высокая честь! Будь достоин звания лицеиста.</li>
            <li>Точку Архимеда искать в самом себе.</li>
          </ul>
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
  name: "About",
  props: ["url"],
  data() {
    return {
      docs: [],
      loading: null,
      error: null,
    };
  },
  components: {
    "my-header": Header,
    "my-footer": Footer,
    "my-org-webs": OrganizationsWebsites,
  },
  methods: {
    fetchData() {
      fetch(this.url, {
        //путь к api (обращение к серверу за данными)
        headers: { "Content-type": "application/json" },
      })
        .then((res) => res.json())
        .then((response) => {
          this.docs = response;
        })
        .then(() => {
          this.loading = false;
        })
        .catch((error) => {
          this.error = error;
          this.loading = false;
        });
    },
  },
  mounted() {
    // this.loading = true;
    // this.fetchData();
  },
};
</script>    