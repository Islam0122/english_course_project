from rest_framework import generics
from .models import TestResult, UserAnswer
from .serializers import TestResultSerializer, UserAnswerSerializer


# Представление для получения списка TestResult
class TestResultListView(generics.ListCreateAPIView):
    queryset = TestResult.objects.all()
    serializer_class = TestResultSerializer


# Представление для получения списка UserAnswer
class UserAnswerListView(generics.ListCreateAPIView):
    queryset = UserAnswer.objects.all()
    serializer_class = UserAnswerSerializer