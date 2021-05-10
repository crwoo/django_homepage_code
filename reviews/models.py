from django.db import models
from core import models as core_mds

# Create your models here.
class Review(core_mds.TimeStampModel):

    """Review Model Definitions"""

    review = models.TextField()

    # 맛, 친절도, 배달, 청결도
    taste = models.IntegerField()
    cleanliness = models.IntegerField()
    location = models.IntegerField()
    delivery = models.IntegerField()
    price = models.IntegerField()
    kindness = models.IntegerField()

    user = models.ForeignKey("users.User", on_delete=models.CASCADE)
    restaurant = models.ForeignKey("restaurants.Restaurant", on_delete=models.CASCADE)

    def __str__(self):
        # return self.review
        return f"{self.review}-{self.restaurant.name}"
        # return self.restaurants.name
