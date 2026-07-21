import re

SKILLS_DB = {
    "python": ["python"],
    "java": ["java"],
    "sql": ["sql"],
    "mysql": ["mysql", "my sql"],
    "machine learning": ["machine learning", "ml"],
    "deep learning": ["deep learning"],
    "nlp": ["nlp", "natural language processing"],
    "data analysis": ["data analysis", "data analytics", "data analyst"],
    "data visualization": ["data visualization", "visualization"],
    "power bi": ["power bi", "powerbi"],
    "tableau": ["tableau"],
    "excel": ["excel", "microsoft excel"],
    "html": ["html"],
    "css": ["css"],
    "javascript": ["javascript", "js"],
    "react": ["react", "reactjs", "react.js"],
    "node.js": ["node", "nodejs", "node.js"],
    "fastapi": ["fastapi", "fast api"],
    "flask": ["flask"],
    "django": ["django"],
    "git": ["git"],
    "github": ["github", "git hub"],
    "communication": ["communication", "communicating"],
    "teamwork": ["teamwork", "team work", "collaboration"],
    "problem solving": ["problem solving", "problem-solving"],
    "leadership": ["leadership", "leading", "team lead"],
    "analytical thinking": ["analytical thinking", "analysis"],
    "adaptability": ["adaptability", "adaptable"],
    "pandas": ["pandas"],
    "numpy": ["numpy"],
    "scikit learn": ["scikit learn", "sklearn"]
}

def extract_skills(text):
    text = text.lower()
    found_skills = []

    for main_skill, variations in SKILLS_DB.items():
        for variation in variations:
            pattern = r'\b' + re.escape(variation) + r'\b'

            if re.search(pattern, text):
                found_skills.append(main_skill)
                break

    return list(set(found_skills))