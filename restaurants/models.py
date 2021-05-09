# python import
from django.db import models  # django 와 관련된 패키지 import
from django_countries.fields import CountryField  # 3rd party package import
from core import models as core_md  # my package import
from users import models as user_md


class AbsctactItem(core_md.TimeStampModel):

    """Abstract items"""

    name = models.CharField(max_length=80)

    class Meta:
        abstract = True

    def __str__(self):
        return self.name


# 양식 , 한식, Asian, chinese, taiwanese....
class restaurantType(AbsctactItem):
    class Meta:
        verbose_name = "Restaurant Type"

    pass


# #설비 주차가능, 아이 놀이터, 등......
class Facility(AbsctactItem):

    """restaurant object definitions"""

    class Meta:
        verbose_name_plural = "Facilities"

    pass


class WholeMenu(AbsctactItem):

    """restaurnat whole menu"""

    class Meta:
        verbose_name = "Whole Menu"
        ordering = ["created"]

    pass


class Photo(core_md.TimeStampModel):

    """photo Model Definition"""

    caption = models.CharField(max_length=80)
    file = models.ImageField()
    restaurant = models.ForeignKey("Restaurant", on_delete=models.CASCADE)

    def __str__(self):
        return self.caption


# Create your models here.
class Restaurant(core_md.TimeStampModel):
    # class > string
    """Restaurant Model definition"""

    # restaurant basic info
    name = models.CharField(max_length=140)  # restaurant name
    description = models.TextField()
    country = CountryField()
    city = models.CharField(max_length=80)
    address = models.CharField(max_length=140)
    instant_book = models.BooleanField(default=False)
    working_hours = models.CharField(max_length=140)
    restaurant_type = models.ForeignKey(
        "restaurantType", on_delete=models.SET_NULL, null=True
    )
    facilities = models.ManyToManyField("Facility", blank=True)
    whole_menu = models.ManyToManyField("WholeMenu", blank=True)

    # foreign Key -------------
    # on_delete: model connected on user ,delete userm, restaurants are also delete
    # reference : https://docs.djangoproject.com/en/2.2/ref/models/fields/
    # owner = models.ForeignKey("users.User", on_delete=models.CASCADE)
    owner = models.ForeignKey(user_md.User, on_delete=models.CASCADE)

    # menu and price description
    menuname_1 = models.CharField(max_length=80)
    menuprice_1 = models.IntegerField()

    menuname_2 = models.CharField(max_length=80)
    menuprice_2 = models.IntegerField()

    menuname_3 = models.CharField(max_length=80)
    menuprice_3 = models.IntegerField()

    def __str__(self):
        return self.name
