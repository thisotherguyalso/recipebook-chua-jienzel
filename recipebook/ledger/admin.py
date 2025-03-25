"""Admin file."""
from django.contrib import admin
from .models import Recipe, Ingredient, RecipeIngredient, RecipeImage
# Register your models here.


class RecipeIngredientInline(admin.TabularInline):
    """Admin access to recipeingredient."""

    model = RecipeIngredient


class RecipeImageInline(admin.TabularInline):
    """Admin access to recipeimage."""

    model = RecipeImage


class RecipeAdmin(admin.ModelAdmin):
    """Admin access to recipe."""

    inlines = [RecipeIngredientInline, RecipeImageInline]


class IngredientAdmin(admin.ModelAdmin):
    """Admin access to ingredient."""

    inlines = [RecipeIngredientInline]


admin.site.register(Recipe, RecipeAdmin)


admin.site.register(Ingredient, IngredientAdmin)


admin.site.register(RecipeIngredient)

admin.site.register(RecipeImage)
