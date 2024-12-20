<script setup lang="ts">
import { RouterLink, RouterView } from 'vue-router'

import ThemeSwitcher from './components/ThemeSwitcher.vue'
import GoToTop from './components/GoToTop.vue'
import HeaderComponent from './components/HeaderComponent.vue'
import FooterComponent from './components/FooterComponent.vue'
</script>

<template>
  <RouterLink to="/" class="logo">
    <img alt="Vue logo" class="logo-img" src="@/assets/logo.svg" width="80" height="80" />
  </RouterLink>

  <ThemeSwitcher :showLabel="false" />
  <GoToTop />

  <HeaderComponent />

  <RouterView />

  <FooterComponent />
</template>

<style scoped>
.logo {
  display: block;
  margin: 0 auto;
  padding: 1rem;
  width: fit-content;
  height: fit-content;
}

/* Desktop */
@media (min-width: 1024px) {
  .logo {
    margin: 0;
    padding: 1rem 2rem;
    position: relative;
    z-index: 9999;
  }
}
</style>
