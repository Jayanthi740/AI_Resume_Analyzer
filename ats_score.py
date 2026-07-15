# ats_score.py


def calculate_ats_score(resume_text, resume_skills, job_skills):
    """
    Advanced ATS Score Calculation

    Weightage:
    Skills       : 40%
    Projects     : 20%
    Education    : 20%
    Experience   : 20%
    """


    # Skills Score (40%)

    if len(job_skills) > 0:

        matched_skills = 0

        for skill in job_skills:
            if skill.lower() in resume_skills:
                matched_skills += 1

        skills_score = (matched_skills / len(job_skills)) * 100

    else:
        skills_score = 0



    # Projects Score (20%)

    project_keywords = [
        "project",
        "developed",
        "created",
        "built",
        "application"
    ]

    project_count = 0

    for word in project_keywords:
        if word in resume_text:
            project_count += 1


    projects_score = (project_count / len(project_keywords)) * 100



    # Education Score (20%)

    education_keywords = [
        "b.tech",
        "btech",
        "bachelor",
        "degree",
        "computer science",
        "cse",
        "university",
        "college",
        "cgpa"
    ]

    education_count = 0

    for word in education_keywords:
        if word in resume_text:
            education_count += 1


    education_score = (
        education_count / len(education_keywords)
    ) * 100



    # Experience Score (20%)

    experience_keywords = [
        "internship",
        "experience",
        "training",
        "worked",
        "certificate",
        "certification",
        "project"
    ]

    experience_count = 0

    for word in experience_keywords:
        if word in resume_text:
            experience_count += 1


    experience_score = (
        experience_count / len(experience_keywords)
    ) * 100



    # Final Score

    final_score = (
        skills_score * 0.40 +
        projects_score * 0.20 +
        education_score * 0.20 +
        experience_score * 0.20
    )


    score_details = {

        "Skills Score": round(skills_score,2),

        "Projects Score": round(projects_score,2),

        "Education Score": round(education_score,2),

        "Experience Score": round(experience_score,2)

    }


    return round(final_score,2), score_details