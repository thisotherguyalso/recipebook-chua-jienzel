"""Views file."""
from django.shortcuts import redirect
from .models import Recipe
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView
from .forms import RecipeForm, RecipeImageForm
# Create your views here.


class RecipeListView(ListView):
    """List view of recipe."""

    model = Recipe
    template_name = 'recipe_list.html'


class RecipeDetailView(DetailView):
    """Detail view of recipe."""

    model = Recipe
    template_name = 'recipe_detail.html'


class RecipeUpdateView(LoginRequiredMixin, UpdateView):
    """Update view of recipe."""

    model = Recipe
    template_name = 'recipe_update.html'
    form_class = RecipeImageForm

    def get_success_url(self):
        """Return success url."""
        return reverse_lazy('ledger:recipe-detail',
                            kwargs={'pk': self.get_object().pk})

    def get_context_data(self, **kwargs):
        """Return context data."""
        context = super().get_context_data(**kwargs)
        context['form'] = RecipeImageForm()
        return context

    def post(self, request, *args, **kwargs):
        """Post request."""
        currentRecipe = self.get_object()
        form = RecipeImageForm(request.POST, request.FILES)
        if form.is_valid():
            recipeImage = form.save(commit=False)
            recipeImage.recipe = currentRecipe
            recipeImage.save()
            return redirect(self.get_success_url())
        else:
            self.object_list = self.get_queryset(**kwargs)
            context = self.get_context_data(**kwargs)
            context['form'] = form
            return self.render_to_response(context)


class RecipeCreateView(CreateView):
    """Create view of recipe."""

    model = Recipe
    template_name = 'recipe_add.html'
    form_class = RecipeForm

    def get_success_url(self):
        """Return success url."""
        return reverse_lazy('ledger:recipe-list')
