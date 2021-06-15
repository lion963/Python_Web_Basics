from django.urls import path
from lost_and_found_app import views

urlpatterns = (
    path('', views.index, name="index"),
    path('create/', views.create, name="create"),
    path('edit/<int:id>', views.edit, name="edit"),
    path('delete/<int:id>', views.delete, name="delete"),
    path('found/<int:id>', views.found, name="found")
)
