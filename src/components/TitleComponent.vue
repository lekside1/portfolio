<script setup lang="ts">
defineProps<{
  title: string
}>()
</script>

<template>
  <h1 class="title">{{ title }}</h1>
</template>

<style scoped>
@media (min-width: 1024px) {
}
</style>
