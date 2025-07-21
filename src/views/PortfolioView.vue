<script setup lang="ts">
import { ref } from 'vue'

import TitleComponent from '@/components/TitleComponent.vue'
import PageContent from '@/components/PageContent.vue'
import PortfolioItem from '@/components/PortfolioItem.vue'

import marcelle from '@/assets/marcelle.png'
import aib from '@/assets/aib.png'
import watier from '@/assets/watier.png'
import bentley from '@/assets/bentley.png'
import molsoft from '@/assets/molsoft.png'
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

import marcelleIcon from '@/assets/marcelle.svg'
import aibIcon from '@/assets/aib.svg'
import watierIcon from '@/assets/watier.svg'
import bentleyIcon from '@/assets/bentley.svg'
import molsoftIcon from '@/assets/molsoft.svg'
import lecompteIcon from '@/assets/lecompte.svg'
import parmiIcon from '@/assets/parmi.svg'
import gardeMaladeIcon from '@/assets/garde-malade.svg'
import maisonLavandeIcon from '@/assets/maison-lavande.svg'
import obersonIcon from '@/assets/oberson.svg'
import naakIcon from '@/assets/naak.svg'
import opusIcon from '@/assets/opus.svg'
import uniqueIcon from '@/assets/unique.svg'
import sportsExcellenceIcon from '@/assets/sports-excellence.svg'
import woodstockIcon from '@/assets/woodstock.svg'
import holosIcon from '@/assets/holos.svg'

// <!-- TODO: add description to portfolio items -->
const portfolioItems = ref([
  {
    name: 'Groupe Marcelle',
    site: 'https://marcelle.com/',
    image: marcelle,
    icon: marcelleIcon,
    description: [''],
  },
  {
    name: 'AIB International',
    site: 'https://aibinternational.com/',
    image: aib,
    icon: aibIcon,
    description: [''],
  },
  {
    name: 'Watier',
    site: 'https://watier.com/',
    image: watier,
    icon: watierIcon,
    description: [''],
  },
  {
    name: 'Bentley',
    site: 'https://www.shopbentley.com/',
    image: bentley,
    icon: bentleyIcon,
    description: [''],
  },
  {
    name: 'Molsoft',
    site: 'https://www.molsoft.io/',
    image: molsoft,
    icon: molsoftIcon,
    description: [''],
  },
  {
    name: 'Magasins LeCompte',
    site: 'https://maglecompte.ca/',
    image: lecompte,
    icon: lecompteIcon,
    description: [''],
  },
  {
    name: 'Parmi Lifewear',
    site: 'https://parmilifewear.com/',
    image: parmi,
    icon: parmiIcon,
    description: [''],
  },
  {
    name: 'Garde Malade',
    site: 'https://www.garde-malade.ca/',
    image: gardeMalade,
    icon: gardeMaladeIcon,
    description: [''],
  },
  {
    name: 'La Maison Lavande',
    site: 'https://maisonlavande.ca/',
    image: maisonLavande,
    icon: maisonLavandeIcon,
    description: [''],
  },
  {
    name: 'Oberson',
    site: 'https://oberson.com/',
    image: oberson,
    icon: obersonIcon,
    description: [''],
  },
  {
    name: 'Naak',
    site: 'https://www.naak.com/pages/nutrition-calculator',
    image: naak,
    icon: naakIcon,
    description: [''],
  },
  {
    name: 'Opus Art Supplies',
    site: 'https://opusartsupplies.com/',
    image: opus,
    icon: opusIcon,
    description: [''],
  },
  {
    name: 'Unique Appliances',
    site: 'https://uniqueappliances.com/',
    image: unique,
    icon: uniqueIcon,
    description: [''],
  },
  {
    name: 'Sports Excellence',
    site: 'https://sportsexcellence.com/',
    image: sportsExcellence,
    icon: sportsExcellenceIcon,
    description: [''],
  },
  {
    name: 'Woodstock & cie',
    site: 'https://woodstockcie.com/',
    image: woodstock,
    icon: woodstockIcon,
    description: [''],
  },
  {
    name: 'Holos',
    site: 'https://www.liveholos.com/',
    image: holos,
    icon: holosIcon,
    description: [''],
  },
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
        :icon="item.icon"
        :description="item.description"
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
