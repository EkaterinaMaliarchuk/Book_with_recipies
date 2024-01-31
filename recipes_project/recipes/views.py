from django.shortcuts import render
from django.http import HttpResponse
import random
from .models import Recipe, Product, RecipeProduct


def add_product_to_recipe(request):
    # Получаем все рецепты и продукты из базы данных
    recipes = Recipe.objects.all()
    products = Product.objects.all()

    # Выбираем случайный рецепт и продукт
    random_recipe = random.choice(recipes)
    random_product = random.choice(products)

    # Генерируем случайное количество продукта для добавления к рецепту
    random_quantity = random.randint(1, 100)

    # Создаем связь RecipeProduct для добавления продукта к рецепту
    recipe_product = RecipeProduct.objects.create(
        recipe=random_recipe,
        product=random_product,
        quantity=random_quantity
    )

    return HttpResponse(f"Product '{random_product.name}' added to recipe '{random_recipe.title}' with quantity {random_quantity}!")

def cook_recipe(request, recipe_id):
    # Получаем рецепт по переданному идентификатору
    recipe = Recipe.objects.get(pk=recipe_id)

    # Получаем все продукты, связанные с данным рецептом
    recipe_products = RecipeProduct.objects.filter(recipe=recipe)

    # Представим, что здесь есть логика приготовления рецепта с использованием списка продуктов

    return HttpResponse(f"Recipe '{recipe.title}' cooked!")

def show_recipes_without_product(request, product_id):
    # Получаем продукт по переданному идентификатору
    product = Product.objects.get(pk=product_id)

    # Получаем все рецепты, в которых указанный продукт отсутствует или присутствует в количестве менее 10 грамм
    recipes_without_product = Recipe.objects.exclude(products=product)  # Вероятно, вам нужно адаптировать это условие

    return render(request, 'recipes/recipes_without_product.html', {'recipes': recipes_without_product})
