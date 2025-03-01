from django.urls import path

from .views import recipe_list, recipe_1, recipe_2, IngredientListView, IngredientDetailView

urlpatterns = [
    path('recipes/list', recipe_list, name="recipe/list"),
    path('recipe/1', recipe_1, name="recipe/1"),
    path('recipe/2', recipe_2, name="recipe/2"),
    path('list', IngredientListView.as_view(), name='list'),
    path('<int:id>/detail', IngredientDetailView.as_view(), name='ingredient-detail')
]

app_name = "ledger"