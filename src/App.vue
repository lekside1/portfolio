<script setup lang="ts">
import { RouterView } from 'vue-router'

import HeaderComponent from './components/HeaderComponent.vue'
import FooterComponent from './components/FooterComponent.vue'
</script>

<template>
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
