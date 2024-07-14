import streamlit as st
from main import run_job_posting_process
from resume_main import run_resume_creation_process
import logging
import markdown

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def main():
    st.title("AI-Powered Job Search Assistant")

    # Sidebar for selecting functionality
    functionality = st.sidebar.selectbox("Choose Functionality", ["Job Posting Creation", "Resume Creation"])

    if functionality == "Job Posting Creation":
        st.header("Agentic Job Posting Creation")
        company_description = st.text_input("Company Description")
        company_domain = st.text_input("Company Domain")
        hiring_needs = st.text_input("Hiring Needs")
        specific_benefits = st.text_input("Specific Benefits")

        if st.button("Create Job Posting"):
            result = run_job_posting_process(company_description, company_domain, hiring_needs, specific_benefits)
            st.markdown(result)

    elif functionality == "Resume Creation":
        st.header("AI-Powered Resume Creation")
        candidate_info = st.text_area("Candidate Information (skills, experiences, education, etc.)")
        job_title = st.text_input("Desired Job Title")
        industry = st.text_input("Industry")
        job_description = st.text_area("Job Description")

        if st.button("Create Resume"):
            with st.spinner("Creating your resume... This may take a few minutes."):
                try:
                    logger.info("Starting resume creation process")
                    resume_markdown = run_resume_creation_process(candidate_info, job_title, industry, job_description)
                    logger.info(f"Resume created successfully. Length: {len(resume_markdown)}")

                    st.subheader("Generated Resume")

                    # Display options
                    display_option = st.radio("Choose display option:", ("Markdown", "Formatted HTML"))

                    if display_option == "Markdown":
                        st.markdown(resume_markdown)
                    else:
                        resume_html = markdown.markdown(resume_markdown)
                        st.components.v1.html(resume_html, height=600, scrolling=True)

                    # Add download buttons
                    st.download_button(
                        label="Download Resume as Markdown",
                        data=resume_markdown,
                        file_name="generated_resume.md",
                        mime="text/markdown"
                    )

                    st.download_button(
                        label="Download Resume as HTML",
                        data=markdown.markdown(resume_markdown),
                        file_name="generated_resume.html",
                        mime="text/html"
                    )
                except Exception as e:
                    logger.error(f"An error occurred during resume creation: {str(e)}", exc_info=True)
                    st.error(f"An error occurred: {str(e)}")
                    st.error("Please check the console for more details.")

if __name__ == "__main__":
    main()
