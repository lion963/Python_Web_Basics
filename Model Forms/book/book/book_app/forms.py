from django import forms
from django.core.exceptions import ValidationError

from book.book_app.models import Book


class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = '__all__'
        widgets = {
            'title' : forms.TextInput(attrs= {'class': 'form-control'}),
            'pages' : forms.NumberInput(attrs= {'class': 'form-control'}),
            'author' : forms.TextInput(attrs= {'class': 'form-control'}),
            'description' : forms.Textarea(attrs= {'class': 'form-control'}),
        }

    # def clean_pages(self):
    #     value = self.cleaned_data['pages']
    #     if value <= 0:
    #         raise ValidationError('Page count must be bigger than zero')