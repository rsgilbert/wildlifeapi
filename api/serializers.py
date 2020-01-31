from rest_framework import serializers

from .models import Category, Animal, Question, Choice


class CategorySerializer(serializers.HyperlinkedModelSerializer):
    id = serializers.ReadOnlyField()

    class Meta:
        model = Category
        exclude = ['url']


class AnimalSerializer(serializers.HyperlinkedModelSerializer):
    category_id = serializers.CharField(source='category.id')

    class Meta:
        model = Animal
        fields = 'id', 'category_id', 'name', 'level', 'count', 'location'


class QuestionSerializer(serializers.HyperlinkedModelSerializer):
    category_id = serializers.CharField(source='category.id')

    class Meta:
        model = Question
        fields = 'id', 'category_id', 'question'


class ChoiceSerializer(serializers.HyperlinkedModelSerializer):
    question_id = serializers.CharField(source='question.id')

    class Meta:
        model = Choice
        fields = 'id', 'choice', 'correct', 'question_id', 'info'
