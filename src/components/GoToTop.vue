<script setup lang="ts">
import { ref, onMounted, onUnmounted } from 'vue'

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
  <button v-if="showButton" @click="scrollToTop" class="go-to-top">Top</button>
</template>

<style scoped>
.go-to-top {
  position: fixed;
  bottom: 20px;
  right: 20px;
  padding: 10px 20px;
  background-color: var(--vt-c-green);
  color: var(--color-text);
  border: none;
  border-radius: 50%;
  cursor: pointer;
  z-index: 999;
  transition: opacity 0.3s;
  width: 3rem;
  height: 3rem;
  display: grid;
  place-items: center;
  place-content: center;
}

.go-to-top:hover {
  background-color: var(--vt-c-green-90);
}
</style>
