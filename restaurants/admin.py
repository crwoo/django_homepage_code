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

    fieldsets = (
        (
            "Basic Info",
            {
                "fields": (
                    "name",
                    "description",
                    "country",
                    "address",
                    "restaurant_type",
                    "instant_book",
                )
            },
        ),
        (
            "Times",
            {
                "fields": (
                    "working_hours",
                    "working_hours_end",
                )
            },
        ),
        (
            "Menues",
            {
                "fields": (
                    "menuname_1",
                    "menuprice_1",
                    "menuname_2",
                    "menuprice_2",
                    "menuname_3",
                    "menuprice_3",
                )
            },
        ),
        (
            "Detail about Restaurants",
            {
                "fields": (
                    "facilities",
                    "whole_menu",
                )
            },
        ),
        (
            "Owner",
            {"fields": ("owner",)},
        ),
    )

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
        "restaurant_type",
        "facilities",
        "whole_menu",
        "city",
        "country",
    )

    filter_horizontal = (
        "facilities",
        "whole_menu",
    )

    ordering = ("name", "restaurant_type")

    # 검색으로 도시 찾을 수 있음
    # owner__ <언더바 두개 = foreign key
    search_fields = ("^city", "owner__username", "name")

    def count_facilities(self, obj):
        # print(obj.owner)
        return "P"

    # count_facilities.short_description

    pass


@admin.register(models.Photo)
class PhotoAdmin(admin.ModelAdmin):
    pass
