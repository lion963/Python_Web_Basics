from django.contrib import admin
from lost_and_found_app import models

# Register your models here.
admin.site.register(models.Post)
admin.site.register(models.Object)
