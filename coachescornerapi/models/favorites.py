from pyexpat import model
from django.db import models

class Favorite(models.Model):
    player = models.ForeignKey("Player", on_delete=models.CASCADE, related_name="player_id")
    college = models.ForeignKey("College", on_delete=models.CASCADE, related_name="school")
    