<script setup lang="ts">
import IconsComponent from './IconsComponent.vue'

defineProps<{
  name: string
  site: string
  image?: string
  icon?: string
  description?: string[]
}>()
</script>

<template>
  <div
    class="portfolio-item on-hover-transition"
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
      <div v-if="icon" class="portfolio-item-icon">
        <img :src="icon" :alt="`${name} icon`" loading="lazy" />
      </div>

      <div v-if="description && description.length > 0" class="portfolio-item-description">
        <div v-for="(desc, idx) in description" :key="idx" class="boldish">
          {{ desc }}
        </div>
      </div>

      <div class="portfolio-item-text">
        <span class="portfolio-item-name bold">{{ name }}</span>
        <IconsComponent icon="external-link" />
      </div>
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

  .portfolio-item-icon {
    width: 150px;

    img {
      max-height: 50px;
    }
  }

  .portfolio-item-link {
    display: flex;
    flex-direction: column;
    justify-content: space-between;
    gap: 0.5rem;
    width: 100%;
    padding: 1rem;
    color: var(--vt-c-white-soft);
    background-color: var(--background-overlay);
    border-radius: inherit;
  }

  .portfolio-item-description {
    margin: 0.5rem 0;
  }

  .portfolio-item-text {
    display: flex;
    align-items: center;
    gap: 0.2rem;
    width: 100%;
    margin-top: auto;
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
    /* transition: transform 0.3s ease-in-out;

    @media (hover: hover) {
      &:hover {
        transform: scale(1.05);
      }
    } */
  }
}
</style>
