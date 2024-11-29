from django.contrib.auth.models import User
from django.db import models
from ..english_test.models import *


class TestResult(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    test = models.ForeignKey(TestModel, on_delete=models.CASCADE)
    score = models.IntegerField(default=0)
    completed_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.test.title} ({self.score} баллов)"

    class Meta:
        verbose_name = "Результат теста"
        verbose_name_plural = "Результаты тестов"


class UserAnswer(models.Model):
    test_result = models.ForeignKey(
        TestResult,
        related_name='answers',
        on_delete=models.CASCADE
    )
    question = models.ForeignKey(
        QuestionModel,
        on_delete=models.CASCADE
    )
    user_answer = models.CharField(
        max_length=1,
        choices=[('A', 'Вариант A'), ('B', 'Вариант B'), ('C', 'Вариант C'), ('D', 'Вариант D')],
        verbose_name='Ответ пользователя',
        help_text='Введите выбранный вариант ответа (A, B, C или D).'
    )

    def __str__(self):
        return f"Ответ на вопрос {self.question.title} от {self.test_result.user.username}"

    class Meta:
        verbose_name = "Ответ пользователя"
        verbose_name_plural = "Ответы пользователей"