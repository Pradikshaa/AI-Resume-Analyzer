
from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI, UploadFile, File, Form
from analyzer import extract_skills
from ats import calculate_ats
from similarity import calculate_similarity
from suggestions import generate_suggestions
import PyPDF2
import io

app = FastAPI()

# CORS Middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Home Route
@app.get("/")
def home():
    return {"message": "AI Resume Analyzer Backend Running"}

# Upload Route
@app.post("/upload")
async def upload_resume(
    file: UploadFile = File(...),
    job_description: str = Form(...)
):
    # Read uploaded PDF
    contents = await file.read()
    pdf_reader = PyPDF2.PdfReader(io.BytesIO(contents))

    text = ""

    # Extract text from all pages
    for page in pdf_reader.pages:
        extracted = page.extract_text()
        if extracted:
            text += extracted

    # Extract skills from resume
    skills = extract_skills(text)

    # Required skills for ATS scoring
    required_skills = [
        "python",
        "sql",
        "machine learning",
        "deep learning",
        "nlp"
    ]

    # Calculate ATS Score
    score, matched, missing = calculate_ats(skills, required_skills)

    # Generate Suggestions
    suggestions = generate_suggestions(missing, score)

    # Calculate Similarity Score with Job Description
    similarity_score = calculate_similarity(text, job_description)

    return {
        "filename": file.filename,
        "skills": skills,
        "ats_score": score,
        "matched_skills": matched,
        "missing_skills": missing,
        "similarity_score": similarity_score,
        "suggestions": suggestions
    }
