<script setup lang="ts">
defineProps<{
  icon?: string
}>()

const getIconComponent = (icon: string) => {
  switch (icon) {
    case 'home':
      return {
        template:
          '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 32 32" xml:space="preserve"><path fill="none" stroke="currentColor" stroke-width="2" stroke-miterlimit="10" d="M3 17 16 4l13 13"/><path fill="none" stroke="currentColor" stroke-width="2" stroke-miterlimit="10" d="M6 14v13h7V17h6v10h7V14"/></svg>',
      }
    case 'resume':
      return {
        template:
          '<svg viewBox="0 0 256 256" xml:space="preserve" xmlns="http://www.w3.org/2000/svg"><path d="M227.6 58.3 179 9.6c-2.6-2.6-6.1-4-9.8-4H45.1c-11.5 0-20.8 9.3-20.8 20.8v203.3c0 11.5 9.3 20.8 20.8 20.8h165.8c11.5 0 20.8-9.3 20.8-20.8V68c0-3.7-1.4-7.1-4.1-9.7m-6.1 171.3c0 5.8-4.8 10.6-10.6 10.6H45.1c-5.8 0-10.6-4.8-10.6-10.6V26.4c0-5.8 4.8-10.6 10.6-10.6h124.2c1 0 1.9.4 2.6 1.1l48.6 48.6c.7.7 1.1 1.6 1.1 2.6v161.5z"/><path d="M209.2 71.7h-32.9c-5.8 0-10.6-4.8-10.6-10.6v-33c0-2.8-2.3-5.1-5.1-5.1s-5.1 2.3-5.1 5.1V61c0 11.5 9.3 20.8 20.8 20.8h32.9c2.8 0 5.1-2.3 5.1-5.1s-2.3-5-5.1-5M105 143.5c2.2 11.1 12 19.2 23.3 19.2s21.1-8.1 23.3-19.2l2.9-14.9c1-7.1-1.2-14.2-5.9-19.6s-11.5-8.5-18.6-8.5h-3.4c-7.1 0-13.9 3.1-18.6 8.5s-6.8 12.5-5.8 19.9zm10.6-27.8c2.8-3.2 6.7-5 10.9-5h3.4c4.2 0 8.2 1.8 10.9 5 2.8 3.2 4 7.4 3.5 11.2l-2.8 14.7c-1.2 6.3-6.8 10.9-13.3 10.9s-12-4.6-13.3-10.9l-2.8-14.4c-.5-4.2.8-8.4 3.5-11.5m53.2 62-22.9-8.1-17.7 17.7-17.7-17.7-22.9 8.1c-3.5 1.2-6.1 4.2-6.8 7.8l-8.1 38.1h111l-8.1-38.1c-.7-3.5-3.3-6.5-6.8-7.8m-83.5 35.7 5.5-25.8q0-.3.3-.3l16.8-6 20.4 20.4 20.4-20.4 16.8 6c.1.1.3.2.3.3l5.5 25.8z"/></svg>',
      }
    case 'about':
      return {
        template:
          '<svg viewBox="0 0 32 32" xmlns="http://www.w3.org/2000/svg"><path d="M16 16a7 7 0 1 0-7-7 7 7 0 0 0 7 7m0-12a5 5 0 1 1-5 5 5 5 0 0 1 5-5m1 14h-2A11 11 0 0 0 4 29a1 1 0 0 0 1 1h22a1 1 0 0 0 1-1 11 11 0 0 0-11-11M6.06 28A9 9 0 0 1 15 20h2a9 9 0 0 1 8.94 8Z"/></svg>',
      }
    case 'contact':
      return {
        template:
          '<svg viewBox="0 0 15 15" fill="currentColor" xmlns="http://www.w3.org/2000/svg"><path d="M2 12.5v.5h1v-.5zm5 0v.5h1v-.5zm-4 0V12H2v.5zm4-.5v.5h1V12zm-2-2a2 2 0 0 1 2 2h1a3 3 0 0 0-3-3zm-2 2a2 2 0 0 1 2-2V9a3 3 0 0 0-3 3zm2-8a2 2 0 0 0-2 2h1a1 1 0 0 1 1-1zm2 2a2 2 0 0 0-2-2v1a1 1 0 0 1 1 1zM5 8a2 2 0 0 0 2-2H6a1 1 0 0 1-1 1zm0-1a1 1 0 0 1-1-1H3a2 2 0 0 0 2 2zM1.5 3h12V2h-12zm12.5.5v8h1v-8zm-.5 8.5h-12v1h12zM1 11.5v-8H0v8zm.5.5a.5.5 0 0 1-.5-.5H0A1.5 1.5 0 0 0 1.5 13zm12.5-.5a.5.5 0 0 1-.5.5v1a1.5 1.5 0 0 0 1.5-1.5zM13.5 3a.5.5 0 0 1 .5.5h1A1.5 1.5 0 0 0 13.5 2zm-12-1A1.5 1.5 0 0 0 0 3.5h1a.5.5 0 0 1 .5-.5zM9 6h3V5H9zm0 3h3V8H9zm-9 6h15v-1H0zM3 0v2.5h1V0zm8 0v2.5h1V0z" fill="currentColor"/></svg>',
      }
    case 'close':
      return {
        template:
          '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 52 52" xml:space="preserve"><path d="m31 25.4 13-13.1c.6-.6.6-1.5 0-2.1l-2-2.1c-.6-.6-1.5-.6-2.1 0L26.8 21.2c-.4.4-1 .4-1.4 0L12.3 8c-.6-.6-1.5-.6-2.1 0l-2.1 2.1c-.6.6-.6 1.5 0 2.1l13.1 13.1c.4.4.4 1 0 1.4L8 39.9c-.6.6-.6 1.5 0 2.1l2.1 2.1c.6.6 1.5.6 2.1 0L25.3 31c.4-.4 1-.4 1.4 0l13.1 13.1c.6.6 1.5.6 2.1 0L44 42c.6-.6.6-1.5 0-2.1L31 26.8c-.4-.4-.4-1 0-1.4"/></svg>',
      }
    default:
      return {
        template:
          '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 32 32"><path d="M16 0C7.2 0 0 7.2 0 16s7.2 16 16 16 16-7.2 16-16S24.8 0 16 0zm0 30C8 30 2 24 2 16S8 2 16 2s14 6 14 14-6 14-14 14z"/><path d="M22.7 10.3c-.4-.4-1-.4-1.4 0L16 15.6l-5.3-5.3c-.4-.4-1-.4-1.4 0s-.4 1 0 1.4l5.3 5.3-5.3 5.3c-.4.4-.4 1 0 1.4s1 .4 1.4 0l5.3-5.3 5.3 5.3c.4.4 1 .4 1.4 0s.4-1 0-1.4l-5.3-5.3 5.3-5.3c.4-.4.4-1 0-1.4z"/></svg>',
      }
  }
}
</script>
<template>
  <div v-html="getIconComponent(icon ?? '').template" />
</template>

<style scoped>
/* Desktop */
@media (min-width: 1024px) {
}
</style>
