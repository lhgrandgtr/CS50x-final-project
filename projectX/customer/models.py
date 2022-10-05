from django.db import models

# Create your models here.
class Employee(models.Model):
    firstname = models.CharField(max_length=64)
    lastname = models.CharField(max_length=64)
    age = models.IntegerField()
    email = models.EmailField(max_length=128)
    mobile = models.IntegerField()
    nic = models.IntegerField()
    gender = models.CharField(max_length=10,)
    image = models.ImageField(upload_to='images', width_field=None, height_field=None)
    garden = models.BooleanField(default=False)
    house = models.BooleanField(default=False)
    pipe = models.BooleanField(default=False)
    roof = models.BooleanField(default=False)