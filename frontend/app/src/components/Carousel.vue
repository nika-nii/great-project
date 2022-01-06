<template>
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
</template>

<script>
   export default{

   }
</script>

<style>

</style>