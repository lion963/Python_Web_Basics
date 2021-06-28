from django.shortcuts import render, redirect

from Notes.notes_app.forms import NoteForm, ProfileForm
from Notes.notes_app.models import Profile, Note


def home_page(request):
    profile = Profile.objects.first()
    notes = Note.objects.all()
    if profile:
        context = {
            'profile': profile,
            'notes': notes,
        }
        return render(request, 'home-with-profile.html', context)

    if request.method == 'GET':
        context = {
            'profile': profile,
            'form': ProfileForm()
        }
        return render(request, 'home-no-profile.html', context)
    if request.method == 'POST':
        form = ProfileForm(request.POST)
        context = {
            'profile': profile,
            'form': form
        }
        if form.is_valid():
            prifile = form.save()
            prifile.save()
            return redirect('home')
        return render(request, 'home-no-profile.html', context)


def add_note(request):
    if request.method == 'GET':
        form = NoteForm()
        context = {
            'form': form
        }
        return render(request, 'note-create.html', context)
    form = NoteForm(request.POST)
    context = {
        'form': form
    }
    if form.is_valid():
        form.save()
        return redirect('home')
    return render(request, 'note-create.html', context)

def edit_note(request, pk):
    note = Note.objects.get(pk=pk)
    if request.method == 'GET':
        form = NoteForm(instance=note)
        return render(request, 'note-edit.html', {'form': form, 'note': note})
    form = NoteForm(request.POST, instance=note)
    if form.is_valid():
        note = form.save()
        note.save()
        return redirect('home')
    return render(request, 'note-edit.html', {'form': form, 'note': note})

def delete_note(request, pk):
    note = Note.objects.get(pk=pk)
    if request.method == 'GET':
        form = NoteForm(instance=note)
        for field in form.fields:
            form.fields[field].widget.attrs['readonly'] = True
            form.fields[field].widget.attrs['disabled'] = True
        return render(request, 'note-delete.html', {'form': form, 'note': note})
    note.delete()
    return redirect('home')

def details_note(request, pk):
    note = Note.objects.get(pk=pk)
    return render(request, 'note-details.html', {'note': note})

def profile_page(request):
    profile= Profile.objects.first()
    notes = Note.objects.all()
    count = len(notes)

    if request.method == 'GET':
        return render(request, 'profile.html', {'profile': profile, 'count': count})
    profile.delete()
    for note in Note.objects.all():
        note.delete()
    return redirect('home')

