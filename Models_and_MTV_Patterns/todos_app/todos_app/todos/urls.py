from django.urls import path

from todos_app.todos.views import index, show_forms_demo

urlpatterns = [
    path('', index),
    path('forms/', show_forms_demo)

]