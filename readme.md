```markdown
# AI Resume Analyzer

![Python](https://img.shields.io/badge/python-3.11-blue) 
![Django](https://img.shields.io/badge/django-5.2-green) 
![DRF](https://img.shields.io/badge/DRF-3.15-blueviolet) 
![Google GenAI](https://img.shields.io/badge/Google%20GenAI-AI-orange) 

---

## About This Project

**AI Resume Analyzer** is a Django + DRF project that allows users to:

- Upload resumes (PDFs) securely
- Analyze resumes using **Google Generative AI (GenAI)**
- Compare resumes with job descriptions
- Get structured insights: match score, strengths, missing skills, and improvement suggestions
- Manage resumes and AI analysis history

This project is **portfolio-ready**, showcasing:

- Django REST Framework
- JWT Authentication
- Google GenAI integration
- Interactive Swagger / Redoc API documentation
- Secure environment variable management with `python-decouple`

---

## Features

- User registration and authentication (JWT)
- Upload multiple resumes (PDF)
- Automatic text extraction from PDF
- AI-powered resume analysis
- Save AI results in structured JSON
- Interactive Swagger UI documentation
- Secure configuration using `.env` for API keys

---



## API Endpoints

| Endpoint | Method | Description | Auth |
|----------|--------|-------------|------|
| `/api/register/` | POST | User registration | No |
| `/api/token/` | POST | JWT access & refresh token | No |
| `/api/upload-resume/` | POST | Upload PDF resume | Yes (Bearer) |
| `/api/analyze-resume/` | POST | Analyze resume with job description | Yes (Bearer) |
| `/api/analysis-history/` | GET | List past resume analyses | Yes (Bearer) |
| `/api/docs/` | GET | Swagger interactive docs | No |
| `/api/redoc/` | GET | Redoc clean API docs | No |

---

### Example: Analyze Resume API

**Request:**

```http
POST /api/analyze-resume/
Authorization: Bearer <ACCESS_TOKEN>
Content-Type: application/json

{
  "resume_id": 1,
  "job_description": "Looking for Django developer with REST API, AWS, Docker"
}
````

**Response:**

```json
{
  "id": 1,
  "resume_id": 1,
  "resume_file": "/media/resumes/mycv.pdf",
  "job_description": "Looking for Django developer with REST API, AWS, Docker",
  "match_score": 85,
  "missing_skills": ["AWS"],
  "strengths": ["Django", "Python"],
  "suggestions": ["Add cloud experience"],
  "ai_model": "gemini-1.5-flash",
  "status": "completed",
  "error_message": null,
  "created_at": "2026-02-14T11:35:00Z",
  "updated_at": "2026-02-14T11:35:00Z"
}
```

---

## Setup Instructions

1. **Clone the repository:**

```bash
git clone https://github.com/yourusername/ai-resume-analyzer.git
cd ai-resume-analyzer
```

2. **Create a virtual environment:**

```bash
python -m venv env
source env/bin/activate  # Linux/macOS
env\Scripts\activate     # Windows
```

3. **Install dependencies:**

```bash
pip install -r requirements.txt
```

4. **Add `.env` file** in the project root:

```text
DEBUG=True
SECRET_KEY=your_django_secret_key
GOOGLE_API_KEY=your_google_genai_api_key
```

> ⚠️ Never commit `.env` to GitHub

5. **Run migrations:**

```bash
python manage.py migrate
```

6. **Run the server:**

```bash
python manage.py runserver
```

7. **Access API documentation:**

* Swagger UI: `http://127.0.0.1:8000/api/docs/`
* Redoc: `http://127.0.0.1:8000/api/redoc/`

---

## Environment & Security

* **API keys and secrets** are stored in `.env` using **python-decouple**.
* JWT authentication secures all user-specific APIs.
* `.env` file should never be uploaded to GitHub.

---

## Future Enhancements

* Resume rewriting AI (generate improved resumes)
* Skill extraction & tagging
* Async AI processing with Celery + Redis
* Frontend dashboard (React / Vue)
* Deployment using Docker + cloud platforms

---
