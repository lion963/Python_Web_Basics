"""Recipes URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from Recipes.views import home_page, create_recipe, delete_recipe, edit_recipe, details_recipe

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home_page),
    path('create', create_recipe),
    path('delete', delete_recipe),
    path('edit', edit_recipe),
    path('details', details_recipe)
]
