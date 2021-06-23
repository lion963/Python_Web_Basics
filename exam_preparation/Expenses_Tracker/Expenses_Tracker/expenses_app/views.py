from django.shortcuts import render, redirect

from Expenses_Tracker.expenses_app.forms import ProfileForm, ExpenseForm
from Expenses_Tracker.expenses_app.models import Profile, Expense


def home_page(request):
    profiles = Profile.objects.all()
    expenses = Expense.objects.all()
    if profiles:
        left = profiles[0].budget - sum([expense.price for expense in expenses])
        context = {
            'profile': profiles[0],
            'expenses': expenses,
            'left': left
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

def edit_profile(request):
    profile = Profile.objects.all()[0]
    if request.method == 'GET':
        form = ProfileForm(instance=profile)
        return render(request, 'profile-edit.html', {'form': form})
    form = ProfileForm(request.POST, instance=profile)
    if form.is_valid():
        profile = form.save()
        profile.save()
        return redirect('profile')
    return render(request, 'profile-edit.html', {'form': form})

def delete_profile(request):
    profile = Profile.objects.all()[0]
    if request.method == 'GET':
        return render(request, 'profile-delete.html')
    profile.delete()
    for expense in Expense.objects.all():
        expense.delete()
    return redirect('home')

def create_expenses(request):
    if request.method == 'GET':
        form = ExpenseForm()
        context = {
            'form': form
        }
        return render(request, 'expense-create.html', context)
    form = ExpenseForm(request.POST)
    context = {
        'form': form
    }
    if form.is_valid():
        form.save()
        return redirect('home')
    return render(request, 'expense-create.html', context)

def edit_expenses(request, pk):
    expense = Expense.objects.get(pk=pk)
    if request.method == 'GET':
        form = ExpenseForm(instance=expense)
        return render(request, 'expense-edit.html', {'form': form})
    form = ExpenseForm(request.POST, instance=expense)
    if form.is_valid():
        expense = form.save()
        expense.save()
        return redirect('home')
    return render(request, 'expense-edit.html', {'form': form})


def delete_expenses(request,pk):
    expense = Expense.objects.get(pk=pk)
    if request.method == 'GET':
        form = ExpenseForm(instance=expense)
        for field in form.fields:
            form.fields[field].widget.attrs['readonly'] = True
        return render(request, 'expense-edit.html', {'form': form})
    expense.delete()
    return redirect('home')


