from django.urls import path
from .views import LevelListView, LevelDetailView, CategoryListView, CategoryDetailView

urlpatterns = [
    path('levels/', LevelListView.as_view(), name='level-list'),  # Список уровней
    path('levels/<int:pk>/', LevelDetailView.as_view(), name='level-detail'),  # Детали уровня
    path('categories/', CategoryListView.as_view(), name='category-list'),  # Список категорий
    path('categories/<int:pk>/', CategoryDetailView.as_view(), name='category-detail'),  # Детали категории
]