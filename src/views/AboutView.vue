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

      <div class="about-content">
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
    padding: 1rem;

    .about-img {
      border-radius: 1rem;
    }
  }

  .about-content {
    padding: 1rem;

    li {
      margin-bottom: 1rem;
    }
  }
  /*
  .information {
    p {
      margin: 1rem 0;
    }
  } */

  @media (min-width: 1024px) {
    .about-inner {
      flex-direction: row;
    }
  }
}
</style>
