from django.db import models

# Assuming you have a model for countries and cities, or you can use third-party packages like django-countries
from django_countries.fields import CountryField

class UploadedImage(models.Model):
    image = models.ImageField(upload_to='images/')
    uploaded_at = models.DateTimeField(auto_now_add=True)

class Skill(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name

class Emp_details(models.Model):
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    mobile = models.CharField(max_length=12)
    birth = models.DateField()
    gender = models.CharField(max_length=100)
    address = models.TextField()
    country = CountryField()
    city = models.CharField(max_length=100)
    skills = models.ManyToManyField(Skill)

