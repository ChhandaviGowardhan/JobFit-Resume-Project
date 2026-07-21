import streamlit as st
from utils.pdf_extractor import extract_text_from_pdf
from utils.text_cleaner import clean_text
from utils.matcher import calculate_match
from utils.skills_extractor import extract_skills

st.set_page_config(
    page_title="Resume Screening Tool",
    page_icon="📄",
    layout="wide"
)

st.title("📄 Resume Screening and Job Matching Tool")
st.write("Upload a resume and compare it with a job description.")

uploaded_file = st.file_uploader("Upload Resume PDF", type=["pdf"])

job_description = st.text_area(
    "Paste Job Description Here",
    height=200
)

# Button
calculate = st.button("🔍 Calculate Match Score", type="primary")

if calculate:

    if uploaded_file is None:
        st.warning("Please upload a resume.")
        st.stop()

    if not job_description.strip():
        st.warning("Please paste a job description.")
        st.stop()

    extracted_text = extract_text_from_pdf(uploaded_file)

    cleaned_resume = clean_text(extracted_text)
    cleaned_job_description = clean_text(job_description)

    resume_skills = extract_skills(cleaned_resume)
    job_skills = extract_skills(cleaned_job_description)

    matching_skills = sorted(list(set(resume_skills) & set(job_skills)))
    missing_skills = sorted(list(set(job_skills) - set(resume_skills)))
    extra_skills = sorted(list(set(resume_skills) - set(job_skills)))

    match_score = calculate_match(
        cleaned_resume,
        cleaned_job_description,
        resume_skills,
        job_skills
    )

    st.divider()

    st.subheader("Resume Match Score")

    if match_score >= 80:
        st.success(f"Excellent Match: {match_score}%")
    elif match_score >= 60:
        st.warning(f"Good Match: {match_score}%")
    else:
        st.error(f"Low Match: {match_score}%")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.subheader("✅ Matching Skills")
        if matching_skills:
            for skill in matching_skills:
                st.success(skill)
        else:
            st.write("No matching skills found.")

    with col2:
        st.subheader("❌ Missing Skills")
        if missing_skills:
            for skill in missing_skills:
                st.error(skill)
        else:
            st.write("No missing skills.")

    with col3:
        st.subheader("ℹ️ Extra Skills")
        if extra_skills:
            for skill in extra_skills:
                st.info(skill)
        else:
            st.write("No extra skills.")