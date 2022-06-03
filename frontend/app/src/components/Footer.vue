<template>
<footer class="container py-5">
      <div class="row text-center">
        <div class="col-6 col-md">
          <h5>Ссылки</h5>
          <ul class="list-unstyled text-small">
            <li>
              <a class="link-secondary text-decoration-none" href="https://vk.com/32bel"
                ><font-awesome-icon :icon="['fab', 'vk']" />&nbsp;32bel</a
              >
            </li>
            <li>
              <a
                class="link-secondary text-decoration-none"
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
              <a class="link-secondary text-decoration-none" href="geo:50.611976,36.585040"
                ><font-awesome-icon
                  :icon="['fas', 'map-marker-alt']"
                />&nbsp;308014, г.&nbsp;Белгород, ул.&nbsp;Мичурина,&nbsp;39</a
              >
            </li>
            <li>
              <a class="link-secondary text-decoration-none" href="tel:+74722380819"
                ><font-awesome-icon :icon="['fas', 'phone-alt']" />&nbsp;(4722)
                38-08-19 (приёмная)</a
              >
            </li>
            <li>
              <a class="link-secondary text-decoration-none" href="tel:+74722346463"
                ><font-awesome-icon :icon="['fas', 'phone-alt']" />&nbsp;(4722)
                34-64-63 (вахта)</a
              >
            </li>
            <li>
              <a class="link-secondary text-decoration-none" href="mailto:school32@beluo31.ru"
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
</template>

<script>
   export default{

   }
</script>

<style>
@import "./style.css";
</style>