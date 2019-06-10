from django.db import models

# Create your models here.

class inputFields(models.Model):
    latitude = models.IntegerField(max_length= 25)
    longitude = models.IntegerField(max_length=25)

    filters = models.CharField(max_length=50)





