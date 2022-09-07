import imp
from django.db import models

class College(models.Model):
    name = models.CharField(max_length=50)
    location = models.CharField (max_length=50)
    min_GPA = models.FloatField()
    