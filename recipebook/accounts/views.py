from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
# Create your views here.

class CustomView(LoginRequiredMixin, RecipeListView):
    template_name = "recipe_list.html"
    redirect_field_name = '/login' # URL to redirect when not logged in
