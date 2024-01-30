# recipes/views.py
from django.shortcuts import render
from django.http import HttpResponse

def add_product_to_recipe(request):
    # Логика добавления продукта к рецепту
    return HttpResponse("Product added to recipe!")

def cook_recipe(request):
    # Логика приготовления рецепта
    return HttpResponse("Recipe cooked!")

def show_recipes_without_product(request):
    # Логика отображения рецептов без указанного продукта
    return render(request, 'recipes/recipes_without_product.html', {'recipes': your_filtered_recipe_list})
