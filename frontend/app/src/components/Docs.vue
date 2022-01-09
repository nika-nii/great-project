<template>
  <body>
    <my-header></my-header>
    <div class="container-fluid shadow-sm">
      <div class="container">
        <div class="row">
          <nav aria-label="breadcrumb">
            <ol class="breadcrumb mt-3">
              <li class="breadcrumb-item">
                <a href="#" class="link-secondary text-decoration-none"><font-awesome-icon :icon="['fas', 'home']" />&nbsp;Домой</a>
              </li>
              <li class="breadcrumb-item active" aria-current="page">
                Документы
              </li>
            </ol>
          </nav>
        </div>
      </div>
    </div>

    <div class="container">
      <!-- документы -->
      <div class="row">
        <p class="fs-2 text-start">Документы</p>
        <div class="text-start">В данном разделе публикуются такие документы, регламентирующие работу образовательного учреждения, как:</div>
        <ul>
          <li>
            устав ОУ; лицензия на осуществление образовательной деятельности (с приложениями); свидетельство о государственной аккредитации (с приложениями); предписания органов, осуществляющих государственный контроль
          </li>
          <li>
            локальные нормативные акты, предусмотренные частью 2 статьи 30 Федерального закона «Об образовании в Российской Федерации», правила внутреннего распорядка обучающихся, правила внутреннего трудового распорядка и коллективного договора; документ о порядке оказания платных образовательных услуг, в том числе образец договора об оказании платных образовательных услуг, документ об утверждении стоимости обучения по каждой образовательной программе
          </li>
        </ul>
        <div class="col-12 mb-4">
          <div class="border-bottom border-top my-hover">
            <div class="row m-2 align-items-center pt-2">
              <div class="col-2 text-center icon-resize d-none d-md-block">
                <img src="../assets/clock_icon.png" alt="..." />
              </div>
              <div class="col-10">
                <p>
                  Приказ Департамента образования Белгородской области "О
                  переоформлении свидетельства о государственной аккредитации"
                </p>
                <div class="row">
                  <div class="col-4">
                    <a href="#" class="link-secondary">Открыть</a>
                  </div>
                  <div class="col-4">
                    <a href="#" class="link-secondary">Скачать</a>
                  </div>
                  <div class="col-4">
                    <p>Дата: 26.06.2021</p>
                  </div>
                </div>
              </div>
            </div>
          </div>
          <div class="border-bottom border-top my-hover">
            <div class="row m-2 align-items-center pt-2">
              <div class="col-2 text-center icon-resize d-none d-md-block">
                <img src="../assets/clock_icon.png" alt="..." />
              </div>
              <div class="col-10">
                <p>
                  Приказ Департамента образования Белгородской области "О
                  переоформлении свидетельства о государственной аккредитации"
                </p>
                <div class="row">
                  <div class="col-4">
                    <a href="#" class="link-secondary">Открыть</a>
                  </div>
                  <div class="col-4">
                    <a href="#" class="link-secondary">Скачать</a>
                  </div>
                  <div class="col-4">
                    <p>Дата: 21.07.2016</p>
                  </div>
                </div>
              </div>
            </div>
          </div>
          <div class="border-bottom border-top my-hover">
            <div class="row m-2 align-items-center pt-2">
              <div class="col-2 text-center icon-resize d-none d-md-block">
                <img src="../assets/clock_icon.png" alt="..." />
              </div>
              <div class="col-10">
                <p>
                  Приказ Департамента образования Белгородской области "О
                  переоформлении свидетельства о государственной аккредитации"
                </p>
                <div class="row">
                  <div class="col-4">
                    <a href="#" class="link-secondary">Открыть</a>
                  </div>
                  <div class="col-4">
                    <a href="#" class="link-secondary">Скачать</a>
                  </div>
                  <div class="col-4">
                    <p>Дата: 01.09.2009</p>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>
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

export default {
  name: "Docs",
  props: ["url"],
  components: {
    "my-header": Header,
    "my-footer": Footer,
    "my-org-webs": OrganizationsWebsites,
  },
};
</script>
