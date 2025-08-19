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
    title: 'Web Developer - Team Lead',
    company: 'Molsoft Inc.',
    location: 'Montreal, Quebec',
    date: 'Mar 2023 - Sept 2024',
    description: [
      'Led a team of 3 developers across multiple projects; from design phase to completion, and ongoing maintenance.',
      'Developed custom Shopify themes and apps, ensuring responsive design and seamless user experience.',
      'Collaborated with product, design, and integration teams.',
      'Implemented and optimized internal tools, boosting productivity and reducing project completion time.',
      'Troubleshoot and optimize websites to increase performance, SEO, accessibility and security.',
      'Performed unit testing, and wrote documentation to standardize project workflows and support team onboarding.',
      'Performed code reviews, ensuring adherence to coding standards',
      'Performed quality assurance to maintain high-quality output.',
      'Mentored junior developers, providing guidance on best practices and technical skills.',
    ],
    techStack:
      'Javascript, Typescript, React, Shopify Liquid, Shopify Hydrogen, HTML, CSS/SCSS, Tailwind, Vanilla extract, GraphQL, Node.js',
  },
  {
    title: 'Front-end Developer',
    company: 'Molsoft Inc.',
    location: 'Montreal, Quebec',
    date: 'May 2021 - Mar 2023',
    description: [
      'Developed custom Shopify themes ensuring responsive design and seamless user experience across devices.',
      'Troubleshoot and optimize websites to increase performance, SEO, accessibility and security.',
      'Performed unit testing, and wrote documentation to standardize project workflows and support team onboarding.',
      'Performed code reviews, ensuring adherence to coding standards',
    ],
    techStack: 'Javascript, React, Shopify Liquid, HTML, CSS/SCSS',
  },
  {
    title: 'Web Developer Intern - CTCM',
    company: 'Corning Technology Center Montreal - iBwave Solutions',
    location: 'Montreal, Quebec',
    date: 'Sept 2020 - Dec 2020',
    description: [
      'Implemented features on an internal telecommunication network application',
      'Shadowed developers to learn key details about job duties and tasks.',
    ],
    techStack:
      'JavaScript, TypeScript, React, HTML, CSS, OpenLayers, PostgreSQL, C#/.Net, Microsoft Azure services',
  },
  {
    title: 'Information Technology System Consultant - Intern',
    company: 'Wapikoni Mobile',
    location: 'Montreal, Quebec',
    date: 'May 2020 - Aug 2020',
    description: [
      "Developed and maintained the organization's internal website improving user experience.",
      'Collaborated with various teams to assess organizational needs.',
      'Implemented a new file-sharing system, improving team collaboration and workflow efficiency.',
    ],
    techStack: 'HTML, CSS, JavaScript, Google Drive',
  },
  {
    title: 'Web Developer Intern - Civil Aviation',
    company: 'CAE Inc.',
    location: 'Montreal, Quebec',
    date: 'Sept 2019 - Dec 2019',
    description: [
      'Developed features on a civil aviation training courseware application.',
      'Engaged in continuous learning of emerging technologies, incorporating industry advancements into projects when applicable.',
    ],
    techStack: 'JavaScript, React, Vue.js, HTML, CSS, PouchDB/CouchDB',
  },
])

const educationCardItems = ref([
  {
    title: 'Bachelor of Computer Science - Co-op',
    school: 'Gina Cody School of Engineering and Computer Science, Concordia University',
    location: 'Montreal, Quebec',
    date: '2018 - 2021',
    description: ['Member of the Institute for Co-operative Education'],
  },
  {
    title: 'Bachelor of Science - Specialization in Biology',
    school: 'Concordia University',
    location: 'Montreal, Quebec',
    date: '2013 - 2016',
  },
  {
    title: 'Certifications',
    school: 'LinkedIn Learning',
    date: '2019',
    description: [
      'Node.js Essential Training (Nov 2019)',
      'React.js Essential Training (Nov 2019)',
      'Learning Backbone.js (Oct 2019)',
      'Responsive Layout (Oct 2019)',
    ],
  },
])
</script>

<template>
  <PageContent class="resume">
    <TitleComponent title="Resume" />

    <div class="tabs-container">
      <div class="tabs">
        <button
          :class="['tab-button', 'button', { active: selectedTab === index }]"
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
            <h2 class="green uppercase">Professional Summary</h2>
            <p>
              Detail-oriented Software Developer with 4+ years of experience in web development,
              creating interactive, user-centered scalable web applications. Proficient in modern
              front-end and back-end technologies, ensuring high performance, clean and maintainable
              code. Strong problem-solver with a focus on seamless user experience and performance
              optimization. A collaborative team player with the ability to effectively translate
              business goals into robust technical solutions.
            </p>
          </div>

          <div class="tab-content-item">
            <h2 class="green uppercase">Skills</h2>
            <ul>
              <li>HTML, CSS/SCSS, JavaScript, TypeScript</li>
              <li>React.js, Vue.js, Backbone.js, Shopify Liquid</li>
              <li>Node.js, Python, Java, C/C++, C#/.NET</li>

              <li>SQL/NoSQL Databases</li>
              <li>RESTful APIs, GraphQL, Microsoft Azure</li>

              <li>Git, GitHub, GitLab</li>
              <li>Agile, Scrum, Kanban</li>

              <li>
                Shopify Plus, Shopify Hydrogen, VS Code, Eclipse, Figma, Jira, Confluence, Storybook
              </li>
              <li>Code Refactoring, Debugging, Testing, Performance Optimization, Documentation</li>
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

    .button-download {
      .button-title {
        font-size: 13.333333px;
      }
    }

    .tabs {
      padding: 1.5rem;
      gap: 1.5rem;
    }
  }
}
</style>
