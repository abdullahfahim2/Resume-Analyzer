from django.db import models
from resumes.models import Resume


class ResumeAnalysis(models.Model):
    resume = models.ForeignKey(
        Resume,
        on_delete=models.CASCADE,
        related_name="analyses"
    )

    # 🔹 Job information
    job_description = models.TextField()

    # 🔹 AI results
    match_score = models.PositiveIntegerField(default=0)
    missing_skills = models.JSONField(default=list)
    strengths = models.JSONField(default=list)
    suggestions = models.JSONField(default=list)

    # 🔹 Metadata
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # 🔹 Optional future scalability
    ai_model = models.CharField(
        max_length=50,
        default="gemini-1.5-flash"
    )

    status = models.CharField(
        max_length=20,
        default="completed",
        choices=[
            ("pending", "Pending"),
            ("completed", "Completed"),
            ("failed", "Failed"),
        ],
    )

    error_message = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"Analysis {self.id} - Resume {self.resume.id}"
