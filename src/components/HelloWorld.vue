<script setup lang="ts">
defineProps<{
  msg: string
}>()
</script>

<template>
  <div class="greetings">
    <h2 class="green typewriter">{{ msg }}</h2>
  </div>
</template>

<style scoped>
.greetings {
  text-align: center;
  width: fit-content;
  margin: 0 auto;
}

@keyframes typing {
  0% {
    width: 0;
  }
  100% {
    width: 100%;
  }
}

@keyframes blinking {
  0% {
    border-right-color: transparent;
  }
  50% {
    border-right-color: var(--color-text);
  }
  100% {
    border-right-color: transparent;
  }
}

.typewriter {
  font-size: 2rem;
  overflow: hidden;
  border-right: 0.2rem solid var(--color-text);
  white-space: nowrap;
  animation:
    /* typing 4s steps(40, end) 1s infinite alternate, */
    typing 4s steps(40, end),
    blinking 1s steps(1, end) infinite;
}

@media (min-width: 1024px) {
}
</style>
