from django.db import models

class Person(models.Model):
    name = models.CharField(max_length=30)

class Category(models.Model):
    name = models.CharField(max_length=20)


class Todo(models.Model):
    text = models.CharField(max_length=30)
    state = models.BooleanField(default=False)
    owner = models.ForeignKey(Person, on_delete=models.CASCADE, null=True)
    categories = models.ManyToManyField(Category)

