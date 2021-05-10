from django.db import models
from core import models as core_md

# Create your models here.
class Reservation(core_md.TimeStampModel):

    """Reservation Model Definitions"""

    STATUS_PENDING = "pending"
    STATUS_CONFIRMED = "confirmed"
    STATUS_CANCELED = "cancled"

    STATUS_CHOICES = (
        (STATUS_PENDING, "Pending"),
        (STATUS_CANCELED, "Cancle"),
        (STATUS_CONFIRMED, "Confirmed"),
    )

    # 예약상태, 손님, 식당, 손님 수, 방문시간
    visit_time = models.DateField()  # 방문날짜
    num_of_visitors = models.IntegerField()  # 방문인원
    message = models.TextField(max_length=120, blank=True)  # 간단한 메세지
    status = models.CharField(
        max_length=12, choices=STATUS_CHOICES, default=STATUS_PENDING
    )  # 예약상태
    guest = models.ForeignKey("users.User", on_delete=models.CASCADE)  # 예약손님
    restaurant = models.ForeignKey(
        "restaurants.Restaurant", on_delete=models.CASCADE
    )  # 식당

    def __str__(self):
        return f"{self.restaurant} - {self.visit_time}"
