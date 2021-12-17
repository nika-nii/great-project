<template>
  <body>
    <header>
      <nav
        class="navbar navbar-expand-md navbar-light bg-light"
        aria-label="Навигация"
      >
        <div class="container-fluid">
          <a class="navbar-brand" href="#">Лицей 32</a>
          <button
            class="navbar-toggler"
            type="button"
            data-bs-toggle="collapse"
            data-bs-target="#navbarsExample04"
            aria-controls="navbarsExample04"
            aria-expanded="false"
            aria-label="Раскрыть навигатор"
          >
            <span class="navbar-toggler-icon"></span>
          </button>

          <div class="collapse navbar-collapse" id="navbarsExample04">
            <ul class="navbar-nav me-auto mb-2 mb-md-0">
              <li class="nav-item">
                <a class="nav-link active" aria-current="page" href="#"
                  >Главная</a
                >
              </li>
              <li class="nav-item">
                <a class="nav-link" href="#">Новости</a>
              </li>
              <li class="nav-item">
                <a
                  class="nav-link disabled"
                  href="#"
                  tabindex="-1"
                  aria-disabled="true"
                  >Пока не сделано</a
                >
              </li>
              <li class="nav-item dropdown">
                <a
                  class="nav-link dropdown-toggle"
                  href="#"
                  id="dropdown04"
                  data-bs-toggle="dropdown"
                  aria-expanded="false"
                  >Меню</a
                >
                <ul class="dropdown-menu" aria-labelledby="dropdown04">
                  <li><a class="dropdown-item" href="#">Опция 1</a></li>
                  <li><a class="dropdown-item" href="#">Опция 2</a></li>
                  <li><a class="dropdown-item" href="#">Опция 3</a></li>
                </ul>
              </li>
            </ul>
            <form>
              <input
                class="form-control"
                type="text"
                placeholder="Поиск"
                aria-label="Поиск"
              />
            </form>
          </div>
        </div>
      </nav>
    </header>

    <!-- Карусель -->

    <div
      id="carouselPictures"
      class="carousel slide carousel-my"
      data-bs-ride="carousel"
    >
      <div class="carousel-indicators">
        <button
          type="button"
          data-bs-target="#carouselPictures"
          data-bs-slide-to="0"
          class="active"
          aria-current="true"
          aria-label="Слайд 1"
        ></button>
        <button
          type="button"
          data-bs-target="#carouselPictures"
          data-bs-slide-to="1"
          aria-label="Слайд 2"
        ></button>
        <button
          type="button"
          data-bs-target="#carouselPictures"
          data-bs-slide-to="2"
          aria-label="Слайд 3"
        ></button>
      </div>
      <div class="carousel-inner">
        <div class="carousel-item active">
          <img src="../assets/01.jpg" class="d-block w-100" alt="..." />
          <div class="carousel-caption d-none d-md-block">
            <h5>Добро пожаловать</h5>
            <p>Это главная страница сайта</p>
          </div>
        </div>
        <div class="carousel-item">
          <img src="../assets/02.jpg" class="d-block w-100" alt="..." />
          <div class="carousel-caption d-none d-md-block">
            <h5>Самые свежие новости</h5>
            <p>Обновляются регулярно</p>
          </div>
        </div>
        <div class="carousel-item">
          <img src="../assets/03.jpg" class="d-block w-100" alt="..." />
          <div class="carousel-caption d-none d-md-block">
            <h5>Документы и прочее</h5>
            <p>Удобство и доступность</p>
          </div>
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

    <!-- Быстрые ссылки -->

    <div class="container-fluid bg-light shadow my-4">
      <div class="row align-items-center">
        <div class="my-2 col-sm-6 col-md-4 col-lg-2 col-xl-2 text-center">
          <p><font-awesome-icon :icon="['fas', 'school']" size="5x" /></p>
          <p>Сведения об ОО</p>
        </div>
        <div class="my-2 col-sm-6 col-md-4 col-lg-2 col-xl-2 text-center">
          <p><font-awesome-icon :icon="['fas', 'info']" size="5x" /></p>
          <p>О лицее</p>
        </div>
        <div class="my-2 col-sm-6 col-md-4 col-lg-2 col-xl-2 text-center">
          <p><font-awesome-icon :icon="['fas', 'scroll']" size="5x" /></p>
          <p>Условия приема</p>
        </div>
        <div class="my-2 col-sm-6 col-md-4 col-lg-2 col-xl-2 text-center">
          <p><font-awesome-icon :icon="['fas', 'calendar-alt']" size="5x" /></p>
          <p>Календарь</p>
        </div>
        <div class="my-2 col-sm-6 col-md-4 col-lg-2 col-xl-2 text-center">
          <p><font-awesome-icon :icon="['fas', 'camera']" size="5x" /></p>
          <p>Видео</p>
        </div>
        <div class="my-2 col-sm-6 col-md-4 col-lg-2 col-xl-2 text-center">
          <p><font-awesome-icon :icon="['fas', 'desktop']" size="5x" /></p>
          <p>Виртуальная школа</p>
        </div>
      </div>
    </div>

    <!-- Блок новостей -->

    <div class="container">
      <div class="row justify-items-center">
        <p class="fs-2 text-decoration-underline text-start">Новости</p>
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
              <a href="#" class="card-link">Продолжить чтение</a>
            </div>
          </div>
        </div>
      </div>
    </div>

    <!-- Ссылки снизу -->

    <div class="container-fluid bg-light shadow my-4">
      <div class="row align-items-center text-center small-text">
        <div class="col">
          <a class="btn btn-light" href="#" role="button">
            <img
              src="../assets/gosuslugi_icon.png"
              class="menu-icon-size"
              alt="..."
            />
            <p>Госуслуги</p>
          </a>
        </div>
        <div class="col">
          <a class="btn btn-light" href="#" role="button">
            <img src="../assets/ol_icon.png" class="menu-icon-size" alt="..." />
            <p>Всероссийская олимпиада школьников</p>
          </a>
        </div>
        <div class="col">
          <a class="btn btn-light" href="#" role="button">
            <img src="../assets/ch_icon.png" class="menu-icon-size" alt="..." />
            <p>Персональные данные.Дети</p>
          </a>
        </div>
      </div>
    </div>

    <footer class="container py-5">
      <div class="row text-center">
        <div class="col-6 col-md">
          <h5>Ссылки</h5>
          <ul class="list-unstyled text-small">
            <li>
              <a class="link-secondary" href="https://vk.com/32bel"
                ><font-awesome-icon :icon="['fab', 'vk']" />&nbsp;32bel</a
              >
            </li>
            <li>
              <a
                class="link-secondary"
                href="https://www.instagram.com/lyceum32belgorod/"
                ><font-awesome-icon
                  :icon="['fab', 'instagram']"
                />&nbsp;lyceum32belgorod</a
              >
            </li>
          </ul>
        </div>
        <div class="col-6 col-md">
          <h5>Контакты</h5>
          <ul class="list-unstyled text-small">
            <li>
              <a class="link-secondary" href="geo:50.611976,36.585040"
                ><font-awesome-icon
                  :icon="['fas', 'map-marker-alt']"
                />&nbsp;308014, г.&nbsp;Белгород, ул.&nbsp;Мичурина,&nbsp;39</a
              >
            </li>
            <li>
              <a class="link-secondary" href="tel:+74722380819"
                ><font-awesome-icon :icon="['fas', 'phone-alt']" />&nbsp;(4722)
                38-08-19 (приёмная)</a
              >
            </li>
            <li>
              <a class="link-secondary" href="tel:+74722346463"
                ><font-awesome-icon :icon="['fas', 'phone-alt']" />&nbsp;(4722)
                34-64-63 (вахта)</a
              >
            </li>
            <li>
              <a class="link-secondary" href="mailto:school32@beluo31.ru"
                ><font-awesome-icon
                  :icon="['fas', 'envelope']"
                />&nbsp;school32@beluo31.ru</a
              >
            </li>
          </ul>
        </div>
      </div>
      <div class="row text-center">
        <div class="col-12 col-md">
          <small class="d-block mb-3 text-muted"
            >&copy; 2021, МБОУ "Лицей №32" г.&nbsp;Белгорода</small
          >
        </div>
      </div>
    </footer>
  </body>
</template>

<style>
@import "./style.css";
</style>

<script>


export default {
  name: 'Page',
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
      fetch(this.url, {
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
