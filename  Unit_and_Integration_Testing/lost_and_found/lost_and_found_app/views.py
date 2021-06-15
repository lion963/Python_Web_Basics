from django.shortcuts import render, redirect
from lost_and_found_app.models import *
from lost_and_found_app.forms import PostCreateForm, ObjectForm, PostEditForm


# Create your views here.
def index(req):
    posts = Post.objects.all()
    return render(req, 'index.html', context={'posts': posts})


def edit(req, id):
    if req.method == "POST":
        post_from_base = Post.objects.get(pk=id)
        post_form = PostEditForm(req.POST, instance=post_from_base)

        if post_form.is_valid():
            post_form.save()
            return redirect('index')
    else:
        post = Post.objects.get(pk=id)
        post_form = PostEditForm(instance=post)
        return render(req, 'post_edit.html', context={'post_form': post_form})


def delete(req, id):
    post = Post.objects.get(pk=id)
    post.delete()
    return redirect('index')


def found(req, id):
    post = Post.objects.get(pk=id)
    post.found = True
    post.save()
    return redirect('index')


def create(req):
    if req.method == "POST":
        data = req.POST

        object_data = {
            'name': data['name'],
            'image': data['image'],
            'width': int(data['width']),
            'height': int(data['height']),
            'weight': int(data['weight'])
        }

        object = Object(**object_data)
        object.save()

        post_data = {
            'title': data['title'],
            'description': data['description'],
            'author_name': data['author_name'],
            'author_phone': data['author_phone'],
            'object': object
        }

        post = Post(**post_data)
        post.save()
        return redirect('index')
    else:
        post_form = PostCreateForm()
        object_form = ObjectForm()
        return render(req, 'post_create.html', context={'post_form': post_form, 'object_form': object_form})
