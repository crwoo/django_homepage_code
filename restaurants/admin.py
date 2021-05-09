from django.contrib import admin
from . import models


# restaurantType, Facility, WholeMenu
# Meta class
@admin.register(models.restaurantType, models.Facility, models.WholeMenu)
class ItemAdmin(admin.ModelAdmin):
    """Item admin Definitions"""

    pass


# Register your models here.
@admin.register(models.Restaurant)
class RestaurantAdmin(admin.ModelAdmin):
    """restaurant admin Definitions"""

    pass


@admin.register(models.Photo)
class PhotoAdmin(admin.ModelAdmin):
    pass
