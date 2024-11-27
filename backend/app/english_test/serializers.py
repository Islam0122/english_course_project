from rest_framework import serializers
from .models import TestModel, QuestionModel


class QuestionModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = QuestionModel
        fields = ('id', 'test', 'title', 'option_a', 'option_b', 'option_c', 'option_d', 'correct_option', 'created_at',
                  'updated_at')


class TestModelSerializer(serializers.ModelSerializer):
    # Включаем вопросы для теста
    questions = QuestionModelSerializer(many=True, read_only=True)

    class Meta:
        model = TestModel
        fields = ('id', 'title', 'description', 'created_at', 'updated_at', 'questions')
