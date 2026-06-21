def calculate_ats(resume_skills, required_skills):
    matched = []
    missing = []

    for skill in required_skills:
        if skill.lower() in resume_skills:
            matched.append(skill)
        else:
            missing.append(skill)

    score = int((len(matched) / len(required_skills)) * 100)

    return score, matched, missing