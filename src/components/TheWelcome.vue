<script setup lang="ts">
defineProps<{
  title?: string
  content?: string
}>()

import SocialLinks from './SocialLinks.vue'
import TypeWriter from './TypeWriter.vue'
</script>

<template>
  <h1 class="title name">{{ title }}</h1>
  <div class="welcome">
    <!-- <TypeWriter msg="Welcome to my portfolio." /> -->
    <TypeWriter msg="Website in progress." />
  </div>

  <SocialLinks />
</template>

<style scoped>
.name {
  font-size: 4rem;
}

.welcome {
  margin: 2rem auto;

  /* Desktop */
  @media (min-width: 1024px) {
    margin: 1rem auto;
  }
}
</style>
