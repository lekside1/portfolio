<script setup lang="ts">
defineProps<{
  showLabel?: boolean
}>()

import { ref, onMounted, watch } from 'vue'

// slider checkbox for light/dark mode
const isDarkMode = ref(false)
if (window.matchMedia && window.matchMedia('(prefers-color-scheme: dark)').matches) {
  isDarkMode.value = true
} else if (window.matchMedia && window.matchMedia('(prefers-color-scheme: light)').matches) {
  isDarkMode.value = false
}

const toggleTheme = () => {
  isDarkMode.value = !isDarkMode.value
  document.documentElement.setAttribute('data-theme', isDarkMode.value ? 'dark' : 'light')
}

onMounted(() => {
  const savedTheme = localStorage.getItem('theme')
  if (savedTheme) {
    isDarkMode.value = savedTheme === 'dark'
    document.documentElement.setAttribute('data-theme', savedTheme)
  }
})

watch(isDarkMode, (newValue) => {
  localStorage.setItem('theme', newValue ? 'dark' : 'light')
})
</script>

<template>
  <div class="switcher">
    <span v-if="showLabel" class="switcher-label">{{
      isDarkMode ? 'Toggle light mode' : 'Toggle dark mode'
    }}</span>

    <label class="switch">
      <input type="checkbox" @change="toggleTheme" :checked="isDarkMode" />
      <span class="slider"></span>
    </label>
  </div>
</template>

<style scoped>
.switcher {
  position: absolute;
  top: 0;
  right: 0;
  display: flex;
  padding: 1rem;
  place-content: center;
  place-items: center;
  gap: 1rem;
  --width-of-switch: 3.5rem;
  --height-of-switch: 2rem;
  --size-of-icon: 1.4rem;
  --slider-offset: 0.3rem;
}

.switcher-label {
  font-size: inherit;
  font-weight: 600;
}

.switch {
  display: block;
  position: relative;
  width: var(--width-of-switch);
  height: var(--height-of-switch);
}

.switch input {
  opacity: 0;
  width: 0;
  height: 0;
}

.slider {
  position: absolute;
  cursor: pointer;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  background-color: var(--color-border);
  transition: 0.4s;
  border-radius: 30px;
}

.slider:before {
  position: absolute;
  content: '';
  height: var(--size-of-icon, 1.4rem);
  width: var(--size-of-icon, 1.4rem);
  border-radius: 20px;
  left: var(--slider-offset, 0.3rem);
  top: 50%;
  transform: translateY(-50%);
  background: linear-gradient(40deg, var(--sunrise-1), var(--sunrise-2) 70%);
  transition: 0.4s;
}

input:checked + .slider {
  background-color: var(--dark-grey-background);
}

input:checked + .slider::before {
  left: calc(100% - (var(--size-of-icon, 1.4rem) + var(--slider-offset, 0.3rem)));
  background: var(--dark-grey-background);
  box-shadow:
    inset -3px -2px 3px -2px var(--moon-1),
    inset -10px -4px 0 0 var(--moon-2);
}

/* Mobile */
@media (max-width: 1024px) {
  .switcher {
    gap: 0.5rem;
    flex-direction: column;
    place-items: flex-end;
  }
}
</style>
