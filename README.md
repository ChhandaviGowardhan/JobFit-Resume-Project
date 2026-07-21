# 📄 JobFit – Resume Screening and Job Matching Tool

An **NLP-powered Resume Screening and Job Matching Tool** built with **Python** and **Streamlit** that automates resume evaluation by comparing a candidate's resume against a job description. The application extracts text from PDF resumes, preprocesses unstructured textual data, identifies technical and soft skills, and computes a compatibility score using **TF-IDF Vectorization**, **Cosine Similarity**, and **rule-based skill matching**.

---

## 📌 Overview

Recruiters often spend significant time manually reviewing resumes to determine whether candidates meet job requirements. This project streamlines the initial screening process by automatically analyzing resumes and measuring how well they align with a given job description.

The application performs the following tasks:

- Extracts text from PDF resumes
- Cleans and preprocesses textual data using NLP techniques
- Identifies technical and soft skills from resumes and job descriptions
- Computes semantic similarity using TF-IDF and Cosine Similarity
- Calculates a weighted resume-job compatibility score
- Displays matching, missing, and additional skills through an interactive dashboard

---

## ✨ Features

- 📄 Upload resume in PDF format
- 🧹 Automatic text preprocessing using NLTK
- 🔍 Rule-based technical & soft skill extraction
- 📊 Resume-job compatibility scoring
- 🤖 TF-IDF based semantic similarity analysis
- 📈 Weighted scoring algorithm
- ✅ Matching Skills Detection
- ❌ Missing Skills Identification
- ➕ Additional Skills Identification
- 💻 Interactive Streamlit web interface

---

## 🛠️ Tech Stack

| Category | Technologies |
|----------|--------------|
| Programming Language | Python |
| Web Framework | Streamlit |
| Natural Language Processing | NLTK |
| Machine Learning | Scikit-learn |
| PDF Processing | PyPDF2 |
| Pattern Matching | Regular Expressions (Regex) |

---

## 📂 Project Structure

```text
JobFit/
│
├── Screenshots/
│   ├── 1.jpg
│   └── Demo.mp4
│
├── data/
│   ├── Sample JD.pdf
│   └── Sample Resume.pdf
│
├── utils/
│   ├── matcher.py
│   ├── pdf_extractor.py
│   ├── skills_extractor.py
│   └── text_cleaner.py
│
├── .gitignore
├── README.md
├── app.py
└── requirements.txt
```

---

# ⚙️ How It Works

The application follows a multi-stage NLP pipeline.

```text
Resume PDF
      │
      ▼
Text Extraction (PyPDF2)
      │
      ▼
Text Cleaning (NLTK)
      │
      ▼
Skill Extraction (Regex)
      │
      ▼
Job Description Processing
      │
      ▼
TF-IDF Vectorization
      │
      ▼
Cosine Similarity
      │
      ▼
Skill Matching
      │
      ▼
Weighted Match Score
      │
      ▼
Interactive Results
```

---

# 🧠 Working Pipeline

## 1. Resume Upload

The user uploads a resume in PDF format through the Streamlit interface.

---

## 2. PDF Text Extraction

The uploaded resume is processed using **PyPDF2** to extract textual content from each page.

---

## 3. Text Preprocessing

The extracted text is cleaned using NLP techniques including:

- Lowercase conversion
- Removal of punctuation and special characters
- Tokenization
- Stop-word removal
- Noise reduction

This preprocessing ensures better text representation for similarity analysis.

---

## 4. Skill Extraction

A predefined skills database is used to identify technical and soft skills from both the resume and the job description.

Examples include:

- Python
- SQL
- Machine Learning
- FastAPI
- Power BI
- Git
- Communication
- Teamwork
- Leadership

Regex-based pattern matching is used to recognize different variations of the same skill.

Example:

```
React
ReactJS
React.js
```

are all mapped to

```
React
```

---

## 5. Semantic Similarity

The cleaned resume and job description are transformed into numerical vectors using **TF-IDF Vectorization**.

Cosine Similarity is then computed to determine how semantically similar the documents are.

This helps evaluate overall textual relevance rather than relying solely on keyword matching.

---

## 6. Skill Matching

The application compares extracted skills from both documents to determine:

- Matching Skills
- Missing Skills
- Additional Skills

This provides actionable feedback for improving resume quality.

---

## 7. Resume Match Score

The final compatibility score is calculated using a weighted formula:

```
Final Score

= (30% × TF-IDF Similarity)

+ (70% × Skill Match Score)
```

This gives greater importance to required skills while also considering semantic similarity.

---

# 📊 Output

The application displays:

- Overall Resume Match Score
- Matching Skills
- Missing Skills
- Additional Skills
- Extracted Resume Text
- Cleaned Resume Text

---

# 🚀 Installation

## Clone the repository

```bash
git clone https://github.com/your-username/JobFit.git
```

Navigate into the project

```bash
cd JobFit
```

---

## Create a Virtual Environment

Windows

```bash
python -m venv venv
```

Activate it

Command Prompt

```bash
venv\Scripts\activate
```

PowerShell

```powershell
.\venv\Scripts\Activate.ps1
```

---

## Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Run the Application

```bash
streamlit run app.py
```

The application will launch at

```
http://localhost:8501
```

---

# 📁 Sample Files

The repository includes sample files for testing.

```
data/
├── Sample Resume.pdf
└── Sample JD.pdf
```

Simply upload the sample resume and paste the sample job description to test the application.

---

# 📷 Screenshots

Project screenshots and demo video are available in the `Screenshots` folder.

```
Screenshots/
├── 1.jpg
└── Demo.mp4
```

---

# 🧩 Core Modules

### pdf_extractor.py

- Reads PDF resumes
- Extracts text page by page using PyPDF2

---

### text_cleaner.py

Responsible for text preprocessing.

Functions include:

- Lowercasing
- Tokenization
- Stop-word removal
- Special character removal

---

### skills_extractor.py

Implements rule-based skill extraction using:

- Regex
- Custom skills database

Returns unique skills detected within the document.

---

### matcher.py

Calculates resume-job compatibility using:

- TF-IDF Vectorization
- Cosine Similarity
- Weighted scoring algorithm

---

### app.py

Main Streamlit application responsible for:

- User Interface
- File Upload
- Processing Pipeline
- Displaying Results

---

# 📈 Future Improvements

Some possible enhancements include:

- OCR support for scanned PDF resumes
- Named Entity Recognition (NER) using spaCy
- Transformer-based embeddings using Sentence-BERT
- Automatic skill ontology expansion
- Resume ranking for multiple candidates
- AI-generated resume improvement suggestions
- Job recommendation system
- ATS score estimation
- Export results to PDF or Excel
- Integration with job portals and LinkedIn

---

# ⚠️ Limitations

- Supports only text-based PDF resumes.
- Skill extraction relies on a predefined skills database.
- Does not understand contextual synonyms beyond configured variations.
- Matching algorithm uses fixed weighting (30% semantic similarity, 70% skill matching).
- Processes one resume and one job description at a time.

---

# 🎯 Learning Outcomes

This project demonstrates practical implementation of:

- Natural Language Processing (NLP)
- Text Preprocessing
- Information Retrieval
- PDF Processing
- Feature Extraction
- TF-IDF Vectorization
- Cosine Similarity
- Rule-based Information Extraction
- Streamlit Application Development
- Machine Learning Workflow Integration

---

# 👨‍💻 Author

**Chhandavi Gowardhan**

If you found this project useful, feel free to ⭐ the repository.
