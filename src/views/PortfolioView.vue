<script setup lang="ts">
import { ref } from 'vue'

import TitleComponent from '@/components/TitleComponent.vue'
import PageContent from '@/components/PageContent.vue'
import PortfolioItem from '@/components/PortfolioItem.vue'

import marcelle from '@/assets/marcelle.png'
import aib from '@/assets/aib.png'
import watier from '@/assets/watier.png'
import bentley from '@/assets/bentley.png'
import molsoft from '@/assets/bentley.png'
import lecompte from '@/assets/lecompte.png'
import parmi from '@/assets/parmi.png'
import gardeMalade from '@/assets/garde-malade.png'
import maisonLavande from '@/assets/maison-lavande.png'
import oberson from '@/assets/oberson.png'
import naak from '@/assets/naak.png'
import opus from '@/assets/opus.png'
import unique from '@/assets/unique.png'
import sportsExcellence from '@/assets/sports-excellence.png'
import woodstock from '@/assets/woodstock.png'
import holos from '@/assets/holos.png'

// <!-- TODO: update portfolio item  -->
const portfolioItems = ref([
  { name: 'Groupe Marcelle', site: 'https://marcelle.com/', image: marcelle },
  { name: 'AIB International', site: 'https://aibinternational.com/', image: aib },
  { name: 'Watier', site: 'https://watier.com/', image: watier },
  { name: 'Bentley', site: 'https://www.shopbentley.com/', image: bentley },
  { name: 'Molsoft', site: 'https://www.molsoft.io/', image: molsoft },
  { name: 'Magasins LeCompte', site: 'https://maglecompte.ca/', image: lecompte },
  { name: 'Parmi Lifewear', site: 'https://parmilifewear.com/', image: parmi },
  { name: 'Garde Malade', site: 'https://www.garde-malade.ca/', image: gardeMalade },
  { name: 'La Maison Lavande', site: 'https://maisonlavande.ca/', image: maisonLavande },
  { name: 'Oberson', site: 'https://oberson.com/', image: oberson },
  { name: 'Naak', site: 'https://www.naak.com/pages/nutrition-calculator', image: naak },
  { name: 'Opus Art Supplies', site: 'https://opusartsupplies.com/', image: opus },
  { name: 'Unique Appliances', site: 'https://uniqueappliances.com/', image: unique },
  { name: 'Sports Excellence', site: 'https://sportsexcellence.com/', image: sportsExcellence },
  { name: 'Woodstock & cie', site: 'https://woodstockcie.com/', image: woodstock },
  { name: 'Holos', site: 'https://www.liveholos.com/', image: holos },
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
        :image="item.image"
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
