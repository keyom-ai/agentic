from dotenv import load_dotenv
load_dotenv()

from crewai import Agent, Task, Crew, Process
import logging

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def run_resume_creation_process(candidate_info, job_title, industry, job_description):
    # Create a single agent for resume creation
    resume_agent = Agent(
        role='Professional Resume Writer',
        goal='Create a concise, impactful, and ATS-friendly resume tailored to the specific job description',
        backstory='Experienced in crafting effective resumes for senior professionals, with expertise in highlighting key achievements and relevant skills',
        verbose=True
    )

    # Create a single task for resume creation
    resume_task = Task(
        description=f"""
        Create a professional, ATS-friendly resume based on the following information:
        Candidate Info: {candidate_info}
        Job Title: {job_title}
        Industry: {industry}
        Job Description: {job_description}

        The resume should include:
        1. Contact Information: Full name, email, phone number, and location (city, state).
        2. Professional Summary: A concise 2-3 sentence summary highlighting key qualifications and achievements most relevant to the job description.
        3. Skills: List 10-12 key technical skills most relevant to the job description. Include 3-4 soft skills if applicable.
        4. Work Experience:
           - For the most recent role (likely at Capgemini Financial Services):
             * Company name, job title, and employment dates (MM/YYYY - Present)
             * 4-5 bullet points highlighting significant achievements and responsibilities
             * Focus on projects, technologies, and accomplishments most relevant to the target job
             * Use action verbs and include quantifiable results where possible
           - For the next 1-2 most recent roles:
             * Company name, job title, and employment dates (MM/YYYY - MM/YYYY)
             * 2-3 bullet points highlighting key responsibilities or achievements
           - For older roles, provide a brief list:
             * Company name, job title, and employment dates (YYYY - YYYY)
        5. Education: Degree, major, institution name (if provided)
        6. Certifications: List the most recent and relevant certifications

        Ensure the resume is ATS-friendly by:
        - Using standard section headings
        - Incorporating keywords from the job description naturally throughout the resume
        - Using a clean, simple format without tables or complex formatting

        Format the resume in Markdown, using appropriate syntax for headings, bullet points, and emphasis.
        The entire resume should not exceed the equivalent of two pages when formatted.
        """,
        expected_output="""
        A concise, professionally formatted resume in Markdown, including all relevant sections based on the provided information.
        The resume should be ATS-friendly, highlighting key skills and experiences related to the job description,
        with a focus on the candidate's most recent and relevant achievements. The content should be tailored to the specific job requirements,
        emphasizing recent accomplishments and skills without being overly verbose.
        """,
        agent=resume_agent
    )

    # Create a crew with just this task
    crew = Crew(
        agents=[resume_agent],
        tasks=[resume_task],
        verbose=2
    )

    # Execute the task
    result = crew.kickoff()

    logger.info(f"Resume created: {result[:100]}...")  # Log first 100 characters of the result

    return result
