from django.contrib.auth.models import AbstractUser
from django.db import models
from django.contrib.gis.db.models import PointField
from django.contrib.gis.geos import Point
from .managers import CustomUserManager


class CustomUser(AbstractUser):

    # Extra fields
    home_address = models.CharField(max_length=250, null=False, blank=False)
    phone_number = models.CharField(max_length=11, null=False, blank=False)
    location = PointField(geography=True, default=Point(0.0, 0.0))

    REQUIRED_FIELDS = [
        "password",
        "home_address",
        "phone_number",
        "location"
    ]

    objects = CustomUserManager()

    def __str__(self):
        return self.email
