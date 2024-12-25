<script setup lang="ts">
defineProps<{
  title?: string
  content?: string
}>()
</script>

<template>
  <section class="page">
    <h1 class="title">{{ title }}</h1>
    <slot></slot>
  </section>
</template>

<style scoped>
@media (min-width: 1024px) {
  .page {
    color: var(--color-text);
  }
}
</style>
