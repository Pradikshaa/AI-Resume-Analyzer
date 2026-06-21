
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def calculate_similarity(resume_text, jd_text):
    texts = [resume_text, jd_text]

    vectorizer = TfidfVectorizer()
    vectors = vectorizer.fit_transform(texts)

    similarity = cosine_similarity(vectors)[0][1]

    return round(similarity * 100, 2)