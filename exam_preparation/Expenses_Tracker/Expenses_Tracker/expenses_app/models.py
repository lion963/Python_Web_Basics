from django.db import models


class Profile(models.Model):
    first_name = models.CharField(max_length=15)
    last_name = models.CharField(max_length=15)
    budget = models.IntegerField(null=True)


class Expense(models.Model):
    title = models.CharField(max_length=50)
    image_url = models.URLField(null=True)
    description = models.TextField(null=True)
    price = models.FloatField(null=True)



