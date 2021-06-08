from django.shortcuts import render, redirect
from Recipes.recipes_app.models import Recipe
from urllib import parse


def index(request):
    context = {
        'recipes': Recipe.objects.all()
    }
    return render(request, 'index.html', context)


def create(request):
    return render(request, 'create.html')


def create_recipe(request):
    title = request.POST['title']
    image_url = request.POST['image_url']
    description = request.POST['description']
    ingredients = request.POST['ingredients']
    time = request.POST['time']
    recipe = Recipe(
        title=title,
        image_url=image_url,
        description=description,
        ingredients=ingredients,
        time=time
    )
    recipe.save()
    return redirect('/')

def edit(request, pk):
    recipe = Recipe.objects.get(pk=pk)
    context = {
        'recipe': recipe
    }
    return render(request, 'edit.html', context)

def edit_recipe(request, pk):
    recipe = Recipe.objects.get(pk=pk)
    recipe.title = request.POST['title']
    recipe.image_url = request.POST['image_url']
    recipe.description = request.POST['description']
    recipe.ingredients = request.POST['ingredients']
    recipe.time = request.POST['time']
    recipe.save()
    return redirect('/')

def delete(request):
    return render(request, 'delete.html')

def details(request):
    return render(request, 'details.html')
