<script setup lang="ts">
defineProps<{
  icon?: string
  width?: string
  height?: string
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
    case 'x':
      return {
        template:
          '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24"><path d="M24 4.6c-.9.4-1.8.7-2.8.8 1-.6 1.7-1.5 2-2.6-.9.5-1.9.9-3 1.1-.9-.9-2.1-1.5-3.4-1.5-2.6 0-4.7 2.1-4.7 4.7 0 .4 0 .8.1 1.2-3.9-.2-7.3-2.1-9.6-5-.4.7-.6 1.5-.6 2.3 0 1.6.8 3 2.1 3.8-.8 0-1.5-.2-2.1-.6v.1c0 2.3 1.6 4.2 3.7 4.6-.4.1-.8.2-1.2.2-.3 0-.6 0-.8-.1.6 1.9 2.4 3.3 4.5 3.3-1.6 1.2-3.6 1.9-5.7 1.9-.4 0-.8 0-1.1-.1 2 1.3 4.4 2.1 7 2.1 8.4 0 13-7 13-13v-.6c.9-.7 1.7-1.5 2.3-2.4z"/></svg>',
      }
    case 'linkedin':
      return {
        template:
          '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24"><path d="M19 0h-14c-2.8 0-5 2.2-5 5v14c0 2.8 2.2 5 5 5h14c2.8 0 5-2.2 5-5v-14c0-2.8-2.2-5-5-5zm-11 19h-3v-10h3v10zm-1.5-11.3c-1 0-1.7-.8-1.7-1.7s.8-1.7 1.7-1.7 1.7.8 1.7 1.7-.8 1.7-1.7 1.7zm13.5 11.3h-3v-5.5c0-1.3-.5-2.2-1.7-2.2-.9 0-1.4.6-1.7 1.2-.1.2-.1.5-.1.8v5.7h-3v-10h3v1.3c.4-.6 1.1-1.3 2.7-1.3 2 0 3.5 1.3 3.5 4.1v5.9z"/></svg>',
      }
    case 'github':
      return {
        template:
          '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24"><path d="M12 .3c-6.6 0-12 5.4-12 12 0 5.3 3.4 9.8 8.2 11.4.6.1.8-.3.8-.6v-2.2c-3.3.7-4-1.6-4-1.6-.5-1.3-1.2-1.6-1.2-1.6-1-.7.1-.7.1-.7 1.1.1 1.7 1.1 1.7 1.1 1 .1.7 1.6.7 1.6-.8.1-1.6-.8-1.6-.8-.5-1.3-.1-1.6-.1-1.6 1.1-.1 2.2 1.1 2.2 1.1.9 1.6 2.6 1.1 3.3.8.1-.7.4-1.1.7-1.4-2.6-.3-5.3-1.3-5.3-5.8 0-1.3.5-2.4 1.2-3.3-.1-.3-.5-1.6.1-3.3 0 0 1-.3 3.3 1.2.9-.3 1.8-.5 2.7-.5s1.8.2 2.7.5c2.3-1.5 3.3-1.2 3.3-1.2.6 1.7.2 3 .1 3.3.7.9 1.2 2 1.2 3.3 0 4.5-2.7 5.5-5.3 5.8.4.3.8 1 .8 2v3c0 .3.2.7.8.6 4.8-1.6 8.2-6.1 8.2-11.4 0-6.6-5.4-12-12-12z"/></svg>',
      }
    case 'codepen':
      return {
        template:
          '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24"><path d="M12 0c-6.6 0-12 5.4-12 12s5.4 12 12 12 12-5.4 12-12-5.4-12-12-12zm6.7 8.3l-2.7 1.8v-3.6l2.7 1.8zm-6.7-4.3l2.7 1.8-2.7 1.8-2.7-1.8 2.7-1.8zm-6.7 4.3l2.7-1.8v3.6l-2.7-1.8zm0 7.4l2.7-1.8v3.6l-2.7-1.8zm6.7 4.3l-2.7-1.8 2.7-1.8 2.7 1.8-2.7 1.8zm6.7-4.3l-2.7 1.8v-3.6l2.7 1.8zm-3.6-2.5l-3.1-2.1-3.1 2.1v-4.2l3.1 2.1 3.1-2.1v4.2z"/></svg>',
      }
    case 'hamburger':
      return {
        template:
          '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24"><path d="M3 6h18v2H3zm0 5h18v2H3zm0 5h18v2H3z"/></svg>',
      }
    case 'arrow-up':
      return {
        template:
          '<svg viewBox="0 0 20 20" xmlns="http://www.w3.org/2000/svg"><path d="M11 17V5.414l3.293 3.293a.999.999 0 1 0 1.414-1.414l-5-5a1 1 0 0 0-1.414 0l-5 5a.997.997 0 0 0 0 1.414 1 1 0 0 0 1.414 0L9 5.414V17a1 1 0 1 0 2 0" fill="currentColor"/></svg>',
      }
    default:
      return {
        template:
          '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24"><path d="M12 2C6.5 2 2 6.5 2 12s4.5 10 10 10 10-4.5 10-10S17.5 2 12 2zm0 18c-4.4 0-8-3.6-8-8s3.6-8 8-8 8 3.6 8 8-3.6 8-8 8zm-1-13h2v6h-2zm0 8h2v2h-2z"/></svg>',
      }
  }
}
</script>
<template>
  <div
    :style="{ '--svg-width': width, '--svg-height': height }"
    v-html="getIconComponent(icon ?? '').template"
  />
</template>

<style scoped>
/* Desktop */
@media (min-width: 1024px) {
}
</style>

<!-- AFA
<svg width="800" height="800" viewBox="0 0 32 32" xmlns="http://www.w3.org/2000/svg"><path d="m28.34 26.854-10.527-22.4a.8.8 0 0 0-.724-.46h-1.088a.8.8 0 0 0-.721.455l-.002.005-10.529 22.4a.8.8 0 0 0 .722 1.14h.993a.8.8 0 0 0 .723-.456l.002-.005 2.44-5.203H23.43l2.471 5.207a.8.8 0 0 0 .723.457h.992a.8.8 0 0 0 .722-1.145zm-17.542-7.053 5.744-12.17 5.718 12.17z"/></svg><svg width="800" height="800" viewBox="0 0 32 32" xmlns="http://www.w3.org/2000/svg"><path d="M24.863 3.993H10.4a.8.8 0 0 0-.8.8v22.4c0 .442.358.8.8.801h.928a.8.8 0 0 0 .8-.801v-8.959H23.68a.803.803 0 0 0 .801-.801v-.929a.8.8 0 0 0-.801-.8H12.128V6.52h12.735c.442 0 .8-.358.801-.8v-.929a.8.8 0 0 0-.801-.8z"/></svg><svg width="800" height="800" viewBox="0 0 32 32" xmlns="http://www.w3.org/2000/svg"><path d="m28.34 26.854-10.527-22.4a.8.8 0 0 0-.724-.46h-1.088a.8.8 0 0 0-.721.455l-.002.005-10.529 22.4a.8.8 0 0 0 .722 1.14h.993a.8.8 0 0 0 .723-.456l.002-.005 2.44-5.203H23.43l2.471 5.207a.8.8 0 0 0 .723.457h.992a.8.8 0 0 0 .722-1.145zm-17.542-7.053 5.744-12.17 5.718 12.17z"/></svg> -->
