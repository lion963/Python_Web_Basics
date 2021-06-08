from django.contrib import admin
from django.urls import path

from Recipes.recipes_app.views import index, create, delete, edit, details, create_recipe, edit_recipe

urlpatterns = [
    path('', index),
    path('create', create),
    path('create_recipe', create_recipe),
    path('edit/<int:pk>', edit),
    path('edit_recipe/<int:pk>', edit_recipe),
    path('delete', delete),
    path('details', details)
]