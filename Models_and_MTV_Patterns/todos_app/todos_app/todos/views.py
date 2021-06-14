from django.shortcuts import render

from todos_app.todos.models import Todo

def show_forms_demo(request):
    return render(request, 'forms_demo.html')

def index(request):
    context = {
        'todos': Todo.objects.all()
    }
    return render(request, 'index.html', context)
