# Replace en dash (–) with hyphen (-) to avoid UnicodeEncodeError
import re

def clean_text(text):
    return re.sub(r"[–•]", "-", text)

# Regenerate the PDF with cleaned text
class ResumePDFClean(FPDF):
    def header(self):
        self.set_font("Arial", "B", 16)
        self.cell(0, 10, clean_text("ADELEKAN XXXXX"), ln=True, align="C")
        self.set_font("Arial", "", 12)
        self.cell(0, 10, clean_text("xxxxxx@outlook.com | linkedin.com/in/xxxxx | github.com/xxxxx | (438) XXX-XXXX | [Location]"), ln=True, align="C")
        self.ln(5)

    def add_section_title(self, title):
        self.set_font("Arial", "B", 14)
        self.set_text_color(30, 30, 30)
        self.cell(0, 10, clean_text(title), ln=True)
        self.set_text_color(0, 0, 0)

    def add_bullet_point(self, text):
        self.set_font("Arial", "", 11)
        self.multi_cell(0, 8, clean_text(f"- {text}"))

    def add_paragraph(self, text):
        self.set_font("Arial", "", 11)
        self.multi_cell(0, 8, clean_text(text))
        self.ln(2)

pdf = ResumePDFClean()
pdf.add_page()

# Add resume content
pdf.add_section_title("PROFESSIONAL SUMMARY")
pdf.add_paragraph("Results-driven and detail-oriented Software Developer with over 4 years of experience in building scalable, high-performance web applications. Proven track record of leading development teams, collaborating cross-functionally, and delivering seamless user experiences. Proficient in React, TypeScript, Node.js, GraphQL, and Shopify Liquid, with strong problem-solving and communication skills.")

pdf.add_section_title("CORE SKILLS")
skills = [
    "HTML5, CSS/SCSS, JavaScript, TypeScript, React.js, Vue.js, Java, C/C++, C#/.NET, Node.js, Python",
    "Shopify Liquid, Shopify Hydrogen, Shopify Plus",
    "RESTful APIs, GraphQL, SQL, NoSQL (CouchDB, PouchDB)",
    "Git, GitHub/GitLab, Figma, Storybook",
    "Jira, Confluence, Agile/Scrum, Sprint Planning",
    "Unit Testing, Performance Optimization, Documentation, Cross-Browser Compatibility"
]
for skill in skills:
    pdf.add_bullet_point(skill)

pdf.add_section_title("PROFESSIONAL EXPERIENCE")
pdf.add_paragraph("Team Lead - Web Developer | Molsoft Inc., Montreal, QC | Mar 2023 - Sept 2024")
for item in [
    "Led a team of 3 developers across multiple Shopify and web development projects.",
    "Built custom Shopify themes and apps with responsive design.",
    "Utilized React, TypeScript, Liquid, GraphQL, REST API, Node.js.",
    "Collaborated cross-functionally, conducted code reviews, and participated in Agile ceremonies."
]:
    pdf.add_bullet_point(item)

pdf.ln(2)
pdf.add_paragraph("Front-end Developer | Molsoft Inc., Montreal, QC | May 2021 - Mar 2023")
for item in [
    "Developed and maintained Shopify storefronts using JavaScript, React, Liquid.",
    "Wrote documentation and participated in peer code reviews."
]:
    pdf.add_bullet_point(item)

pdf.ln(2)
pdf.add_paragraph("Web Developer Intern - CTCM (DNA Team) | iBwave Solutions | Sept 2020 - Dec 2020")
for item in [
    "Enhanced DNA network visualization tool using React, OpenLayers, PostgreSQL.",
    "Contributed to full-stack development and cloud integration with Microsoft Azure."
]:
    pdf.add_bullet_point(item)

pdf.ln(2)
pdf.add_paragraph("IT System Consultant Intern | Wapikoni Mobile | May 2020 - Aug 2020")
for item in [
    "Redesigned company website using HTML, CSS, and JavaScript.",
    "Improved interdepartmental collaboration with a new file sharing system."
]:
    pdf.add_bullet_point(item)

pdf.ln(2)
pdf.add_paragraph("Web Developer Intern | CAE Inc. | Sept 2019 - Dec 2019")
for item in [
    "Supported development of training interfaces using React, Vue.js, CouchDB.",
    "Participated in Scrum ceremonies and feature development."
]:
    pdf.add_bullet_point(item)

pdf.add_section_title("EDUCATION")
pdf.add_paragraph("Bachelor of Computer Science (Co-op Program) | Concordia University | 2018 - 2021")
pdf.add_paragraph("Bachelor of Science - Specialization in Biology | Concordia University | 2013 - 2016")

pdf.add_section_title("LANGUAGES")
pdf.add_paragraph("English (Fluent), French (Fluent), Yoruba (Native)")

pdf.add_section_title("INTERESTS")
pdf.add_paragraph("Tech & Innovation, Football (Soccer), Dodgeball, Video Games, Visual Arts, Music, Languages, Travel")

# Save the cleaned PDF
resume_path = "/mnt/data/Adelekan_Resume.pdf"
pdf.output(resume_path)

resume_path
