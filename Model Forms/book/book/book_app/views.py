from django.shortcuts import render, redirect

from book.book_app.forms import BookForm
from book.book_app.models import Book


def index(request):
    books_data = Book.objects.all()
    context = {
        'books' : books_data
    }

    return render(request, 'index.html', context)



def create(request):
    if request.method == 'GET':
        form = BookForm()
        return render(request, 'create.html', {'form': form})
    form = BookForm(request.POST)
    if form.is_valid():
        book = form.save()
        book.save()
        return redirect('create')
    return render(request, 'create.html', {'form': form})

def edit(request, pk):
    book = Book.objects.get(pk=pk)
    if request.method == 'GET':
        form = BookForm(instance=book)
        return render(request, 'edit.html', {'form':form})
    form = BookForm(request.POST, instance=book)
    if form.is_valid():
        book = form.save()
        book.save()
        return redirect(f'/edit/{pk}')
    return render(request, 'edit.html', {'form': form})
