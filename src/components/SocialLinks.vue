<script setup lang="ts"></script>

<template>
  <!-- TODO: add icons and links -->
  <div class="social-links">
    <a href="https://twitter.com" target="_blank" rel="noopener noreferrer"
      ><span class="fab fa-twitter">X</span></a
    >
    <a href="https://linkedin.com" target="_blank" rel="noopener noreferrer"
      ><span class="fab fa-linkedin">LinkedIn</span></a
    >
    <a href="https://github.com" target="_blank" rel="noopener noreferrer"
      ><span class="fab fa-github">Github</span></a
    >
    <a href="https://codepen.io" target="_blank" rel="noopener noreferrer"
      ><span class="fab fa-codepen">Codepen</span></a
    >
  </div>
</template>

<style scoped>
.social-links {
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 1rem;
  margin: 1rem 0;
}

.fab {
  display: block;
  /* width: 25px;
  height: 25px; */
  color: var(--color-primary);
}

.fab:hover {
  color: var(--vt-c-green);
}

/* Desktop */
@media (min-width: 1024px) {
}
</style>
