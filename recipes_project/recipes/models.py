# recipes/models.py
from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=255, unique=True)
    times_cooked = models.IntegerField(default=0)

    def __str__(self):
        return self.name

class Recipe(models.Model):
    name = models.CharField(max_length=255)

class RecipeProduct(models.Model):
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    weight = models.IntegerField()

    def __str__(self):
        return f"{self.recipe.name} - {self.product.name} ({self.weight}g)"
