from django import forms

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
