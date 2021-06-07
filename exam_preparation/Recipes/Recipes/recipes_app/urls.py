from django.contrib import admin
from django.urls import path

from Recipes.recipes_app.views import index, create, delete, edit, details, create_recipe

urlpatterns = [
    path('', index),
    path('create', create),
    path('create_recipe', create_recipe),
    path('delete', delete),
    path('edit', edit),
    path('details', details)
]