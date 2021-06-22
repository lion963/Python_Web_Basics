from django import forms

from Expenses_Tracker.expenses_app.models import Profile, Expense


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = '__all__'

        widgets = {
            'budget': forms.NumberInput(attrs={'class': 'form-control'}),
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'})
        }

class ExpenseForm(forms.ModelForm):
    class Meta:
        model = Expense
        fields = "__all__"

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control raunded 4'}),
            'image_url': forms.URLInput(attrs={'class': 'form-control raunded 4'}),
            'description': forms.Textarea(attrs={'class': 'form-control raunded 4'}),
            'price': forms.NumberInput(attrs={'class': 'form-control raunded 4'})
        }