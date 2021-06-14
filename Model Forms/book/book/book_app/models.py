from django.db import models

from book.book_app.validators import page_validator


class Book(models.Model):
    title = models.CharField(max_length=20, null=True)
    pages = models.IntegerField(default=0, validators=[page_validator])
    description = models.CharField(max_length=100, default='', null=True)
    author = models.CharField(max_length=20, null=True)