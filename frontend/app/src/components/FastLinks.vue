<template>
<div class="container-fluid bg-light shadow my-4">
      <div class="row align-items-center">
        <div class="my-2 col-sm-6 col-md-4 col-lg-2 col-xl-2 text-center">
          <p><font-awesome-icon :icon="['fas', 'school']" size="5x" /></p>
          <p><router-link to="/about" class="text-dark text-decoration-none">Сведения об ОО</router-link></p>
        </div>
        <div class="my-2 col-sm-6 col-md-4 col-lg-2 col-xl-2 text-center">
          <p><font-awesome-icon :icon="['fas', 'info']" size="5x" /></p>
          <p>О лицее</p>
        </div>
        <div class="my-2 col-sm-6 col-md-4 col-lg-2 col-xl-2 text-center">
          <p><font-awesome-icon :icon="['fas', 'scroll']" size="5x" /></p>
          <p><router-link to="/rules" class="text-dark text-decoration-none">Правила приема</router-link></p>
        </div>
        <div class="my-2 col-sm-6 col-md-4 col-lg-2 col-xl-2 text-center">
          <p><font-awesome-icon :icon="['fas', 'calendar-alt']" size="5x" /></p>
          <p>Календарь мероприятий</p>
        </div>
        <div class="my-2 col-sm-6 col-md-4 col-lg-2 col-xl-2 text-center">
          <p><font-awesome-icon :icon="['fas', 'camera']" size="5x" /></p>
          <p>Дополнительное образование</p>
        </div>
        <div class="my-2 col-sm-6 col-md-4 col-lg-2 col-xl-2 text-center">
          <p><font-awesome-icon :icon="['fas', 'desktop']" size="5x" /></p>
          <p><a href="https://www.vsopen.ru/" class="text-dark text-decoration-none">Виртуальная школа</a></p>
        </div>
      </div>
    </div>
</template>

<script>
   export default{

   }
</script>

<style>

</style>