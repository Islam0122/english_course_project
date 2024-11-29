from django.urls import path
from .views import *

urlpatterns = [
    path('test-results/', TestResultListCreateView.as_view(), name='test-result-list-create'),
    path('test-results/<int:pk>/', TestResultDetailView.as_view(), name='test-result-detail'),
]