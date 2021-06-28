from django.db import models

class Profile(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    age = models.IntegerField(null=True)
    image_url = models.URLField(null=True)

class Note(models.Model):
    titele = models.CharField(max_length=30)
    image_url = models.URLField(null=True)
    content = models.TextField(null=True)

