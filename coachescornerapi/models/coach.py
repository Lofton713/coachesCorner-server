from django.db import models
from django.contrib.auth.models import User

class Coach(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    college = models.ForeignKey("College", on_delete=models.CASCADE, null=True)
    bio = models.TextField(max_length=200)
    profile_pic = models.ImageField(upload_to='profilepics', height_field=None,
        width_field=None, max_length=None, null=True)
    recruits = models.ManyToManyField("Player", through="Recruit", related_name="recruits")