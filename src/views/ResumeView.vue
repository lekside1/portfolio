<script setup lang="ts">
import { ref } from 'vue'

import TitleComponent from '@/components/TitleComponent.vue'
import PageContent from '@/components/PageContent.vue'
import IconsComponent from '@/components/IconsComponent.vue'

import resume from '@/assets/afa-resume-2025.pdf'

import WelcomeItem from '@/components/WelcomeItem.vue'
import DocumentationIcon from '@/components/icons/IconDocumentation.vue'
import ToolingIcon from '@/components/icons/IconTooling.vue'
import EcosystemIcon from '@/components/icons/IconEcosystem.vue'
import CommunityIcon from '@/components/icons/IconCommunity.vue'
import SupportIcon from '@/components/icons/IconSupport.vue'

const tabs = ref([
  { title: 'Summary', icon: 'summary' },
  { title: 'Work experience', icon: 'work' },
  { title: 'Education', icon: 'education' },
])

const selectedTab = ref(0)

const selectTab = (index: number) => {
  selectedTab.value = index
}
</script>

<template>
  <PageContent class="resume">
    <TitleComponent title="Resume" />

    <div class="tabs-container">
      <div class="tabs">
        <button
          :class="[
            'tab-button',
            index % 2 === 0 ? 'button' : 'button button-tertiary',
            { active: selectedTab === index },
          ]"
          v-for="(tab, index) in tabs"
          :key="index"
          :aria-label="tab.title"
          @click="selectTab(index)"
        >
          <span class="button-title">{{ tab.title }}</span>
          <IconsComponent :icon="tab.icon" />
        </button>

        <!-- Download resume button -->
        <a
          :href="resume"
          download="AFA-Resume"
          class="button button-tertiary button-download"
          aria-label="Download resume pdf"
        >
          <span class="button-title">Download</span>
          <IconsComponent icon="download" />
        </a>
      </div>

      <div class="tab-content">
        <!-- TODO: Summary -->
        <div v-if="selectedTab === 0">
          <div class="tab-content-item">
            <h2 class="green">Professional Summary</h2>
            <p>
              Detail-oriented Software Developer with experience developing innovative software
              solutions. Demonstrates collaborative teamwork, strong communication skills, and
              excels at efficiently resolving issues. A quick learner with a results-driven mindset,
              committed to delivering high-quality results in fast-paced environments..
            </p>
          </div>

          <div class="tab-content-item">
            <h2 class="green">Summary of Skills</h2>
            <ul>
              <li>HTML, CSS/SCSS, JavaScript, TypeScript</li>
              <li>React, Vue.js, Shopify Liquid</li>
              <li>Node.js, Python, Java, C/C++, C#/.NET</li>

              <li>MySQL, PostgreSQL, NoSQL Databases</li>
              <li>RESTful APIs, GraphQL</li>

              <li>Git, GitHub, GitLab</li>
              <li>Agile, Scrum, Kanban</li>

              <li>Shopify Plus, Shopify Hydrogen, Figma, Jira, Confluence</li>
            </ul>
          </div>
        </div>

        <!-- TODO: Work experience -->
        <div v-if="selectedTab === 1">
          <WelcomeItem>
            <template #icon>
              <DocumentationIcon />
            </template>
            <template #heading>Work experience</template>

            Vue’s
            <a href="https://vuejs.org/" target="_blank" rel="noopener">official documentation</a>
            provides you with all information you need to get started.
          </WelcomeItem>

          <WelcomeItem>
            <template #icon>
              <ToolingIcon />
            </template>
            <template #heading>Tooling</template>

            This project is served and bundled with
            <a href="https://vite.dev/guide/features.html" target="_blank" rel="noopener">Vite</a>.
            The recommended IDE setup is
            <a href="https://code.visualstudio.com/" target="_blank" rel="noopener">VSCode</a>
            +
            <a href="https://github.com/johnsoncodehk/volar" target="_blank" rel="noopener">Volar</a
            >. If you need to test your components and web pages, check out
            <a href="https://www.cypress.io/" target="_blank" rel="noopener">Cypress</a>
            and
            <a href="https://on.cypress.io/component" target="_blank" rel="noopener"
              >Cypress Component Testing</a
            >.

            <br />

            More instructions are available in <code>README.md</code>.
          </WelcomeItem>

          <WelcomeItem>
            <template #icon>
              <EcosystemIcon />
            </template>
            <template #heading>Ecosystem</template>

            Get official tools and libraries for your project:
            <a href="https://pinia.vuejs.org/" target="_blank" rel="noopener">Pinia</a>,
            <a href="https://router.vuejs.org/" target="_blank" rel="noopener">Vue Router</a>,
            <a href="https://test-utils.vuejs.org/" target="_blank" rel="noopener">Vue Test Utils</a
            >, and
            <a href="https://github.com/vuejs/devtools" target="_blank" rel="noopener"
              >Vue Dev Tools</a
            >. If you need more resources, we suggest paying
            <a href="https://github.com/vuejs/awesome-vue" target="_blank" rel="noopener"
              >Awesome Vue</a
            >
            a visit.
          </WelcomeItem>

          <WelcomeItem>
            <template #icon>
              <CommunityIcon />
            </template>
            <template #heading>Community</template>

            Got stuck? Ask your question on
            <a href="https://chat.vuejs.org" target="_blank" rel="noopener">Vue Land</a>, our
            official Discord server, or
            <a
              href="https://stackoverflow.com/questions/tagged/vue.js"
              target="_blank"
              rel="noopener"
              >StackOverflow</a
            >. You should also subscribe to
            <a href="https://news.vuejs.org" target="_blank" rel="noopener">our mailing list</a>
            and follow the official
            <a href="https://twitter.com/vuejs" target="_blank" rel="noopener">@vuejs</a>
            twitter account for latest news in the Vue world.
          </WelcomeItem>

          <WelcomeItem>
            <template #icon>
              <SupportIcon />
            </template>
            <template #heading>Support Vue</template>

            As an independent project, Vue relies on community backing for its sustainability. You
            can help us by
            <a href="https://vuejs.org/sponsor/" target="_blank" rel="noopener"
              >becoming a sponsor</a
            >.
          </WelcomeItem>
        </div>

        <!-- TODO: Education -->
        <div v-if="selectedTab === 2">
          <WelcomeItem>
            <template #icon>
              <DocumentationIcon />
            </template>
            <template #heading>Education</template>

            Vue’s
            <a href="https://vuejs.org/" target="_blank" rel="noopener">official documentation</a>
            provides you with all information you need to get started.
          </WelcomeItem>

          <WelcomeItem>
            <template #icon>
              <ToolingIcon />
            </template>
            <template #heading>Tooling</template>

            This project is served and bundled with
            <a href="https://vite.dev/guide/features.html" target="_blank" rel="noopener">Vite</a>.
            The recommended IDE setup is
            <a href="https://code.visualstudio.com/" target="_blank" rel="noopener">VSCode</a>
            +
            <a href="https://github.com/johnsoncodehk/volar" target="_blank" rel="noopener">Volar</a
            >. If you need to test your components and web pages, check out
            <a href="https://www.cypress.io/" target="_blank" rel="noopener">Cypress</a>
            and
            <a href="https://on.cypress.io/component" target="_blank" rel="noopener"
              >Cypress Component Testing</a
            >.

            <br />

            More instructions are available in <code>README.md</code>.
          </WelcomeItem>

          <WelcomeItem>
            <template #icon>
              <EcosystemIcon />
            </template>
            <template #heading>Ecosystem</template>

            Get official tools and libraries for your project:
            <a href="https://pinia.vuejs.org/" target="_blank" rel="noopener">Pinia</a>,
            <a href="https://router.vuejs.org/" target="_blank" rel="noopener">Vue Router</a>,
            <a href="https://test-utils.vuejs.org/" target="_blank" rel="noopener">Vue Test Utils</a
            >, and
            <a href="https://github.com/vuejs/devtools" target="_blank" rel="noopener"
              >Vue Dev Tools</a
            >. If you need more resources, we suggest paying
            <a href="https://github.com/vuejs/awesome-vue" target="_blank" rel="noopener"
              >Awesome Vue</a
            >
            a visit.
          </WelcomeItem>

          <WelcomeItem>
            <template #icon>
              <CommunityIcon />
            </template>
            <template #heading>Community</template>

            Got stuck? Ask your question on
            <a href="https://chat.vuejs.org" target="_blank" rel="noopener">Vue Land</a>, our
            official Discord server, or
            <a
              href="https://stackoverflow.com/questions/tagged/vue.js"
              target="_blank"
              rel="noopener"
              >StackOverflow</a
            >. You should also subscribe to
            <a href="https://news.vuejs.org" target="_blank" rel="noopener">our mailing list</a>
            and follow the official
            <a href="https://twitter.com/vuejs" target="_blank" rel="noopener">@vuejs</a>
            twitter account for latest news in the Vue world.
          </WelcomeItem>

          <WelcomeItem>
            <template #icon>
              <SupportIcon />
            </template>
            <template #heading>Support Vue</template>

            As an independent project, Vue relies on community backing for its sustainability. You
            can help us by
            <a href="https://vuejs.org/sponsor/" target="_blank" rel="noopener"
              >becoming a sponsor</a
            >.
          </WelcomeItem>
        </div>
      </div>
    </div>
  </PageContent>
</template>

<style scoped>
.resume {
  .tab-button,
  .button-download {
    display: flex;
    align-items: center;
    gap: 0.5rem;

    .button-title {
      display: none;
    }
  }

  .tabs {
    display: flex;
    place-content: center;
    padding: 1.5rem;
    gap: 1.5rem;
  }

  .tab-content-item {
    padding: 1rem 0;

    p,
    ul {
      margin: 0.5rem 0;
    }

    li {
      margin-bottom: 1rem;
    }
  }

  /* Desktop */
  @media (min-width: 1024px) {
    .tab-button,
    .button-download {
      display: flex;
      align-items: center;
      gap: 0.5rem;

      .button-title {
        display: block;
      }
    }

    .tabs {
      padding: 1.5rem;
      gap: 1.5rem;
    }
  }
}
</style>
