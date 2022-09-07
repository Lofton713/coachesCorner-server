from statistics import mode
from django.db import models

class Attendee(models.Model):
    coach = models.ForeignKey("Coach", on_delete=models.CASCADE)
    game = models.ForeignKey("Game", on_delete=models.CASCADE)