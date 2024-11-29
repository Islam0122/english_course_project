from rest_framework import generics, status
from rest_framework.generics import ListCreateAPIView, RetrieveAPIView
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import TestResult, UserAnswer
from .serializers import *


class TestResultListCreateView(ListCreateAPIView):
    queryset = TestResult.objects.prefetch_related('answers__question')
    serializer_class = TestResultWithAnswersSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class TestResultDetailView(RetrieveAPIView):
    queryset = TestResult.objects.prefetch_related('answers__question')
    serializer_class = TestResultWithAnswersSerializer
