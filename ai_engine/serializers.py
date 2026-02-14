from rest_framework import serializers
from .models import ResumeAnalysis


class ResumeAnalysisSerializer(serializers.ModelSerializer):
    # 🔹 Extra readable fields for frontend
    resume_id = serializers.IntegerField(source="resume.id", read_only=True)
    resume_file = serializers.CharField(
        source="resume.file.url",
        read_only=True
    )

    class Meta:
        model = ResumeAnalysis
        fields = [
            "id",
            "resume_id",
            "resume_file",
            "job_description",
            "match_score",
            "missing_skills",
            "strengths",
            "suggestions",
            "ai_model",
            "status",
            "error_message",
            "created_at",
            "updated_at",
        ]

        # 🔹 Security: user cannot modify AI results
        read_only_fields = [
            "id",
            "resume_id",
            "resume_file",
            "match_score",
            "missing_skills",
            "strengths",
            "suggestions",
            "ai_model",
            "status",
            "error_message",
            "created_at",
            "updated_at",
        ]
