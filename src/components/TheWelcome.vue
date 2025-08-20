<script setup lang="ts">
defineProps<{
  title?: string
  content?: string
}>()

import { RouterLink } from 'vue-router'

import SocialLinks from './SocialLinks.vue'
import TypeWriter from './TypeWriter.vue'
import IconsComponent from './IconsComponent.vue'
</script>

<template>
  <h1 class="title name">{{ title }}</h1>
  <div class="welcome">
    <TypeWriter msg="● Software Developer ●" />
  </div>

  <div class="welcome-links">
    <SocialLinks />
    <RouterLink class="icon" to="/resume"> <IconsComponent icon="resume" /></RouterLink>
  </div>
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

.welcome-links {
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 0.5rem 1.5rem;

  .icon {
    color: var(--color-text);

    @media (hover: hover) {
      &:hover {
        color: var(--vt-c-green);
      }
    }
  }
}
</style>
