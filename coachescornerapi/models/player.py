from django.db import models
from django.contrib.auth.models import User

class Player(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="player")
    birthday = models.DateField()
    bio = models.TextField(max_length=200)
    GPA = models.FloatField()
    hometown = models.CharField(max_length=20)
    state = models.CharField(max_length=2)
    profile_pic = models.ImageField(upload_to='profilepics', height_field=None,
        width_field=None, max_length=None, null=True)
    position = models.CharField(max_length=20)
    grade = models.CharField(max_length=20) 