from django.shortcuts import render, redirect

from Expenses_Tracker.expenses_app.forms import ProfileForm
from Expenses_Tracker.expenses_app.models import Profile, Expense


def home_page(request):
    profiles = Profile.objects.all()
    expenses = True
        # Expense.objects.all()
    if profiles:
        context = {
            'profiles': profiles,
            'expenses': expenses
        }
        return render(request, 'home-with-profile.html', context)

    if request.method == 'GET':
        context = {
            'profiles': profiles,
            'form': ProfileForm()
        }
        return render(request, 'home-no-profile.html', context)
    if request.method == 'POST':
        form = ProfileForm(request.POST)
        context = {
            'profiles': profiles,
            'form': form
        }
        if form.is_valid():
            prifile = form.save()
            prifile.save()
            return redirect('home')
        return render(request, 'home-no-profile.html', context)

def profile(request):
    context = {
        'profile': Profile.objects.all()[0]
    }
    return render(request, 'profile.html', context)

def create_expenses(request):
    return render(request, 'expense-create.html')