<script setup lang="ts">
import IconsComponent from './IconsComponent.vue'

defineProps<{
  name: string
  site: string
  image?: string
}>()
</script>

<template>
  <div
    class="portfolio-item"
    :style="
      image
        ? {
            backgroundImage: `url(${image})`,
            backgroundSize: 'cover',
            backgroundPosition: 'center',
          }
        : {}
    "
  >
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

<style scoped>
.portfolio-item {
  position: relative;
  border: 1px solid var(--color-text);
  border-radius: 1rem;
  box-shadow: 4px 4px var(--color-box-shadow);
  display: flex;
  place-content: center;
  width: 100%;
  min-width: 300px;
  min-height: 250px;

  .portfolio-item-link {
    width: 100%;
    display: flex;
    align-items: flex-end;
    justify-content: flex-start;
    gap: 0.5rem;
    padding: 1rem;
    color: var(--vt-c-white-soft);
  }

  .portfolio-item-name {
    font-size: 1.3rem;
  }

  /* Mobile */
  @media (max-width: 1023px) {
    min-width: 200px;
  }

  /* Desktop */
  @media (min-width: 1024px) {
    transition: transform 0.3s ease-in-out;

    @media (hover: hover) {
      &:hover {
        transform: scale(1.05);
      }
    }
  }
}
</style>
