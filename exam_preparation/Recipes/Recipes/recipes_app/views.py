from django.shortcuts import render
from Recipes.recipes_app.models import Recipe


def index(request):
    context = {
        'recipes': True
            # Recipe.objects.all()
    }
    return render(request, 'index.html', context)


def create_recipe(request):
    # title = request.POST.title
    # image_url = request.POST.image_url
    # description = request.POST.description
    # ingredients = request.POST.ingredients
    # time = request.POST.time
    # Recipe(
    #     title=title,
    #     image_url=image_url,
    #     description=description,
    #     ingredients=ingredients,
    #     time=time
    # ).save()
    return render(request, 'create.html')


def delete(request):
    return render(request, 'delete.html')


def edit(request):
    return render(request, 'edit.html')


def details(request):
    return render(request, 'details.html')
