<script setup lang="ts">
import { ref } from 'vue'

import TitleComponent from '@/components/TitleComponent.vue'
import PageContent from '@/components/PageContent.vue'
import PortfolioItem from '@/components/PortfolioItem.vue'

// <!-- TODO: add portfolio item page content -->
const portfolioItems = ref([
  { name: 'Molsoft', site: 'https://www.molsoft.io/' },
  { name: 'Opus Art Supplies', site: 'https://opusartsupplies.com/' },
  { name: 'Magasin LeCompte', site: 'https://maglecompte.ca/' },
  { name: 'Oberson', site: 'https://oberson.com/' },
  { name: 'Woodstock & cie', site: 'https://woodstockcie.com/' },
  { name: 'Holos', site: 'https://www.liveholos.com/' },
  { name: 'Unique Appliances', site: 'https://uniqueappliances.com/' },
  { name: 'AIB International', site: 'https://aibinternational.com/' },
])
</script>

<template>
  <PageContent class="portfolio">
    <TitleComponent title="Portfolio" />

    <div class="portfolio-inner">
      <PortfolioItem
        v-for="item in portfolioItems"
        :key="item.name"
        :site="item.site"
        :name="item.name"
      />
    </div>
  </PageContent>
</template>

<style scoped>
.portfolio {
  .portfolio-inner {
    width: 100%;
    display: grid;
    grid-template-columns: repeat(2, 1fr);
    gap: 1.5rem;
    padding: 2rem;
  }

  /* Small Mobile */
  @media (max-width: 480px) {
    .portfolio-inner {
      grid-template-columns: 1fr;
    }
  }

  /* Desktop */
  @media (min-width: 1024px) {
    .portfolio-inner {
      grid-template-columns: repeat(3, 1fr);
    }
  }
}
</style>
