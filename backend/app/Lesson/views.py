from rest_framework.generics import ListAPIView, RetrieveAPIView
from .models import Level, Category
from .serializers import LevelSerializer, CategorySerializer


class LevelListView(ListAPIView):
    queryset = Level.objects.all()
    serializer_class = LevelSerializer


class CategoryListView(ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class LevelDetailView(RetrieveAPIView):
    queryset = Level.objects.all()
    serializer_class = LevelSerializer


class CategoryDetailView(RetrieveAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
