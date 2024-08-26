import streamlit as st
from main import run
from dotenv import load_dotenv
import os
import asyncio
import tracemalloc
tracemalloc.start()
load_dotenv()
# Simulate fetching profiles based on job description (this is a placeholder)

os.environ["OPENAI_API_KEY"] = os.getenv('OPENAI_API_KEY')
os.environ["OPENAI_MODEL_NAME"] = 'gpt-4o-mini'


def fetch_suitable_profiles(job_description):
    # Mock data for profiles
    crew_output = asyncio.run(run(job_description))
    # This is a very basic filtering; in a real scenario, you'd have complex logic
    # suitable_profiles = [
    #     profile for profile in profiles if job_description.lower() in profile["skills"].lower()
    # ]

    return [crew_output]


# Streamlit app
st.title("AI-Powered Recruitment Tool")
st.write("Enter the job description to find the most suitable profiles:")

# Text input for job description
job_description = st.text_area("Job Description")

if st.button("Find Suitable Profiles"):
    if job_description:
        # Fetch suitable profiles based on the job description
        suitable_profiles = fetch_suitable_profiles(job_description)

        if suitable_profiles:
            st.write("Suitable Profiles Found:")
            for profile in suitable_profiles:
                st.write(f"{profile}")
                # st.write(f"**Skills:** {profile['skills']}")
                # st.write("---")
        else:
            st.write("No suitable profiles found.")
    else:
        st.write("Please enter a job description.")
