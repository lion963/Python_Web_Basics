from django.db import models

class Person(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return f"{self.id}: {self.name}"

    class Meta:
        verbose_name_plural = 'People'

class Category(models.Model):
    HOME_CHOISE = 'Home'
    WORK_CHOISE = 'Work'
    NAME_CHOICES = (
        (HOME_CHOISE, 'Home stuff'),
        (WORK_CHOISE, 'Work stuff')
    )
    name = models.CharField(max_length=20, choices=NAME_CHOICES)

    class Meta:
        verbose_name_plural = 'Categories'


class Todo(models.Model):
    text = models.CharField(max_length=30)
    state = models.BooleanField(default=False)
    owner = models.ForeignKey(Person, on_delete=models.CASCADE, null=True)
    categories = models.ManyToManyField(Category)

