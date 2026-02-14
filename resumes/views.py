from rest_framework import generics, permissions
from .models import Resume
from .serializers import ResumeUploadSerializer

class ResumeUploadView(generics.CreateAPIView):
    serializer_class = ResumeUploadSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
