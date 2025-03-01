from django.db import models
from django.urls import reverse

# Create your models here.

class Ingredients(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('ingredients', args=[str(self.name)])

class Recipe(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('recipe', args=[str(self.name)])

class RecipeIngredient(models.Model):
    quantity = models.IntegerField()
    ingredients = models.ForeignKey(Ingredients, on_delete=models.CASCADE, related_name='ingredients')
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE, related_name='recipe') 