<script setup lang="ts">
import { ref } from 'vue'

import TitleComponent from '@/components/TitleComponent.vue'
import PageContent from '@/components/PageContent.vue'
import IconsComponent from '@/components/IconsComponent.vue'
import CardItem from '@/components/CardItem.vue'

import resume from '@/assets/afa-resume.pdf'

const tabs = ref([
  { title: 'Summary', icon: 'summary' },
  { title: 'Work experience', icon: 'work' },
  { title: 'Education', icon: 'education' },
])

const selectedTab = ref(0)

const selectTab = (index: number) => {
  selectedTab.value = index
}

const workExpCardItems = ref([
  {
    title: 'Software Developer - Team Lead',
    company: 'Molsoft Inc.',
    location: 'Montreal, Quebec',
    date: 'Mar 2023 - Sept 2024',
    description: [
      'Led a team of 3 developers across multiple projects; from design phase to completion, and ongoing maintenance.',
      'Developed custom Shopify themes and apps, ensuring responsive design and seamless user experience.',
      'Collaborated with product, design, and integration teams.',
      'Troubleshoot and optimize websites to increase performance, SEO, and security.',
      'Performed unit testing, and wrote documentation to standardize project workflows and support team onboarding.',
      'Performed code reviews, ensuring adherence to coding standards',
      'Performed quality assurance to maintain high-quality output.',
      'Mentored junior developers, providing guidance on best practices and technical skills.',
    ],
    techStack:
      'Javascript, Typescript, React, Shopify Liquid, Shopify Hydrogen, HTML, CSS/SCSS, REST API,  GraphQL, Node.js, Vanilla extract',
  },
  {
    title: 'Front-end Developer',
    company: 'Molsoft Inc.',
    location: 'Montreal, Quebec',
    date: 'May 2021 - Mar 2023',
    description: [
      'Developed custom Shopify themes ensuring responsive design and seamless user experience across devices.',
      'Troubleshoot and optimize websites to increase performance, SEO, and security.',
      'Performed unit testing, and wrote documentation to standardize project workflows and support team onboarding.',
      'Performed code reviews, ensuring adherence to coding standards',
    ],
    techStack: 'Javascript, React, Shopify Liquid, HTML, CSS/SCSS',
  },
  {
    title: 'Web Developer for CTCM - Intern',
    company: 'CTCM (Corning Technology Center Montreal - iBwave Solutions)',
    location: 'St-Laurent, Quebec',
    date: 'Sept 2020 - Dec 2020',
    description: [
      'Member of the DNA (Dense Network Architecture) Team.',
      'Developed features for the DNA multi-connected network map.',
    ],
    techStack:
      'JavaScript, TypeScript, React, HTML, CSS, OpenLayers, PostgreSQL, C#/.Net, Microsoft Azure',
  },
  {
    title: 'Information Technology System Assistant - Intern',
    company: 'Wapikoni Mobile',
    location: 'Montreal, Quebec',
    date: 'May 2020 - Aug 2020',
    description: [
      'Performed front-end development on the Wapikoni website.',
      'Collaborated with various teams to assess organizational needs.',
      'Proposed and implemented an optimized file storage and sharing solution, improving cross-team collaboration and accessibility of resources.',
    ],
    techStack: 'HTML, CSS, JavaScript, Google Drive',
  },
  {
    title: 'Web Developer - Intern',
    company: 'CAE Inc.',
    location: 'St-Laurent, Quebec',
    date: 'Sept 2019 - Dec 2019',
    description: [
      'Member of the Civil Aviation Courseware Development Team.',
      'Front-end development on the Civil Aviation Courseware software.',
    ],
    techStack: 'JavaScript, React, Vue.js, HTML, CSS, PouchDB/CouchDB',
  },
])

const educationCardItems = ref([
  {
    title: 'Bachelor of Computer Science – General Program Co-op',
    school: 'Gina Cody School of Engineering and Computer Science, Concordia University',
    location: 'Montreal, Quebec',
    date: '2018 - 2021',
    description: ['Member of the Institute for Co-operative Education'],
  },
  {
    title: 'Bachelor of Science – Specialization in Biology',
    school: 'Concordia University',
    location: 'Montreal, Quebec',
    date: '2013 - 2016',
  },
])
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
        <div v-if="selectedTab === 0">
          <div class="tab-content-item">
            <h2 class="green">Professional Summary</h2>
            <p>
              <strong>Detail-oriented Software Developer</strong> with a proven ability to
              collaborate in teams, communicate effectively, and efficiently resolve complex
              technical challenges. A quick learner with a <strong>results-driven mindset</strong>,
              committed to delivering <strong>high-quality, innovative solutions</strong>.
              Proficient in <strong>modern development frameworks, languages, and tools</strong>,
              with expertise in
              <strong
                >React, TypeScript, Shopify Liquid, Node.js, GraphQL, and SQL/NoSQL
                databases</strong
              >, ensuring scalable and robust software delivery.
            </p>
          </div>

          <div class="tab-content-item">
            <h2 class="green">Summary of Skills</h2>
            <ul>
              <li>HTML, CSS/SCSS, JavaScript, TypeScript</li>
              <li>React, Vue.js, Shopify Liquid</li>
              <li>Node.js, Python, Java, C/C++, C#/.NET</li>

              <li>SQL/NoSQL Databases</li>
              <li>RESTful APIs, GraphQL</li>

              <li>Git, GitHub, GitLab</li>
              <li>Agile, Scrum, Kanban</li>

              <li>Shopify Plus, Shopify Hydrogen, Figma, Jira, Confluence</li>
            </ul>
          </div>
        </div>

        <div class="card-items" v-if="selectedTab === 1">
          <CardItem
            v-for="item in workExpCardItems"
            :key="item.title"
            :title="item.title"
            :company="item.company"
            :location="item.location"
            :date="item.date"
            :description="item.description"
            :techStack="item.techStack"
          />
        </div>

        <div class="card-items" v-if="selectedTab === 2">
          <CardItem
            v-for="item in educationCardItems"
            :key="item.title"
            :title="item.title"
            :school="item.school"
            :location="item.location"
            :date="item.date"
            :description="item.description"
          />
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

  .card-items {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(400px, 1fr));
    gap: 1rem;
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
