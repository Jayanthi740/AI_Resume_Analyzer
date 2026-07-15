# missing_skills.py


def find_missing_skills(resume_skills, job_skills):
    """
    Find skills required by job but missing in resume
    """

    missing = []

    for skill in job_skills:
        if skill.lower() not in resume_skills:
            missing.append(skill)

    return missing