# job_parser.py


def extract_job_skills(job_description):

    skill_list = [
        "python",
        "sql",
        "html",
        "css",
        "javascript",
        "machine learning",
        "django",
        "java",
        "c++",
        "react",
        "nodejs",
        "aws",
        "git"
    ]

    found_skills = []

    text = job_description.lower()

    for skill in skill_list:
        if skill in text:
            found_skills.append(skill)

    return found_skills