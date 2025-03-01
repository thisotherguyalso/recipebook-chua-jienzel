"""Admin file."""
from django.contrib import admin
from .models import Recipe, Ingredient, RecipeIngredient
# Register your models here.


class RecipeAdmin(admin.ModelAdmin):
    """Admin access to recipe."""

    model = Recipe


class IngredientAdmin(admin.ModelAdmin):
    """Admin access to ingredient."""

    model = Ingredient


class RecipeIngredientAdmin(admin.ModelAdmin):
    """Admin access to recipeingredient."""

    model = RecipeIngredient


admin.site.register(Recipe, RecipeAdmin)


admin.site.register(Ingredient, IngredientAdmin)


admin.site.register(RecipeIngredient, RecipeIngredientAdmin)
