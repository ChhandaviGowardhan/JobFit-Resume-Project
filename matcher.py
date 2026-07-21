from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def calculate_match(resume_text, job_description, resume_skills, job_skills):

    documents = [resume_text, job_description]

    tfidf_vectorizer = TfidfVectorizer(ngram_range=(1, 2))

    tfidf_matrix = tfidf_vectorizer.fit_transform(documents)

    similarity_score = cosine_similarity(tfidf_matrix[0:1], tfidf_matrix[1:2])

    tfidf_score = similarity_score[0][0] * 100

    matched_skills = len(set(resume_skills) & set(job_skills))

    if len(job_skills) > 0:
        skill_score = (matched_skills / len(job_skills)) * 100
    else:
        skill_score = 0

    final_score = (0.3 * tfidf_score) + (0.7 * skill_score)

    return round(final_score, 2)