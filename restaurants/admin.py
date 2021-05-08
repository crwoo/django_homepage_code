from django.contrib import admin
from . import models

# Register your models here.
@admin.register(models.Restaurant)
class RestAdmin(admin.ModelAdmin):
    pass
