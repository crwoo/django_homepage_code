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

    list_display = (
        "name",
        "country",
        "city",
        "address",
        "instant_book",
        "restaurant_type",
        "owner",
    )

    list_filter = (
        "instant_book",
        "city",
        "country",
    )

    # 검색으로 도시 찾을 수 있음
    # owner__ <언더바 두개 = foreign key
    search_fields = ("^city", "owner__username", "name")

    pass


@admin.register(models.Photo)
class PhotoAdmin(admin.ModelAdmin):
    pass
