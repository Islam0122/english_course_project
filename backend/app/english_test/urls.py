from django.urls import path
from .views import TestListView, QuestionListView, TestDetailView, QuestionDetailView

urlpatterns = [
    # Получить все тесты
    path('tests/', TestListView.as_view(), name='test-list'),

    # Получить один тест по ID
    path('tests/<int:pk>/', TestDetailView.as_view(), name='test-detail'),

    # Получить все вопросы для теста
    path('tests/<int:test_id>/questions/', QuestionListView.as_view(), name='question-list'),

    # Получить вопрос по ID
    path('questions/<int:pk>/', QuestionDetailView.as_view(), name='question-detail'),
]