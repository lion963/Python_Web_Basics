from django.contrib import admin
from django.urls import path

from Recipes.recipes_app.views import home_page, create_recipe, delete_recipe, edit_recipe, details_recipe

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home_page),
    path('create', create_recipe),
    path('delete', delete_recipe),
    path('edit', edit_recipe),
    path('details', details_recipe)
]