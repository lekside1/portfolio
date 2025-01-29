<script setup lang="ts">
import { RouterLink } from 'vue-router'
import { ref } from 'vue'

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

// onMounted(() => {
//   const headerTop = document.querySelector('.header-top') as HTMLElement
//   if (headerTop) {
//     const headerTopHeight = headerTop.offsetHeight
//     document.documentElement.style.setProperty('--header-top-height', `${headerTopHeight}px`)
//   }
// })
</script>

<template>
  <header>
    <div class="header-top">
      <button class="burger-button" @click="toggleDrawer" aria-label="Open navigation drawer">
        <IconsComponent icon="hamburger" width="2rem" height="2rem" />
      </button>

      <!-- <RouterLink to="/" class="logo">
        <img alt="Vue logo" class="logo-img" src="@/assets/logo.svg" width="50" height="50" />
      </RouterLink> -->

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
        <RouterLink class="nav-item" to="/portfolio">
          <IconsComponent icon="portfolio" />Portfolio
        </RouterLink>
      </nav>

      <ThemeSwitcher :showLabel="false" />
    </div>

    <!-- Mobile nav drawer -->
    <div :class="{ drawer: true, 'drawer-open': isDrawerOpen }">
      <button class="close-button" @click="toggleDrawer" aria-label="Close navigation drawer">
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
        <RouterLink class="nav-item" to="/portfolio" @click="toggleDrawer">
          <IconsComponent icon="portfolio" />Portfolio
        </RouterLink>
      </nav>
    </div>
  </header>
</template>

<style scoped>
header {
  position: sticky;
  top: 0;
  z-index: 9999;
  line-height: 1.5;
  max-height: 100vh;
  background-color: var(--color-background-soft);
  box-shadow: 0 1px 3px var(--color-border);

  .header-top {
    display: flex;
    justify-content: space-between;
    align-items: center;
    padding: 0.5rem;
    margin: 0 auto;
    max-width: var(--xlarge-container);
  }

  .logo {
    display: block;
    margin: 0 auto;
    padding: 1rem;
    width: fit-content;
    height: fit-content;
  }

  .desktop-nav {
    display: none;
  }

  .nav-item {
    display: flex;
    align-items: center;
    gap: 1rem;
  }

  nav {
    display: flex;
    text-align: center;
    gap: 1rem;
    width: 100%;
    height: 100%;
    font-size: 1.5rem;
  }

  nav a {
    color: var(--color-text);
  }

  nav a.router-link-exact-active {
    color: var(--vt-c-green);
  }

  /* Mobile drawer */
  .burger-button,
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

  /* Desktop */
  @media (min-width: 1024px) {
    .header-top {
      padding: 1rem 0;
    }

    .desktop-nav {
      transition: all 0.5s;
      width: fit-content;
      display: flex;
      place-content: center;
      gap: calc(var(--section-gap) / 4);
    }

    .logo {
      margin: 0;
      padding: 1rem 2rem;
      position: relative;
      z-index: 9999;
    }

    .nav-item {
      transition:
        transform 0.2s ease-in-out,
        color 0.2s ease-in-out;

      @media (hover: hover) {
        &:hover {
          transform: scale(1.3);
          color: var(--vt-c-green);
        }
      }
    }

    .drawer-open {
      transform: translateX(-100%);
    }
  }

  /* Mobile */
  @media (max-width: 1023px) {
    nav {
      font-size: 2rem;
    }

    button {
      color: var(--vt-c-green);
      background: none;
      border: none;
      cursor: pointer;
    }

    .burger-button {
      display: block;
      padding: 0;
    }

    .close-button {
      display: block;
      position: absolute;
      top: 1rem;
      right: 1rem;
    }
  }

  @media (max-width: 768px) {
    .drawer {
      max-width: 100%;
    }
  }
}
</style>
