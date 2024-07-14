from textwrap import dedent
from crewai import Task

class ResumeTasks():
    def research_industry_trends_task(self, agent, job_title, industry):
        return Task(
            description=dedent(f"""\
                Research current trends, in-demand skills, and common requirements for the {job_title} role in the {industry} industry.
                Identify at least 5 key technologies, 3 methodologies, and 2 certifications that are highly valued.
                Compile a detailed report summarizing these insights, with at least 3 specific suggestions for each section of a resume (summary, experience, skills, etc.).
                Include information on preferred resume formats and styles in this industry.
                Do not include any specific company names in this research."""),
            expected_output=dedent("""\
                A comprehensive report with:
                1. List of 5+ key technologies
                2. List of 3+ methodologies
                3. List of 2+ relevant certifications
                4. At least 3 specific suggestions for each resume section
                5. Insights on preferred resume formats and styles in the industry
                Total output should be at least 600 words."""),
            agent=agent
        )

    def analyze_job_description_task(self, agent, job_description):
        return Task(
            description=dedent(f"""\
                Analyze the provided job description in detail: "{job_description}".
                Identify all key requirements, preferred qualifications, and any specific language or keywords used.
                Create a comprehensive list of at least 15 important points to address in the resume, including skills, experiences, and qualities the ideal candidate should highlight.
                This list should cover all aspects of a full resume, providing at least 3 specific suggestions for each standard section (summary, experience, education, skills).
                Identify any unique requirements or preferences mentioned in the job description that might require custom resume sections.
                Do not assume any information about the candidate that is not explicitly provided."""),
            expected_output=dedent("""\
                A detailed analysis including:
                1. List of 15+ key points from the job description
                2. At least 3 specific suggestions for each standard resume section
                3. A list of important keywords and phrases to include
                4. Suggestions for any custom sections based on unique job requirements
                Total output should be at least 500 words."""),
            agent=agent
        )

    def draft_resume_task(self, agent, candidate_info, job_description):
        return Task(
            description=dedent(f"""\
                Create a full, detailed resume for the candidate based ONLY on their provided information: "{candidate_info}".
                Do not invent or assume any information not explicitly stated in the candidate_info.
                Tailor the resume to the job description without adding false experiences.
                Include the following sections, each with specific content:
                1. Professional Summary: A compelling paragraph (4-6 sentences) highlighting key qualifications and career objectives based on the actual information provided.
                2. Work Experience: Include only the jobs mentioned in the candidate_info. For each job, provide 4-6 bullet points using strong action verbs and quantifying results where possible.
                3. Education: List only the educational qualifications mentioned in the candidate_info.
                4. Skills: Create a comprehensive list of technical and soft skills mentioned in the candidate_info, relevant to the job. Organize these skills into categories if appropriate.
                5. Additional sections as appropriate (e.g., certifications, volunteer work, projects) only if mentioned in the candidate_info.
                6. Consider creating a custom section that highlights the candidate's unique strengths or aligns particularly well with the job description, based on the provided information.
                Ensure the resume is ATS-friendly by incorporating relevant keywords from the job description throughout, but only where they genuinely apply to the candidate's actual experience."""),
            expected_output=dedent("""\
                A full, tailored resume that accurately reflects the candidate's provided information, including:
                1. Professional Summary
                2. Work Experience (only jobs mentioned by the candidate)
                3. Education (only qualifications mentioned by the candidate)
                4. Skills (categorized if appropriate)
                5. Any additional sections based on provided information
                6. A custom section highlighting unique strengths (if applicable)
                The resume should be detailed, ATS-friendly, and without any invented information."""),
            agent=agent
        )

    def optimize_resume_task(self, agent, job_description, drafted_resume):
        return Task(
            description=dedent(f"""\
                Review and optimize the drafted resume: "{drafted_resume}" for the job: "{job_description}".
                Ensure it's tailored to the specific role and uses impactful action verbs throughout.
                Optimize for ATS systems by:
                1. Incorporating key terms from the job description, but only where they genuinely apply to the candidate's actual experience.
                2. Ensuring proper formatting that can be easily parsed by ATS (e.g., standard section headings, appropriate use of bullet points).
                3. Avoiding graphics, tables, or complex formatting that might confuse ATS.
                4. Using a clean, simple font and consistent formatting throughout.
                Enhance the impact of the resume by:
                1. Ensuring each bullet point starts with a strong action verb.
                2. Quantifying achievements and results wherever possible.
                3. Tailoring the professional summary to closely match the job requirements.
                4. Adjusting the order of skills or experiences to prioritize those most relevant to the job.
                Do not add any information that wasn't in the original draft.
                Provide the optimized resume content, ready for final formatting."""),
            expected_output=dedent("""\
                A fully optimized, ATS-friendly resume content that is tailored to the specific job role, uses impactful language,
                and effectively highlights the candidate's most relevant experiences and skills.
                The optimized content should be ready for final formatting, without any invented or assumed information."""),
            agent=agent
        )

    def format_resume_task(self, agent, optimized_content, industry_trends):
        return Task(
            description=dedent(f"""\
                Format the optimized resume content: "{optimized_content}" into a polished, professional layout.
                Consider the industry trends and preferred formats: "{industry_trends}".
                Follow these formatting guidelines:
                1. Use a clean, professional font (e.g., Arial, Calibri, or Helvetica) at 10-12 point size.
                2. Ensure consistent spacing and alignment throughout the document.
                3. Use bold, italics, and underlining sparingly and consistently to highlight key information.
                4. Implement appropriate margins (usually 0.5 to 1 inch on all sides).
                5. Ensure the resume fits within 1-2 pages, depending on the candidate's experience level.
                6. Use bullet points for easy readability in the experience and skills sections.
                7. Include the candidate's name and contact information prominently at the top of the resume.
                8. Consider using subtle color or design elements if appropriate for the industry, but maintain a professional appearance.
                Provide the final formatted resume in markdown format, ready for submission."""),
            expected_output=dedent("""\
                A professionally formatted resume in markdown format, incorporating all the optimized content.
                The resume should be visually appealing, easy to read, and adhere to industry standards and preferences."""),
            agent=agent
        )

    def final_review_task(self, agent, formatted_resume):
        return Task(
            description=dedent(f"""\
                Conduct a final review of the formatted resume: "{formatted_resume}".
                Check for the following:
                1. Overall impact and alignment with the job description.
                2. Consistency in formatting, tense, and style.
                3. Proper grammar, spelling, and punctuation.
                4. Appropriate use of industry-specific terminology.
                5. Balanced distribution of information across sections.
                6. Ensure all links (if any) are functional.
                7. Verify that the resume length is appropriate (1-2 pages).
                8. Confirm that no personal information beyond name and professional contact details is included.
                Provide a brief report on the resume's strengths and any final suggestions for improvement.
                If any critical issues are found, provide specific recommendations for corrections."""),
            expected_output=dedent("""\
                A comprehensive review report including:
                1. Overall assessment of the resume's impact and effectiveness.
                2. Specific strengths of the resume.
                3. Any suggestions for final improvements or corrections.
                4. Confirmation that the resume meets all professional standards and is ready for submission."""),
            agent=agent
        )
