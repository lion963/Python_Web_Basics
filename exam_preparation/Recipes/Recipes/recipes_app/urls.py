from django.contrib import admin
from django.urls import path

from Recipes.recipes_app.views import index, create_recipe, delete, edit, details

urlpatterns = [
    path('', index),
    path('create', create_recipe),
    path('delete', delete),
    path('edit', edit),
    path('details', details)
]