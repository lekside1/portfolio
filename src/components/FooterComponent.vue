<script setup lang="ts"></script>

<template>
  <footer>
    <div class="quote">
      <p>“The only way to do great work is to love what you do.”</p>
      <p>– Steve Jobs</p>
    </div>

    <!-- TODO: add icons and links -->
    <nav class="social-links">
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
    </nav>

    <div class="copy-right">
      <p>&copy; <b>Adelekan Faruq Aliu 2024</b> - All rights reserved</p>
    </div>
  </footer>
</template>

<style scoped>
footer {
  display: flex;
  place-items: center;
  flex-direction: column;
  gap: 1rem;
  background-color: var(--color-background-soft);
  padding: 1rem;
  margin-top: auto;
}

.social-links {
  display: flex;
  gap: 1rem;
}

/* Desktop */
@media (min-width: 1024px) {
  footer {
    padding: 2rem;
  }
}
</style>
