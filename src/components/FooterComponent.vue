<script setup lang="ts">
import SocialLinks from './SocialLinks.vue'
import GoToTop from './GoToTop.vue'
</script>

<template>
  <footer>
    <div class="quote">
      <p>“The only way to do great work is to love what you do.”</p>
      <p>– Steve Jobs</p>
    </div>

    <SocialLinks />

    <div class="copy-right">
      <p>&copy; <b class="bold">Adelekan Faruq Aliu</b> 2024</p>
    </div>

    <GoToTop />
  </footer>
</template>

<style scoped>
footer {
  position: absolute;
  bottom: 0;
  width: 100%;
  display: flex;
  place-items: center;
  flex-direction: column;
  background-color: var(--color-background-soft);
  padding: 1rem;
  margin-top: auto;
  box-shadow: 0 -1px 3px var(--color-border);
}

/* Desktop */
@media (min-width: 1024px) {
  footer {
    padding: 2rem;
  }
}
</style>
