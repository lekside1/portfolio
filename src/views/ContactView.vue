<script setup lang="ts">
import TitleComponent from '@/components/TitleComponent.vue'
import PageContent from '@/components/PageContent.vue'
import IconsComponent from '@/components/IconsComponent.vue'
</script>

<template>
  <PageContent class="contact">
    <TitleComponent title="Contact" />

    <div class="contact-inner">
      <a
        class="contact-item"
        href="https://www.google.com/maps/place/Montreal,+QC"
        target="_blank"
        rel="noopener"
      >
        <IconsComponent icon="location" />
        <div class="contact-item-text">
          <span>Montreal, QC</span>
        </div>
      </a>

      <a class="contact-item" href="mailto:afaruqaliu@hotmail.com">
        <IconsComponent icon="email" />
        <div class="contact-item-text">
          <span>afaruqaliu@hotmail.com</span>
        </div>
      </a>
    </div>
  </PageContent>
</template>

<style scoped>
.contact {
  .contact-inner {
    display: flex;
    flex-direction: column;
    justify-content: space-between;
    gap: 2rem;
    padding: 2rem 0;
  }

  .contact-item {
    display: flex;
    place-items: center;
    flex-direction: column;
    gap: 0.5rem;

    color: var(--color-text);

    a& {
      @media (hover: hover) {
        &:hover {
          color: var(--vt-c-green);
        }
      }
    }
  }

  /* Desktop */
  @media (min-width: 1024px) {
    .contact-inner,
    .contact-item {
      flex-direction: row;
    }
  }
}
</style>
