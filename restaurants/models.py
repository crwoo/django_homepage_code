# python import
from django.db import models  # django 와 관련된 패키지 import
from django_countries.fields import CountryField  # 3rd party package import
from core import models as core_md  # my package import
from users import models as user_md

# Create your models here.
class Restaurant(core_md.TimeStampModel):

    """Restaurant Model definition"""

    # restaurant basic info
    name = models.CharField(max_length=140)  # restaurant name
    description = models.TextField()
    country = CountryField()
    city = models.CharField(max_length=80)
    address = models.CharField(max_length=140)
    instant_book = models.BooleanField(default=False)
    working_hours = models.CharField(max_length=140)

    # foreign Key -------------
    owner = models.ForeignKey(user_md.User, on_delete=models.CASCADE)

    # menu and price description
    menuname_1 = models.CharField(max_length=80)
    menuprice_1 = models.IntegerField()

    menuname_2 = models.CharField(max_length=80)
    menuprice_2 = models.IntegerField()

    menuname_3 = models.CharField(max_length=80)
    menuprice_3 = models.IntegerField()

    menuname_4 = models.CharField(max_length=80)
    menuprice_4 = models.IntegerField()

    menuname_5 = models.CharField(max_length=80)
    menuprice_5 = models.IntegerField()
