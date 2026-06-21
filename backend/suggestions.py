
def generate_suggestions(missing_skills, ats_score):
    suggestions = []

    if "deep learning" in missing_skills:
        suggestions.append("Add Deep Learning projects to strengthen your profile.")

    if "nlp" in missing_skills:
        suggestions.append("Add NLP projects or certifications.")

    if "sql" in missing_skills:
        suggestions.append("Improve SQL skills for better data handling roles.")

    if "machine learning" in missing_skills:
        suggestions.append("Work on more Machine Learning projects.")

    if ats_score < 70:
        suggestions.append("Improve resume by adding more relevant skills and projects.")

    if ats_score >= 80:
        suggestions.append("Strong profile! Minor improvements can make it even better.")

    return suggestions
