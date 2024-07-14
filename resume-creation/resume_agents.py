import os
from crewai import Agent
from crewai_tools.tools import WebsiteSearchTool, SerperDevTool

# Set the model name to GPT-3.5 Turbo
os.environ["OPENAI_MODEL_NAME"] = "gpt-3.5-turbo"

web_search_tool = WebsiteSearchTool()
serper_dev_tool = SerperDevTool()

class ResumeAgents():
    def industry_research_agent(self):
        return Agent(
            role='Industry Research Analyst',
            goal='Analyze industry trends and job market demands to provide insights for resume creation.',
            tools=[web_search_tool, serper_dev_tool],
            backstory='Expert in analyzing job market trends and identifying key skills and qualifications in demand across various industries.',
            verbose=True,
            allow_delegation=False,
            model_name="gpt-3.5-turbo"
        )

    def resume_writer_agent(self):
        return Agent(
            role='Professional Resume Writer',
            goal='Create a full, detailed resume that highlights the candidate\'s strengths and aligns with job requirements.',
            tools=[web_search_tool, serper_dev_tool],
            backstory='Experienced in crafting comprehensive, professional resumes that effectively communicate candidates\' value to potential employers.',
            verbose=True,
            allow_delegation=False,
            model_name="gpt-3.5-turbo"
        )

    def ats_optimization_agent(self):
        return Agent(
            role='ATS Optimization Specialist',
            goal='Refine and optimize the full resume to pass Applicant Tracking Systems while maintaining readability for human recruiters.',
            tools=[web_search_tool, serper_dev_tool],
            backstory='Expert in understanding ATS algorithms and optimizing resumes to increase the chances of getting past initial screening without compromising the resume\'s comprehensiveness.',
            verbose=True,
            allow_delegation=False,
            model_name="gpt-3.5-turbo"
        )
