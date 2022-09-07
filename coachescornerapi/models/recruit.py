from django.db import models

class Recruit(models.Model):
    coach = models.ForeignKey("Coach", on_delete=models.CASCADE, related_name="coach_id")
    player = models.ForeignKey("Player", on_delete=models.CASCADE, related_name="recruit")