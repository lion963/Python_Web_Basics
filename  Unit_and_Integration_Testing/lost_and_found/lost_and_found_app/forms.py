from lost_and_found_app import models
from django.forms import ModelForm


class PostCreateForm(ModelForm):
    class Meta:
        model = models.Post
        fields = ("title", "description", "author_name", "author_phone")


class PostEditForm(ModelForm):
    class Meta:
        model = models.Post
        fields = ("title", "description", "author_name", "author_phone", "found")


class ObjectForm(ModelForm):
    class Meta:
        model = models.Object
        fields = "__all__"
