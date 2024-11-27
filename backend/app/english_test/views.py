from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import TestModel, QuestionModel
from .serializers import TestModelSerializer, QuestionModelSerializer


class TestListView(APIView):
    def get(self, request):
        tests = TestModel.objects.all()
        serializer = TestModelSerializer(tests, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class TestDetailView(APIView):
    def get(self, request, pk):
        try:
            test = TestModel.objects.get(pk=pk)
        except TestModel.DoesNotExist:
            return Response({'detail': 'Not found.'}, status=status.HTTP_404_NOT_FOUND)
        serializer = TestModelSerializer(test)
        return Response(serializer.data, status=status.HTTP_200_OK)


class QuestionListView(APIView):
    def get(self, request, test_id):
        questions = QuestionModel.objects.filter(test_id=test_id)
        serializer = QuestionModelSerializer(questions, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class QuestionDetailView(APIView):
    def get(self, request, pk):
        try:
            question = QuestionModel.objects.get(pk=pk)
        except QuestionModel.DoesNotExist:
            return Response({'detail': 'Not found.'}, status=status.HTTP_404_NOT_FOUND)
        serializer = QuestionModelSerializer(question)
        return Response(serializer.data, status=status.HTTP_200_OK)

