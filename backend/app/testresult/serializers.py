from rest_framework import serializers
from .models import TestResult, UserAnswer
from django.contrib.auth.models import User


class UserAnswerNestedSerializer(serializers.ModelSerializer):
    question_text = serializers.CharField(source='question.title')  # Текст вопроса
    correct_option = serializers.CharField(source='question.correct_option')  # Правильный вариант из `QuestionModel`

    class Meta:
        model = UserAnswer
        fields = ['id', 'question_text', 'user_answer', 'correct_option']


class TestResultWithAnswersSerializer(serializers.ModelSerializer):
    username = serializers.CharField(source='user.username')
    test_title = serializers.CharField(source='test.title')
    completed_at = serializers.DateTimeField(format='%Y-%m-%d %H:%M:%S')
    answers = UserAnswerNestedSerializer(many=True, read_only=True)

    class Meta:
        model = TestResult
        fields = ['id', 'username', 'test_title', 'score', 'completed_at', 'answers']
