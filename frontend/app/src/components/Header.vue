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
                <router-link to="/" class="nav-link active" aria-current="page">
                  Главная</router-link>
              </li>
              <li class="nav-item">
                <a class="nav-link" href="#">Новости</a>
              </li>
              <li class="nav-item">
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
                  <li><router-link class="dropdown-item" to="/docs">Документы</router-link></li>
                  <li><router-link class="dropdown-item" to="/meals">Питание</router-link></li>
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