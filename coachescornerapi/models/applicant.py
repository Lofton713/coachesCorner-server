from django.db import models

class Applicant(models.Model):
    open_spot = models.ForeignKey("Open_spot", on_delete=models.CASCADE, related_name="open_spot_id")
    player = models.ForeignKey("Player", on_delete=models.CASCADE, related_name="applicant")