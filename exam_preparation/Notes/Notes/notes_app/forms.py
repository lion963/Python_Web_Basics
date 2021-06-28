from django import forms

from Notes.notes_app.models import Profile, Note


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = '__all__'

class NoteForm(forms.ModelForm):
    class Meta:
        model = Note
        fields = "__all__"