from rest_framework import serializers
from .models import Category, Animal, Question, Choice


class CategorySerializer(serializers.HyperlinkedModelSerializer):
    id = serializers.ReadOnlyField()

    class Meta:
        model = Category
        # fields = '__all__'
        exclude = ['url']


class QuestionSerializer(serializers.HyperlinkedModelSerializer):
    category_id = serializers.CharField(source='category.id')
    
    class Meta:
        model = Question
        fields = 'id', 'category_id', 'question'


class Choice(serializers.HyperlinkedModelSerializer):
    question_id = serializers.CharField(source='question.id')
    animal_id = serializers.CharField(source='animal.id')

    class Meta:
        model = Choice
        fields = 'id', 'choice', 'question_id', 'animal_id'

    