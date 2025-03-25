"""Urls file."""
from django.urls import path
from .views import RecipeListView, RecipeDetailView
from .views import RecipeUpdateView, RecipeCreateView

urlpatterns = [
    path('recipes/list', RecipeListView.as_view(), name='recipe-list'),
    path('recipe/<int:pk>', RecipeDetailView.as_view(), name='recipe-detail'),
    path('recipe/add', RecipeCreateView.as_view(), name='recipe-add'),
    path('recipe/<int:pk>/add_image', RecipeUpdateView.as_view(),
         name='recipe-update')
]

app_name = "ledger"
