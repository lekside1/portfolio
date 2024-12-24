<script setup lang="ts">
defineProps<{
  title?: string
  content?: string
}>()

import SocialLinks from './SocialLinks.vue'
import HelloWorld from './HelloWorld.vue'
</script>

<template>
  <h1 class="title">{{ title }}</h1>
  <HelloWorld msg="Welcome to my portfolio. Website in progress." />
  <SocialLinks />
</template>
