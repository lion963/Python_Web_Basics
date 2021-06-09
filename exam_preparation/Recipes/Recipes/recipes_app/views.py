from django.shortcuts import render, redirect
from Recipes.recipes_app.models import Recipe
from urllib import parse


def index(request):
    context = {
        'recipes': Recipe.objects.all()
    }
    return render(request, 'index.html', context)


def create(request):
    if request.POST.get('Create_button'):
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
    return render(request, 'create.html')

def edit(request, pk):
    recipe = Recipe.objects.get(pk=pk)
    context = {
        'recipe': recipe
    }
    if request.POST.get('Edit_button'):
        recipe.title = request.POST['title']
        recipe.image_url = request.POST['image_url']
        recipe.description = request.POST['description']
        recipe.ingredients = request.POST['ingredients']
        recipe.time = request.POST['time']
        recipe.save()
        return redirect('/')
    return render(request, 'edit.html', context)

def delete(request, pk):
    recipe = Recipe.objects.get(pk=pk)
    context = {
        'recipe': recipe
    }
    if request.POST.get('Delete_button'):
        recipe.delete()
        return redirect('/')
    return render(request, 'delete.html', context)


def details(request, pk):
    recipe = Recipe.objects.get(pk=pk)
    ingredients = recipe.ingredients.split(', ')
    context = {
        'recipe': recipe,
        'ingredients_list': ingredients
    }
    return render(request, 'details.html', context)
