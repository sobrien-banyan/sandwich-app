from django.shortcuts import render
from django.views import View

# Create your views here.

ingredients = {
    'meats': ['beef', 'turkey'],
    'cheeses': ['chedder', 'sharp chedder'],
    'toppings': ['mayo', 'mustard'],
}

class SandwichappView(View):
    def get(self, request):
        return render (
            request = request,
            template_name='sandwichapp.html',
            context={'ingredients': ingredients.keys()}
        )

class IngredientsView(View):
    def get(self, request, ingredient_type):
        return render (
            request = request,
            template_name='ingredients_list.html',
            context={
                'ingredients': ingredients[ingredient_type],
                'ingredient': ingredient_type
            }
        )
