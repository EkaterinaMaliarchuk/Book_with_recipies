# recipes/views.py
from django.shortcuts import render
from .models import Recipe, RecipeProduct

def show_recipes_without_product(request, product_id):
    # Рецепты, в которых указанный продукт отсутствует или присутствует в количестве менее 10 грамм
    recipes_without_product = Recipe.objects.exclude(recipeproduct__product_id=product_id) | Recipe.objects.filter(recipeproduct__product_id=product_id, recipeproduct__weight__lt=10)

    context = {
        'product_id': product_id,
        'recipes': recipes_without_product
    }

    return render(request, 'recipes/show_recipes_without_product.html', context)
