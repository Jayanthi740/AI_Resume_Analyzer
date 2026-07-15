# suggestions.py


def generate_suggestions(missing_skills):
    """
    Generate suggestions based on missing skills
    """

    suggestions = []

    for skill in missing_skills:
        suggestions.append(
            f"Improve your resume by adding {skill} skill"
        )

    if len(suggestions) == 0:
        suggestions.append(
            "Your resume matches the required skills well"
        )

    return suggestions