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
        fields = 'id', 'category_id', 'name'


class QuestionSerializer(serializers.HyperlinkedModelSerializer):
    category_id = serializers.CharField(source='category.id')

    class Meta:
        model = Question
        fields = 'id', 'category_id', 'question'


class ChoiceSerializer(serializers.HyperlinkedModelSerializer):
    question_id = serializers.CharField(source='question.id')
    animal_id = serializers.CharField(source='animal.id')

    class Meta:
        model = Choice
        fields = 'id', 'choice', 'question_id', 'animal_id'
