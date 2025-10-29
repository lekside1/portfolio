<script setup lang="ts">
import SocialLinks from './SocialLinks.vue'
import GoToTop from './GoToTop.vue'
</script>

<template>
  <footer>
    <!-- <div class="quote">
      <p>"The best way to predict the future is to create it." - Abraham Lincoln</p>
    </div> -->

    <SocialLinks />

    <div class="copy-right">
      <p>&copy; <b class="bold">Adelekan Faruq Aliu</b> 2024-2025</p>
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
