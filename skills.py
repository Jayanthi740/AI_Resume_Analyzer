# skills.py

def extract_skills(text):
    """
    Extract technical skills from resume text
    """

    skill_list = [
        "python",
        "sql",
        "html",
        "css",
        "javascript",
        "machine learning",
        "django",
        "git",
        "java",
        "c++"
    ]

    found_skills = []

    for skill in skill_list:
        if skill in text.lower():
            found_skills.append(skill)

    return found_skills