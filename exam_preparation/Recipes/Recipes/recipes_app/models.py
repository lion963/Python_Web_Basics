from django.db import models

class Recipe(models.Model):
    title = models.CharField(max_length=30)
    image_url = models.URLField(null=True)
    description = models.TextField(null=True)
    ingredients = models.CharField(max_length=20)
    time = models.IntegerField(null=True)