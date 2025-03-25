"""Models file."""
from django.db import models
from django.urls import reverse

# Create your models here.


class Ingredient(models.Model):
    """Ingredient object."""

    name = models.CharField(max_length=100)

    def __str__(self):
        """Return name."""
        return self.name

    def get_absolute_url(self):
        """Return url link."""
        return reverse('ingredient', args=[str(self.name)])


class Recipe(models.Model):
    """Ingredient object."""

    name = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    createdOn = models.DateTimeField()
    updatedOn = models.DateTimeField()

    def __str__(self):
        """Return name."""
        return self.name

    def get_absolute_url(self):
        """Return url link."""
        return reverse('ledger:recipe-detail', args=[self.pk])


class RecipeIngredient(models.Model):
    """RecipeIngredient object."""

    quantity = models.IntegerField()
    ingredient = models.ForeignKey(Ingredient,
                                   models.SET_NULL,
                                   null=True,
                                   related_name='recipe')
    recipe = models.ForeignKey(Recipe,
                               models.SET_NULL,
                               null=True,
                               related_name='ingredient')


class RecipeImage(models.Model):
    """RecipeImage object."""

    image = models.ImageField(upload_to='images/', null=True)
    description = models.CharField(max_length=255)
    recipe = models.ForeignKey(Recipe,
                               on_delete=models.CASCADE,
                               related_name='images')
