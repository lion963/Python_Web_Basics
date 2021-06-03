from django.shortcuts import render
from Recipes.models import Recipe


def home_page(request):
    # try:
    #     recipes_data = Recipe.objects.get()
    # except:
    #     recipes_data = False
    context = {
        'recipes': True
    }
    return render(request, 'index.html', context)


def create_recipe(request):
    return render(request, 'create.html')


def delete_recipe(request):
    return render(request, 'delete.html')


def edit_recipe(request):
    return render(request, 'edit.html')


def details_recipe(request):
    return render(request, 'details.html')
