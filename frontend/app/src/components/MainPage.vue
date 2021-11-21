<template>
  <body>
    <header>
      <div class="navbar navbar-expand-xl align-items-center">It's a navbar, hooray!</div>
    </header>

    <div
      id="carouselExampleCaptions"
      class="carousel slide carousel-my"
      data-bs-ride="carousel"
    >
      <div class="carousel-indicators">
        <button
          type="button"
          data-bs-target="#carouselExampleCaptions"
          data-bs-slide-to="0"
          class="active"
          aria-current="true"
          aria-label="Slide 1"
        ></button>
        <button
          type="button"
          data-bs-target="#carouselExampleCaptions"
          data-bs-slide-to="1"
          aria-label="Slide 2"
        ></button>
        <button
          type="button"
          data-bs-target="#carouselExampleCaptions"
          data-bs-slide-to="2"
          aria-label="Slide 3"
        ></button>
      </div>
      <div class="carousel-inner">
        <div class="carousel-item active">
          <img src="../assets/1.jpg" class="d-block w-100" alt="..." />
          <div class="carousel-caption d-none d-md-block">
            <h5>Добро пожаловать</h5>
            <p>Это главная страница сайта</p>
          </div>
        </div>
        <div class="carousel-item">
          <img src="../assets/2.jpg" class="d-block w-100" alt="..." />
          <div class="carousel-caption d-none d-md-block">
            <h5>Самые свежие новости</h5>
            <p>Обновляются регулярно</p>
          </div>
        </div>
        <div class="carousel-item">
          <img src="../assets/3.jpg" class="d-block w-100" alt="..." />
          <div class="carousel-caption d-none d-md-block">
            <h5>Документы и прочее</h5>
            <p>Удобство и доступность</p>
          </div>
        </div>
      </div>
      <button
        class="carousel-control-prev"
        type="button"
        data-bs-target="#carouselExampleCaptions"
        data-bs-slide="prev"
      >
        <span class="carousel-control-prev-icon" aria-hidden="true"></span>
        <span class="visually-hidden">Previous</span>
      </button>
      <button
        class="carousel-control-next"
        type="button"
        data-bs-target="#carouselExampleCaptions"
        data-bs-slide="next"
      >
        <span class="carousel-control-next-icon" aria-hidden="true"></span>
        <span class="visually-hidden">Next</span>
      </button>
    </div>

    <div class="container-fluid bg-light my-4">
      <div class="row align-items-center">
        <div class="my-2 col-sm-6 col-md-4 col-lg-2 col-xl-2 text-center">
          <img src="../assets/home_icon.png" class="menu-icon-size" alt="..." />
          Сведения об оо
        </div>
        <div class="my-2 col-sm-6 col-md-4 col-lg-2 col-xl-2 text-center">
          <img src="../assets/edit_icon.png" class="menu-icon-size" alt="..." />
          О лицее
        </div>
        <div class="my-2 col-sm-6 col-md-4 col-lg-2 col-xl-2 text-center">
          <img src="../assets/shopping_icon.png" class="menu-icon-size" alt="..." />
          Условия приёма
        </div>
        <div class="my-2 col-sm-6 col-md-4 col-lg-2 col-xl-2 text-center">
          <img src="../assets/calendar-icon.png" class="menu-icon-size" alt="..." />
          Календарь
        </div>
        <div class="my-2 col-sm-6 col-md-4 col-lg-2 col-xl-2 text-center">
          <img src="../assets/camera_icon.png" class="menu-icon-size" alt="..." />
          Видео
        </div>
        <div class="my-2 col-sm-6 col-md-4 col-lg-2 col-xl-2 text-center">
          <img src="../assets/network_icon.png" class="menu-icon-size" alt="..." />
          Виртуальная школа
        </div>
      </div>
    </div>

    <div id="app" class="container">
      <div class="row justify-items-center">
        <p class="fs-2 text-decoration-underline text-start">Новости</p>
      </div>
      <div class="row">
        <div class="col-12 col-lg-6" v-for="post in posts" v-bind:key="post.title">
          <div class="card card-resize my-3">
            <div class="card-body">
              <h5 class="card-title">{{ post.title }}</h5>
              <h6 class="card-subtitle mb-2 text-muted">{{ post.category }}</h6>
              <p class="card-text">{{ post.text }}</p>
              <a href="#" class="card-link">Продолжить чтение</a>
            </div>
          </div>
        </div>
      </div>
    </div>
    <div class="container my-4">
      <div id="carouselExampleIndicators" class="carousel slide" data-ride="carousel">
        <ol class="carousel-indicators">
          <li
            data-target="#carouselExampleIndicators"
            data-slide-to="0"
            class="active"
          ></li>
          <li data-target="#carouselExampleIndicators" data-slide-to="1"></li>
          <li data-target="#carouselExampleIndicators" data-slide-to="2"></li>
        </ol>
        <div class="carousel-inner">
          <div class="carousel-item active m-4">
            <a class="btn btn-light" href="#" role="button"
              ><img
                src="../assets/gosuslugi_icon.png"
                class="menu-icon-size"
                alt="..."
              />Госуслуги</a
            >
            <a class="btn btn-light" href="#" role="button"
              ><img
                src="../assets/ol_icon.png"
                class="menu-icon-size"
                alt="..."
              />Всероссийская олимпиада школьников</a
            >
            <a class="btn btn-light" href="#" role="button"
              ><img
                src="../assets/ch_icon.png"
                class="menu-icon-size"
                alt="..."
              />Персональные данные.Дети</a
            >
          </div>
          <div class="carousel-item">
            <a class="btn btn-light" href="#" role="button"> Кнопка с иконкой</a>
          </div>
          <div class="carousel-item">
            <a class="btn btn-light" href="#" role="button"> Кнопка с иконкой</a>
          </div>
        </div>
        <a
          class="carousel-control-prev"
          href="#carouselExampleIndicators"
          role="button"
          data-slide="prev"
        >
          <span class="carousel-control-prev-icon" aria-hidden="true"></span>
          <span class="sr-only"></span>
        </a>
        <a
          class="carousel-control-next"
          href="#carouselExampleIndicators"
          role="button"
          data-slide="next"
        >
          <span class="carousel-control-next-icon" aria-hidden="true"></span>
          <span class="sr-only"></span>
        </a>
      </div>
    </div>

    <footer>
      <div class="row text-center">
        <div class="col-lg-4 col-md-4 col-sm-12 mb-4">
          <h5 class="text-uppercase">Социальные сети</h5>
          <ul class="list-unstyled icon-resize">
            <li>
              <!-- VK -->
              <a href="https://vk.com/32bel"
                ><img src="../assets/vk-round-color.svg" alt=""
              /></a>
            </li>
            <!-- Instagram -->
            <li>
              <a href="https://www.instagram.com/lyceum32belgorod/"
                ><img src="../assets/ig-instagram.svg" alt=""
              /></a>
            </li>
          </ul>
        </div>

        <div class="col-lg-4 col-md-4 col-sm-12 mb-4">
          <h5 class="text-uppercase">Links</h5>
          <ul class="list-unstyled mb-0">
            <li>
              <a href="#!" class="text-dark">Link 1</a>
            </li>
            <li>
              <a href="#!" class="text-dark">Link 2</a>
            </li>
            <li>
              <a href="#!" class="text-dark">Link 3</a>
            </li>
            <li>
              <a href="#!" class="text-dark">Link 4</a>
            </li>
          </ul>
        </div>

        <div class="col-lg-4 col-md-4 col-sm-12 mb-4">
          <h5 class="text-uppercase">Контактная информация</h5>
          <ul class="list-unstyled mb-0">
            <li>
              <p class="text-dark"><b>Адрес:</b> 308014, г. Белгород, ул. Мичурина, 39</p>
            </li>
            <li>
              <p class="text-dark">
                <b>Телефоны:</b> (4722) 38-08-19 (приёмная), (4722) 34-64-63 (вахта)
              </p>
            </li>
            <li>
              <p class="text-dark"><b>E-mail:</b> school32@beluo31.ru</p>
            </li>
            <li>
              <a href="#!" class="text-dark"> <link />Обратная связь </a>
            </li>
          </ul>
        </div>

        <div class="text-center p-3" style="background-color: rgba(0, 0, 0, 0.2)">
          Copyright © 2021, МБОУ "Лицей №32", г. Белгорода
        </div>
      </div>
    </footer>
  </body>
</template>

<style>
@import "./style.css";
</style>

<script>
import axios from "axios";
export default {
  name: "MainPage",
  data() {
    return {
      posts: [
        {
          title: "День учителя в 2021",
          category: "Школьные будни",
          text:
            "День учителя — один из самых известных, любимых и широко отмечаемых профессиональных праздников. Поэтому весь лицей готовился к нему, одни готовили праздничный концерт для учителей, другие занимались распределением ролей на День дублера, третьи - украшением здания.",
        },
        {
          title: 'Межрегиональная олимпиада по праву "Фемида"',
          category: "Объявления",
          text:
            "День учителя — один из самых известных, любимых и широко отмечаемых профессиональных праздников. Поэтому весь лицей готовился к нему, одни готовили праздничный концерт для учителей, другие занимались распределением ролей на День дублера, третьи - украшением здания.",
        },
      ],
    };
  },
  mounted() {
    axios.get("http://127.0.0.1:8000/news/").then((response) => {
      this.posts = response.data;
      console.log(response.data);
    });
  },
};
</script>
