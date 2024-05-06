import streamlit as st
from main import run_job_posting_process
from agents import Agents
from tasks import Tasks

def main():
    st.title("Agentic Job Posting Creation")

    company_description = st.text_input("Company Description")
    company_domain = st.text_input("Company Domain")
    hiring_needs = st.text_input("Hiring Needs")
    specific_benefits = st.text_input("Specific Benefits")

    if st.button("Create Job Posting using AI Agents"):
        result = run_job_posting_process(company_description, company_domain, hiring_needs, specific_benefits)
        st.markdown(result)

if __name__ == "__main__":
    main()
