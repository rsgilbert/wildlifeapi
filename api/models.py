from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=128)
    info = models.CharField(max_length=128)
    picture = models.CharField(max_length=128, blank=True)

    def __str__(self):
        return self.name

class Animal(models.Model):
    category = models.ForeignKey(to=Category, on_delete=models.CASCADE)
    name = models.CharField(max_length=128)
    picture = models.CharField(max_length=128, blank=True)

    def __str__(self):
        return self.name


class Question(models.Model):
    category = models.ForeignKey(to=Category, on_delete=models.CASCADE)
    question = models.CharField(max_length=128)
    
    def __str__(self):
        return self.question



class Choice(models.Model):
    question = models.ForeignKey(to=Question, on_delete=models.CASCADE)
    choice = models.CharField(max_length=128)
    animal = models.ForeignKey(to=Animal, on_delete=models.CASCADE)

    def __str__(self):
        return self.choice

