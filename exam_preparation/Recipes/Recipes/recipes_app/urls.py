from django.contrib import admin
from django.urls import path

from Recipes.recipes_app.views import index, create, delete, edit, details

urlpatterns = [
    path('', index),
    path('create', create, name='create'),
    path('edit/<int:pk>', edit, name='edit'),
    path('delete/<int:pk>', delete, name='delete'),
    path('details/<int:pk>', details, name='details')
]