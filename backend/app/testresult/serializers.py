from rest_framework import serializers
from .models import TestResult, UserAnswer
from django.contrib.auth.models import User


# Сериализатор для модели TestResult
class TestResultSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField()  # Для вывода имени пользователя
    test = serializers.StringRelatedField()  # Для вывода названия теста

    class Meta:
        model = TestResult
        fields = ['user', 'test', 'score', 'completed_at']


# Сериализатор для модели UserAnswer
class UserAnswerSerializer(serializers.ModelSerializer):
    test_result = TestResultSerializer()  # Вложенный сериализатор для TestResult
    question = serializers.StringRelatedField()  # Для вывода вопроса
    user_answer = serializers.CharField(max_length=1)  # Ответ пользователя

    class Meta:
        model = UserAnswer
        fields = ['test_result', 'question', 'user_answer']
