from django.db import models


class Level(models.TextChoices):
    Extinct = "Extinct"
    Extinct_in_the_Wild = "Extinct in the Wild"
    Critically_Endangered = "Critically Endangered"
    Endangered = "Endangered"
    Vulnerable = "Vulnerable"
    Near_threatened = "Near Threatened"
    Least_Concern = "Least Concern"
    Data_Deficient = "Data Deficient"

class Home(models.TextChoices):
    Land = "LAND"
    Air = "AIR"
    Water = "WATER"

class Category(models.Model):
    name = models.CharField(max_length=128)
    info = models.CharField(max_length=5000)
    picture = models.CharField(max_length=128, blank=True)
    level = models.CharField(max_length=128, choices=Level.choices)
    count = models.IntegerField(blank=True, null=True)
    home = models.CharField(max_length=128, choices=Home.choices, default=Home.Land)

    def __str__(self):
        return self.name


class Animal(models.Model):
    category = models.ForeignKey(to=Category, on_delete=models.CASCADE)
    name = models.CharField(max_length=128)
    picture = models.CharField(max_length=128, blank=True)
    location = models.CharField(max_length=128, blank=True)
    level = models.CharField(max_length=128, choices=Level.choices)
    count = models.IntegerField(blank=True, null=True)

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
    correct = models.BooleanField(default=False)
    info = models.CharField(max_length=1000, blank=True)

    def __str__(self):
        return self.choice
