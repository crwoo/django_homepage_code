from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

# Abstact User : DB X
class User(AbstractUser):
    """custom user model"""

    GENDER_MALE = "Male"
    GENDER_FEMALE = "Female"
    GENDER_OTHER = "Other"

    GENDER_CHOICES = (
        (GENDER_MALE, "Male"),
        (GENDER_FEMALE, "Female"),
        (GENDER_OTHER, "Other"),
    )

    LANGUAGE_ENGLISH = "en"
    LANGUAGE_KOREAN = "kr"

    LANGUAGE_CHOICES = ((LANGUAGE_ENGLISH, "English"), (LANGUAGE_KOREAN, "Korean"))

    CURRENCY_USD = "usd"
    CURRENCY_KRW = "krw"

    CURRENCY_CHOICES = ((CURRENCY_USD, "USD"), (CURRENCY_KRW, "KRW"))

    bio = models.TextField(default="")  # 제목 이름이 bold가 아님
    avatar = models.ImageField(blank=True)
    gender = models.CharField(
        choices=GENDER_CHOICES, default="Female", max_length=10, blank=True
    )
    birthdate = models.DateField(blank=True, null=True)
    language = models.CharField(choices=LANGUAGE_CHOICES, max_length=2, blank=True)
    currency = models.CharField(choices=CURRENCY_CHOICES, max_length=3, blank=True)

    superrestaurant = models.BooleanField(default=False)


00
