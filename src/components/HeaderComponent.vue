<script setup lang="ts">
import { RouterLink } from 'vue-router'
import { ref, onMounted } from 'vue'

import ThemeSwitcher from './ThemeSwitcher.vue'
import IconsComponent from './IconsComponent.vue'

const isDrawerOpen = ref(false)
const toggleDrawer = () => {
  isDrawerOpen.value = !isDrawerOpen.value
  if (isDrawerOpen.value) {
    document.body.style.overflow = 'hidden'
  } else {
    document.body.style.overflow = 'auto'
  }
}

onMounted(() => {
  const headerTop = document.querySelector('.header-top') as HTMLElement
  if (headerTop) {
    const headerTopHeight = headerTop.offsetHeight
    document.documentElement.style.setProperty('--header-top-height', `${headerTopHeight}px`)
  }
})
</script>

<template>
  <header>
    <div class="header-top">
      <div class="burger-button" @click="toggleDrawer">&#9776;</div>

      <RouterLink to="/" class="logo">
        <img alt="Vue logo" class="logo-img" src="@/assets/logo.svg" width="50" height="50" />
      </RouterLink>

      <ThemeSwitcher :showLabel="false" />
    </div>

    <!-- Desktop nav -->
    <nav class="desktop-nav">
      <RouterLink class="nav-item" to="/"><IconsComponent icon="home" />Home</RouterLink>
      <RouterLink class="nav-item" to="/resume">
        <IconsComponent icon="resume" />Resume
      </RouterLink>
      <RouterLink class="nav-item" to="/about"><IconsComponent icon="about" />About</RouterLink>
      <RouterLink class="nav-item" to="/contact">
        <IconsComponent icon="contact" />Contact
      </RouterLink>
    </nav>

    <!-- Mobile nav drawer -->
    <div :class="{ drawer: true, 'drawer-open': isDrawerOpen }">
      <button class="close-button" @click="toggleDrawer">
        <IconsComponent icon="close" />
      </button>

      <nav class="drawer-nav">
        <RouterLink class="nav-item" to="/" @click="toggleDrawer">
          <IconsComponent icon="home" />Home
        </RouterLink>
        <RouterLink class="nav-item" to="/resume" @click="toggleDrawer">
          <IconsComponent icon="resume" />Resume
        </RouterLink>
        <RouterLink class="nav-item" to="/about" @click="toggleDrawer">
          <IconsComponent icon="about" />About
        </RouterLink>
        <RouterLink class="nav-item" to="/contact" @click="toggleDrawer">
          <IconsComponent icon="contact" />Contact
        </RouterLink>
      </nav>
    </div>
  </header>
</template>

<style scoped>
header {
  line-height: 1.5;
  max-height: 100vh;
  position: sticky;
  top: 0;
  z-index: 9999;
}

.header-top {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 0.5rem 1rem;
  background-color: var(--color-background-soft);
  box-shadow: 0 1px 3px var(--color-border);
}

header .desktop-nav {
  display: none;
}

.nav-item {
  display: flex;
  align-items: center;
  gap: 0.5rem;
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

nav a:first-of-type {
  border: 0;
}

/* Mobile nav drawer */
.burger-button {
  display: none;
  font-size: 2rem;
  cursor: pointer;
}

.close-button {
  display: none;
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
  header .desktop-nav {
    position: fixed;
    top: var(--header-top-height);
    left: 0;
    bottom: 0;
    z-index: 9997;
    transition: all 0.5s;
    padding: 2rem;
    width: fit-content;
    display: flex;
    flex-direction: column;
    place-content: center;
    gap: calc(var(--section-gap) / 4);
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
  }

  .close-button {
    display: block;
    position: absolute;
    top: 1rem;
    right: 1rem;
    font-size: 2rem;
    background: none;
    border: none;
    cursor: pointer;
    color: var(--color-text);
  }
}
</style>
