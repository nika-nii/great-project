<template>
<header>
      <nav
        class="navbar navbar-expand-md navbar-light bg-light"
        aria-label="Навигация"
      >
        <div class="container-fluid">
          <a class="navbar-brand" href="#">МБОУ "Лицей №32"</a>
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
                  <li><a class="dropdown-item" href="#"><router-link to="/docs">Документы</router-link></a></li>
                  <li><a class="dropdown-item" href="localhost:8080/docs">Опция 2</a></li>
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
</template>

<script>
   export default{

   }
</script>

<style>

</style>