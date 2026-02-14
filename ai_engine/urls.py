from django.urls import path
from .views import AnalyzeResumeView, AnalysisHistoryView

urlpatterns = [
    path("analyze-resume/", AnalyzeResumeView.as_view()),
    path("analysis-history/", AnalysisHistoryView.as_view()),
]
