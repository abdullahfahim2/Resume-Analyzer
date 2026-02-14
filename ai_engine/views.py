import logging
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from resumes.models import Resume
from .models import ResumeAnalysis
from .serializers import ResumeAnalysisSerializer
from .gemini_service import analyze_resume_with_gemini
from .pdf_utils import extract_text_from_pdf
from .utils import clean_resume_text

logger = logging.getLogger(__name__)


class AnalyzeResumeView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        resume_id = request.data.get("resume_id")
        job_description = request.data.get("job_description")

        # 🔹 Basic validation
        if not resume_id or not job_description:
            return Response(
                {"error": "Resume ID and job description are required"},
                status=status.HTTP_400_BAD_REQUEST,
            )

        if len(job_description) < 20:
            return Response(
                {"error": "Job description is too short"},
                status=status.HTTP_400_BAD_REQUEST,
            )

        try:
            resume = Resume.objects.get(id=resume_id, user=request.user)
        except Resume.DoesNotExist:
            return Response(
                {"error": "Resume not found"},
                status=status.HTTP_404_NOT_FOUND,
            )

        try:
            # 🔹 Extract resume text
            resume_text = extract_text_from_pdf(resume.file.path)

            if not resume_text:
                return Response(
                    {"error": "Could not extract text from this PDF"},
                    status=status.HTTP_400_BAD_REQUEST,
                )

            # 🔹 Clean and limit text (token control)
            resume_text = clean_resume_text(resume_text)

            # 🔹 AI analysis
            result = analyze_resume_with_gemini(
                resume_text, job_description
            )

            # 🔹 Save result
            analysis = ResumeAnalysis.objects.create(
                resume=resume,
                job_description=job_description,
                match_score=result.get("match_score", 0),
                missing_skills=result.get("missing_skills", []),
                strengths=result.get("strengths", []),
                suggestions=result.get(
                    "improvement_suggestions", []
                ),
            )

            serializer = ResumeAnalysisSerializer(analysis)
            return Response(serializer.data)

        except Exception as e:
            logger.error(f"AI Resume Analysis Failed: {str(e)}")

            return Response(
                {"error": "AI analysis failed. Please try again."},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR,
            )


# 🔥 BONUS: Analysis history API
from rest_framework import generics


class AnalysisHistoryView(generics.ListAPIView):
    serializer_class = ResumeAnalysisSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return ResumeAnalysis.objects.filter(
            resume__user=self.request.user
        ).order_by("-created_at")
