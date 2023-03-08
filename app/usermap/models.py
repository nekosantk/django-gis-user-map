from django.contrib.auth.models import AbstractUser
from django.db import models
from django.contrib.gis.db.models import PointField
from django.contrib.gis.geos import Point
from .managers import CustomUserManager


class CustomUser(AbstractUser):

    # Extra fields
    home_address = models.CharField(max_length=250, blank=True)
    phone_number = models.CharField(max_length=11, blank=True)
    location = PointField(geography=True, default=Point(0.0, 0.0))

    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return self.email
