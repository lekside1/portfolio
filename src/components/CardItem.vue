<script setup lang="ts">
defineProps<{
  title: string
  company?: string
  school?: string
  location?: string
  date: string
  description?: string[]
  techStack?: string
}>()
</script>

<template>
  <div class="card-item">
    <h2 class="card-item-title bold green">{{ title }}</h2>

    <div class="card-item-info">
      <span v-if="company" class="card-item-company boldish">{{ company }}</span>
      <span v-else-if="school" class="card-item-school boldish">{{ school }}</span>
      <span v-if="location" class="card-item-location">, {{ location }}</span>

      <p class="card-item-date boldish green small">{{ date }}</p>
    </div>

    <ul v-if="description" class="card-item-description">
      <li v-for="(item, index) in description" :key="index">{{ item }}</li>
    </ul>

    <div v-if="techStack" class="card-item-tech-stack">
      <span class="boldish green">Tech Stack: </span>
      <p class="boldish">{{ techStack }}</p>
    </div>
  </div>
</template>

<style scoped>
.card-item {
  border: 1px solid var(--color-text);
  border-radius: 1rem;
  box-shadow: 4px 4px var(--color-box-shadow);
  padding: 1rem;

  .card-item-description {
    margin-top: 0.5rem;
    ul& {
      padding-left: 1.5rem;
    }
  }

  .card-item-tech-stack {
    margin-top: 1rem;
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
