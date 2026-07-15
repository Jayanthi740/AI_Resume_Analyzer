import streamlit as st

from job_parser import extract_job_skills
from parser import extract_text_from_pdf
from skills import extract_skills
from ats_score import calculate_ats_score
from missing_skills import find_missing_skills
from suggestions import generate_suggestions
from utils import clean_text


st.title("🤖 AI Resume Analyzer")


uploaded_file = st.file_uploader(
    "Upload your Resume PDF",
    type="pdf"
)


job_description = st.text_area(
    "Paste Job Description"
)


if uploaded_file is not None and job_description:

    # Save uploaded PDF
    with open("uploaded_resume.pdf", "wb") as f:
        f.write(uploaded_file.getbuffer())

    # Extract resume text
    resume_text = extract_text_from_pdf("uploaded_resume.pdf")

    # Clean resume text
    cleaned_text = clean_text(resume_text)

    # Extract resume skills
    resume_skills = extract_skills(cleaned_text)

    # Extract job skills
    job_skills = extract_job_skills(job_description)

    # Calculate ATS Score
    ats_score, score_details = calculate_ats_score(
        cleaned_text,
        resume_skills,
        job_skills
    )

    # Find missing skills
    missing_skills = find_missing_skills(
        resume_skills,
        job_skills
    )

    # Generate suggestions
    suggestions = generate_suggestions(
        missing_skills
    )

    # Display Results
    st.subheader("📌 Resume Skills")
    st.write(resume_skills)

    st.subheader("📌 Job Required Skills")
    st.write(job_skills)

    st.subheader("📊 Overall ATS Score")
    st.success(f"{ats_score}%")

    st.subheader("📈 Score Breakdown")

    for section, score in score_details.items():
        st.write(f"**{section}:** {score}%")

    st.subheader("❌ Missing Skills")

    if missing_skills:
        st.write(missing_skills)
    else:
        st.success("No missing skills 🎉")

    st.subheader("💡 Suggestions")

    for suggestion in suggestions:
        st.write("✔", suggestion)