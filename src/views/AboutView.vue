<script setup lang="ts">
import TitleComponent from '@/components/TitleComponent.vue'
import PageContent from '@/components/PageContent.vue'

import pipboy from '@/assets/pip-boy.jpg'
</script>

<template>
  <PageContent class="about">
    <TitleComponent title="About" />

    <!-- TODO: About page content -->
    <div class="about-inner">
      <div v-if="pipboy" class="image">
        <img alt="pip vault boy" class="about-img" :src="pipboy" width="400" height="500" />
      </div>

      <div class="about-content about-content--card-item">
        <ul>
          <li><span class="bold">Name:</span> Adelekan Faruq Aliu</li>
          <li><span class="bold">City:</span> Montreal, Quebec.</li>
          <li><span class="bold">Languages:</span> English, French, Yoruba</li>
          <li>
            <span class="bold">Interests:</span> Science and Technology, Video Games, Fine Arts,
            Music, Languages, Traveling
          </li>
        </ul>
      </div>
    </div>
  </PageContent>
</template>

<style scoped>
.about {
  .about-inner {
    display: flex;
    flex-direction: column;
    align-items: center;
    gap: 1rem;
  }

  .image {
    display: block;

    .about-img {
      border-radius: 1rem;
      box-shadow: 4px 4px var(--color-box-shadow);
    }
  }

  .about-content {
    padding: 1rem;

    li {
      margin-bottom: 1rem;
    }

    &.about-content--card-item {
      display: flex;
      place-items: center;
      height: 100%;
      border: 1px solid var(--color-text);
      border-radius: 1rem;
      box-shadow: 4px 4px var(--color-box-shadow);

      /* Desktop */
      @media (min-width: 1024px) {
        transition: transform 0.3s ease-in-out;

        @media (hover: hover) {
          &:hover {
            transform: scale(1.05);
          }
        }
      }
    }
  }

  @media (min-width: 1024px) {
    .about-inner {
      flex-direction: row;
    }
  }
}
</style>
