<script setup lang="ts">
import IconsComponent from './IconsComponent.vue'

defineProps<{
  name: string
  site: string
}>()
</script>

<template>
  <div class="portfolio-item">
    <a
      class="portfolio-item-link"
      :href="site"
      :aria-label="name"
      target="_blank"
      rel="noopener noreferrer"
    >
      <span class="portfolio-item-name bold">{{ name }}</span>
      <IconsComponent icon="external-link" />
    </a>
  </div>
</template>

<!-- TODO: box-shadow colour update to match light/ darkk theme -->
<style scoped>
.portfolio-item {
  border: 1px solid var(--color-text);
  border-radius: 1rem;
  box-shadow: 4px 4px #00000040;
  display: flex;
  place-content: center;

  .portfolio-item-link {
    display: flex;
    align-items: center;
    gap: 0.5rem;
    padding: 1rem;
  }

  .portfolio-item-name {
    font-size: 1.2rem;
  }

  /* Desktop */
  @media (min-width: 1024px) {
  }
}
</style>
