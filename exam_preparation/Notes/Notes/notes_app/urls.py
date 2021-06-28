from django.contrib import admin
from django.urls import path

from Notes.notes_app.views import home_page, add_note, edit_note, delete_note, details_note, profile_page

urlpatterns = [
    path('', home_page, name='home'),
    path('add', add_note, name='add note'),
    path('edit/<int:pk>', edit_note, name='edit note'),
    path('delete/<int:pk>', delete_note, name='delete note'),
    path('details/<int:pk>', details_note, name='details note'),
    path('profile', profile_page, name='profile')

]
