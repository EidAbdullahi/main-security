from django.db import models
from django.contrib.auth.models import User


class Police(models.Model):
    name=models.CharField(max_length=200)
    mother_name=models.CharField(max_length=200)
    dob=models.CharField(max_length=20)
    place_of_birth=models.CharField(max_length=200)
    gender=models.CharField(max_length=20)
    maritial_status=models.CharField(max_length=50)
    training_count=models.PositiveIntegerField()
    training_by=models.CharField(max_length=200)

