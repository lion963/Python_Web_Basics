from django.urls import path

from book.book_app.views import index, create, edit

urlpatterns = [
    path('', index, name='index'),
    path('create', create, name='create'),
    path('edit/<int:pk>', edit, name='edit')
]