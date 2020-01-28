from django.contrib import admin
from .models import Category, Animal, Question, Choice

# Register your models here.
admin.site.register(Category)
admin.site.register(Animal)
admin.site.register(Question)
admin.site.register(Choice)
