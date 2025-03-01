from django.shortcuts import render
from django.http import HttpResponse
from .models import Ingredients, Recipe, RecipeIngredient
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
# Create your views here.

class IngredientListView(ListView):
    model = Ingredients
    template_name = 'ingredient_list.html'

class IngredientDetailView(DetailView):
    model = Ingredients
    template_name = 'ingredient_detail.html'

    
def ingredients_list(request):
    ingredients = Ingredients.objects.all()
    ctx = {
        'ingredients' : ingredients
    }
    return render(request, 'ingredient_list.html', ctx)

def ingredients_detail(request, id):
    ctx = {
        'ingredient' : Ingredients.objects.get(id=id) 
    }
    return render(request, 'ingredients_detail.html', ctx)
