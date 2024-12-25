<script setup lang="ts">
import IconsComponent from './IconsComponent.vue'
</script>

<template>
  <!-- TODO: add icons and links -->
  <div class="social-links">
    <a class="icon" href="https://x.com/lefarside" target="_blank" rel="noopener noreferrer">
      <IconsComponent icon="x" />
    </a>
    <a
      class="icon"
      href="https://linkedin.com/in/faruqaliu/"
      target="_blank"
      rel="noopener noreferrer"
    >
      <IconsComponent icon="linkedin" />
    </a>
    <a class="icon" href="https://github.com/lekside1" target="_blank" rel="noopener noreferrer">
      <IconsComponent icon="github" />
    </a>
    <a class="icon" href="https://codepen.io/lekside1" target="_blank" rel="noopener noreferrer">
      <IconsComponent icon="codepen" />
    </a>
  </div>
</template>

<style scoped>
.social-links {
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 1rem;
  margin: 1rem 0;

  /* Desktop */
  @media (min-width: 1024px) {
    a.icon {
      color: var(--color-text);

      @media (hover: hover) {
        &:hover {
          color: var(--vt-c-green);
        }
      }
    }
  }
}
</style>
