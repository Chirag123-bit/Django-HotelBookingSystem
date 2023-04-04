from django.db import models
from django.core.validators import FileExtensionValidator

# Create your models here.


class Hotels(models.Model):
    name = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    country = models.CharField(max_length=50)
    logo = models.ImageField(upload_to="logos", 
                             default="sample_user.png",validators=[FileExtensionValidator(["png", "jpg"])])
    wifi = models.BooleanField()
    pickup = models.BooleanField()
    water = models.BooleanField()
    allService = models.BooleanField()
    telephone = models.BooleanField()

    def __str__(self):
        return self.name



class Accomodations(models.Model):
    name = models.CharField(max_length=100)
    hotel = models.ForeignKey(to=Hotels, on_delete=models.CASCADE)
    price = models.FloatField()
    desc = models.TextField()
    image1 = models.ImageField(upload_to="suites", 
                             default="sample_suite.png",validators=[FileExtensionValidator(["png", "jpg"])])
    image2 = models.ImageField(upload_to="suites", 
                             default="sample_suite.png",validators=[FileExtensionValidator(["png", "jpg"])])
    image3 = models.ImageField(upload_to="suites", 
                             default="sample_suite.png",validators=[FileExtensionValidator(["png", "jpg"])])


    def __str__(self):
        return self.name