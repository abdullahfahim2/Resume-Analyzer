from google import genai
from django.conf import settings
import json
from .prompts import resume_analysis_prompt


# 🔹 Create GenAI client
client = genai.Client(api_key=settings.GOOGLE_API_KEY)


def analyze_resume_with_gemini(resume_text, job_description):
    prompt = resume_analysis_prompt(resume_text, job_description)

    try:
        # 🔹 Generate AI response
        response = client.models.generate_content(
            model="gemini-2.0-flash",
            contents=prompt,
        )

        text = response.text.strip()

        # 🔹 Remove markdown formatting if Gemini returns it
        if text.startswith("```"):
            text = text.replace("```json", "").replace("```", "")

        return json.loads(text)

    except Exception as e:
        return {
            "match_score": 0,
            "missing_skills": [],
            "strengths": [],
            "improvement_suggestions": [f"AI error: {str(e)}"],
        }
