from django.urls import path

from Expenses_Tracker.expenses_app.views import home_page, profile, create_expenses, edit_expenses, delete_expenses, \
    edit_profile, delete_profile

urlpatterns = [
    path('', home_page, name='home'),
    path('profile', profile, name='profile'),
    path('profile/edit', edit_profile, name='edit profile'),
    path('profile/delete', delete_profile, name='delete profile'),
    path('create', create_expenses, name='create expenses'),
    path('edit/<int:pk>', edit_expenses, name='edit expenses'),
    path('delete/<int:pk>', delete_expenses, name='delete expenses'),
]