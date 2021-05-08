from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from . import models


# Register your models here.
@admin.register(
    models.User
)  # decorator, admin.site.register(models.user, CustomUserAdmin)
class CustomUserAdmin(UserAdmin):

    """custom admin panel"""

    fieldsets = UserAdmin.fieldsets + (
        (
            "Custom Profile",
            {
                "fields": (
                    "avatar",
                    "gender",
                    "bio",
                    "birthdate",
                    "language",
                    "currency",
                    "superrestaurant",
                )
            },
        ),
    )  # blue title

    # list_display = ("username", "gender", "language", "currency", "superrestaurant")
    # list_filter = ("language", "currency", "superrestaurant")
