<script setup lang="ts">
import { RouterLink } from 'vue-router'

import { ref } from 'vue'

const isDrawerOpen = ref(false)
const toggleDrawer = () => {
  isDrawerOpen.value = !isDrawerOpen.value
}
</script>

<template>
  <header>
    <nav class="desktop-nav">
      <RouterLink to="/">Home</RouterLink>
      <RouterLink to="/portfolio">Portfolio</RouterLink>
      <RouterLink to="/resume">Resume</RouterLink>
      <RouterLink to="/about">About</RouterLink>
      <RouterLink to="/contact">Contact</RouterLink>
    </nav>

    <!-- TODO: use svg icons -->
    <div class="burger-button" @click="toggleDrawer">&#9776;</div>
    <div :class="{ drawer: true, 'drawer-open': isDrawerOpen }">
      <button class="close-button" @click="toggleDrawer">X</button>
      <nav class="drawer-nav">
        <RouterLink to="/" @click="toggleDrawer">Home</RouterLink>
        <RouterLink to="/portfolio" @click="toggleDrawer">Portfolio</RouterLink>
        <RouterLink to="/resume" @click="toggleDrawer">Resume</RouterLink>
        <RouterLink to="/about" @click="toggleDrawer">About</RouterLink>
        <RouterLink to="/contact" @click="toggleDrawer">Contact</RouterLink>
      </nav>
    </div>
  </header>
</template>

<style scoped>
header {
  line-height: 1.5;
  max-height: 100vh;
  width: fit-content;
}

header .desktop-nav {
  display: none;
}

nav {
  display: flex;
  text-align: center;
  gap: 1rem;
  width: 100%;
  height: 100%;
  font-size: 1.5rem;
}

nav a.router-link-exact-active {
  color: var(--color-text);
}

nav a.router-link-exact-active:hover {
  background-color: transparent;
}

nav a {
  display: inline-block;
  padding: 0 1rem;
}

nav a:first-of-type {
  border: 0;
}

/* Mobile nav drawer */
.burger-button {
  display: none;
  font-size: 2rem;
  cursor: pointer;
  padding: 0.5rem 1rem;
}

.drawer {
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  max-width: 400px;
  height: 100%;
  background-color: var(--color-background-soft);
  box-shadow: 1px 0 3px var(--color-border);
  z-index: 9998;
  transform: translateX(-100%);
  transition: transform 0.3s ease;
}

.drawer-nav {
  display: flex;
  justify-content: center;
  flex-direction: column;
  padding: 2rem;
}

.drawer-open {
  transform: translateX(0);
}

/* Desktop nav */
@media (min-width: 1024px) {
  header {
    position: fixed;
    top: 0;
    left: 0;
    bottom: 0;
    z-index: 9997;
    transition: all 0.5s;
    padding: 2rem;
  }

  header .desktop-nav {
    display: flex;
    flex-direction: column;
    place-content: center;
    gap: calc(var(--section-gap) / 3);
  }

  nav {
    text-align: left;
    padding: 1rem 0;
  }
}

/* Mobile nav */
@media (max-width: 1024px) {
  .burger-button {
    display: block;
    position: absolute;
    top: 0;
    left: 0;
  }

  .close-button {
    position: absolute;
    top: 1rem;
    right: 1rem;
    font-size: 2rem;
    cursor: pointer;
  }
}
</style>
