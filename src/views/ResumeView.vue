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

const summaryCardItems = ref([
  {
    title: 'Professional Summary',
    description: [
      'Detail-oriented Software Developer with 4+ years of experience in web development, creating interactive, user-centered scalable web applications. Proficient in modern front-end and back-end technologies, ensuring high performance, clean and maintainable code. Strong problem-solver with a focus on seamless user experience and performanceoptimization. A collaborative team player with the ability to effectively translate business goals into robust technical solutions.',
    ],
  },
  {
    title: 'Skills',
    description: [
      'HTML5 | CSS/SCSS | TailwindCSS | Vanilla extract | JavaScript | TypeScript',
      'React.js | Vue.js | AngularJS | Backbone.js | Shopify Liquid',
      'Node.js | Python | Java | C#/.NET | C/C++',
      'SQL (PostgreSQL, MySQL) | NoSQL (CouchDB, PouchDB) Databases',
      'RESTful APIs | GraphQL | Microsoft Azure',
      'Agile | Scrum | Kanban | Git | GitHub | GitLab | CI/CD',
      'Shopify Plus | Shopify Hydrogen | Storybook | Figma | Jira | Confluence',
      'Code Refactoring | Code Review | Code Maintenance | Debugging | Testing | Performance Optimization | Documentation',
    ],
  },
  {
    title: 'Continuous Learning & Certifications',
    school: 'LinkedIn Learning',
    description: [
      'Node.js Essential Training',
      'React.js Essential Training',
      'Learning Backbone.js',
      'Responsive Layout',
    ],
  },
])

const workExpCardItems = ref([
  {
    title: 'Web Developer - Team Lead',
    company: 'Molsoft Inc.',
    location: 'Montreal, Quebec',
    date: 'Mar 2023 - Sept 2024',
    description: [
      'Led and mentored a team of 3 developers to deliver custom Shopify and web applications, driving projects from design through deployment and ongoing maintenance.',
      'Developed and optimized internal tools, boosting productivity and reducing project completion time.',
      'Collaborated with product and design teams to translate business requirements and prototypes into scalable, user-friendly applications that improved customer engagement and conversion.',
      'Collaborated with QA to identify and resolve critical bugs, improving overall code quality.',
      'Troubleshot and optimized websites to increase performance, SEO, accessibility and security.',
      'Performed unit testing, and wrote documentation to standardize project workflows and support team onboarding.',
      'Conducted code reviews, and documentation to ensure seamless knowledge transfer.',
    ],
    techStack:
      'Javascript, Typescript, React.js, Shopify Liquid, Shopify Hydrogen, HTML, CSS/SCSS, TailwindCSS, Vanilla extract, GraphQL, Node.js',
  },
  {
    title: 'Front-end Developer',
    company: 'Molsoft Inc.',
    location: 'Montreal, Quebec',
    date: 'May 2021 - Mar 2023',
    description: [
      'Enhanced Shopify themes with custom features, ensuring responsive design and improving performance and user experience.',
      'Optimized websites for improved SEO, accessibility, and security, resulting in faster load times.',
      'Performed unit testing, and wrote documentation to standardize project workflows.',
      'Conducted code reviews,  onboarded and mentored junior developers on best practices.',
    ],
    techStack: 'Javascript, React.js, Shopify Liquid, HTML, CSS/SCSS',
  },
  {
    title: 'Web Developer Intern - CTCM',
    company: 'Corning Technology Center Montreal - iBwave Solutions',
    location: 'Montreal, Quebec',
    date: 'Sept 2020 - Dec 2020',
    description: [
      'Implemented new features for an internal telecommunication network mapping web application tool.',
      'Collaborated with senior developers, gaining experience with large-scale system development practices.',
    ],
    techStack:
      'JavaScript, TypeScript, React.js, HTML, CSS, OpenLayers, PostgreSQL, C#/.Net, Microsoft Azure',
  },
  {
    title: 'Information Technology System Consultant - Intern',
    company: 'Wapikoni Mobile',
    location: 'Montreal, Quebec',
    date: 'May 2020 - Aug 2020',
    description: [
      'Enhanced website performance and usability through optimizations and feature development.',
      'Collaborated with various teams to assess organizational needs.',
      'Implemented a file-sharing system, improving team collaboration and workflow efficiency.',
    ],
    techStack: 'HTML, CSS, JavaScript, AngularJS',
  },
  {
    title: 'Web Developer Intern - Civil Aviation',
    company: 'CAE Inc.',
    location: 'Montreal, Quebec',
    date: 'Sept 2019 - Dec 2019',
    description: [
      'Developed features for civil aviation training courseware application.',
      'Researched and applied emerging technologies to improve and optimize development processes.',
    ],
    techStack: 'JavaScript, React.js, Vue.js, HTML, CSS/SCSS, PouchDB/CouchDB',
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
        <div class="card-items card-item--first-full-width" v-if="selectedTab === 0">
          <CardItem
            v-for="item in summaryCardItems"
            :key="item.title"
            :title="item.title"
            :school="item.school"
            :description="item.description"
          />
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

  .card-items {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(400px, 1fr));
    gap: 1rem;
  }

  .card-item--first-full-width {
    & :first-child {
      grid-column: 1 / -1;
      width: 100%;
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
