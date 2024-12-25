<script setup lang="ts">
import { ref, onMounted, onUnmounted } from 'vue'

import IconsComponent from './IconsComponent.vue'

const showButton = ref(false)

const handleScroll = () => {
  showButton.value = window.scrollY > 200
}

const scrollToTop = () => {
  window.scrollTo({ top: 0, behavior: 'smooth' })
}

onMounted(() => {
  window.addEventListener('scroll', handleScroll)
})

onUnmounted(() => {
  window.removeEventListener('scroll', handleScroll)
})
</script>

<template>
  <!-- TODO: use svg icon, update colors -->
  <button v-if="showButton" @click="scrollToTop" class="go-to-top">
    <IconsComponent icon="arrow-up" />
  </button>
</template>

<style scoped>
.go-to-top {
  position: fixed;
  bottom: 20px;
  right: 20px;
  padding: 1rem;
  background-color: var(--vt-c-green);
  color: var(--color-background-mute);
  border: none;
  border-radius: 50%;
  cursor: pointer;
  z-index: 999;
  transition:
    color 0.2s ease-in-out,
    background-color 0.2s ease-in-out;
  width: 3rem;
  height: 3rem;
  display: grid;
  place-items: center;
  place-content: center;

  @media (hover: hover) {
    &:hover {
      background-color: var(--color-border);
      color: var(--vt-c-green);
    }
  }
}
</style>
