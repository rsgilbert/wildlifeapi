from .models import Category, Animal, Question, Choice
from .serializers import CategorySerializer, QuestionSerializer
from rest_framework import viewsets




class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class QuestionViewSet(viewsets.ModelViewSet):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer


