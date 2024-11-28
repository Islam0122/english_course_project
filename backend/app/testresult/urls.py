from django.urls import path
from .views import TestResultListView, UserAnswerListView

urlpatterns = [
    path('test-results/', TestResultListView.as_view(), name='test-result-list'),
    path('user-answers/', UserAnswerListView.as_view(), name='user-answer-list'),
]