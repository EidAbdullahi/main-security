from django.db import models
from django.contrib.auth.models import User


class Police(models.Model):
    profile_pic= models.ImageField(upload_to='profile_pic/Police/',null=True,blank=True)
    name=models.CharField(max_length=200)
    mother_name=models.CharField(max_length=200)
    dob=models.CharField(max_length=20)
    place_of_birth=models.CharField(max_length=200)
    gender=models.CharField(max_length=20)
    maritial_status=models.CharField(max_length=50)
    training_count=models.PositiveIntegerField()
    salary = models.PositiveIntegerField(null=True)
    training_by=models.CharField(max_length=200)

class Logistic(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    mother_name=models.CharField(max_length=200)
    mobile = models.CharField(max_length=40)
    gender=models.CharField(max_length=20)
    def __str__(self):
        return self.user.first_name
    @property
    def get_id(self):
        return self.user.id
    @property
    def get_name(self):
        return self.user.first_name+" "+self.user.last_name

class CID(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    mother_name=models.CharField(max_length=200)
    mobile = models.CharField(max_length=40)
    gender=models.CharField(max_length=20)
    salary = models.PositiveIntegerField(null=True)
    def __str__(self):
        return self.user.first_name
    @property
    def get_id(self):
        return self.user.id
    @property
    def get_name(self):
        return self.user.first_name+" "+self.user.last_name

class OB(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    mother_name=models.CharField(max_length=200)
    mobile = models.CharField(max_length=40)
    gender=models.CharField(max_length=20)
    salary = models.PositiveIntegerField(null=True)
    def __str__(self):
        return self.user.first_name
    @property
    def get_id(self):
        return self.user.id
    @property
    def get_name(self):
        return self.user.first_name+" "+self.user.last_name

class Report(models.Model):
    crime_date=models.DateField()
    criminal_pic= models.ImageField(upload_to='profile_pic/Criminal/',null=True,blank=True)
    criminal_name=models.CharField(max_length=20)
    gender=models.CharField(max_length=20)
    height=models.CharField(max_length=20)
    weight=models.CharField(max_length=20)
    hair_color=models.CharField(max_length=20)
    crime=models.CharField(max_length=500)

    reporter_name=models.CharField(max_length=20,null=True)
    posted_by=models.CharField(max_length=20,null=True)
    posted_date=models.DateField(auto_now=True)
