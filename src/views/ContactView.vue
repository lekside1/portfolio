<script setup lang="ts">
import TitleComponent from '@/components/TitleComponent.vue'
import PageContent from '@/components/PageContent.vue'
import IconsComponent from '@/components/IconsComponent.vue'
</script>

<template>
  <PageContent class="contact">
    <TitleComponent title="Contact" />

    <!-- TODO: contact page content, icon svgs -->
    <div class="contact-inner">
      <div class="contact-item">
        <IconsComponent icon="location" />
        <div class="contact-item-text">
          <span>Location:</span>
          <span>Montreal, QC</span>
        </div>
      </div>

      <div class="contact-item">
        <a href="mailto:afaruqaliu@hotmail.com"><IconsComponent icon="email" /></a>
        <div class="contact-item-text">
          <span>Email:</span>
          <span>afaruqaliu@hotmail.com</span>
        </div>
      </div>

      <div class="contact-item">
        <a href="tel:+1438887XXXX"><IconsComponent icon="phone" /></a>
        <div class="contact-item-text">
          <span>Phone:</span>
          <span>+1 438 887 XXXX</span>
        </div>
      </div>
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
    gap: 0.5rem;
  }

  .contact-item-text {
    display: grid;
  }

  @media (min-width: 1024px) {
    .contact-inner {
      flex-direction: row;
    }
  }
}
</style>
