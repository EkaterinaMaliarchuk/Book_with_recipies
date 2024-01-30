# recipes/admin.py
from django.contrib import admin
from .models import Product, Recipe, RecipeProduct

class RecipeProductInline(admin.TabularInline):
    model = RecipeProduct

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'times_cooked')

@admin.register(Recipe)
class RecipeAdmin(admin.ModelAdmin):
    list_display = ('name',)
    inlines = [RecipeProductInline]
