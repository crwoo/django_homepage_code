from django.db import models
from core import models as core_md

# Create your models here.


class List(core_md.TimeStampModel):

    """List Model Definition"""

    name = models.CharField(max_length=80)
    user = models.ForeignKey("users.User", on_delete=models.CASCADE)
    restaurants = models.ManyToManyField("restaurants.Restaurant", blank=True)

    def __str__(self):
        return self.name
