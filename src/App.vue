<script setup lang="ts">
import { RouterView } from 'vue-router'

import HeaderComponent from './components/HeaderComponent.vue'
import FooterComponent from './components/FooterComponent.vue'

import { onMounted, ref } from 'vue'

const footerHeight = ref(0)

onMounted(() => {
  const footerElement = document.querySelector('footer')
  if (footerElement) {
    footerHeight.value = footerElement.offsetHeight + 20
  }
})
</script>

<template>
  <div :style="{ paddingBottom: footerHeight + 'px' }">
    <HeaderComponent />
    <RouterView />
    <FooterComponent />
  </div>
</template>

<style scoped>
/* Desktop */
@media (min-width: 1024px) {
}
</style>
