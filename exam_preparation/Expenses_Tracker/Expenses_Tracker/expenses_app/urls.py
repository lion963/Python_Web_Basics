from django.urls import path

from Expenses_Tracker.expenses_app.views import home_page, profile, create_expenses

urlpatterns = [
    path('', home_page, name='home'),
    path('profile', profile, name='profile'),
    path('create', create_expenses, name='create expenses')
]