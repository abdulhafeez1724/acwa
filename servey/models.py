from django.db import models

# Create your models here.
class NewProfile(models.Model):
    fname = models.CharField(max_length=50)  # First name
    lname = models.CharField(max_length=50)  # Last name
    office = models.CharField(max_length=100)  # Office location
    quote = models.CharField(max_length=1000)  # Quote

    def __str__(self):
        return f"{self.fname} {self.lname}"  # Returns full name