def resume_analysis_prompt(resume_text, job_description):
    return f"""
You are an expert HR and technical recruiter.

Analyze the following resume against the job description.

Return ONLY valid JSON. No explanation, no extra text.

JSON format:
{{
  "match_score": 0-100,
  "missing_skills": [],
  "strengths": [],
  "improvement_suggestions": []
}}

Rules:
1. Score realistically.
2. Focus on technical skills and experience.
3. Give 3–6 items in each list.

Resume:
{resume_text[:8000]}

Job Description:
{job_description[:2000]}
"""
