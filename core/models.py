from django.db import models

# Create your models here.
class TimeStampModel(models.Model):

    """Time stamp module"""

    # not database class
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateField(auto_now=True)

    class Meta:
        abstract = True
