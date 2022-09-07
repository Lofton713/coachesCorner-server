from django.db import models

class Open_spot(models.Model):
    college = models.ForeignKey("College", on_delete=models.CASCADE)
    position = models.CharField(max_length=20)
    description = models.TextField(max_length=200)
    posted_by = models.ForeignKey("Coach", on_delete=models.CASCADE)
    applicants = models.ManyToManyField("Player", through="Applicant", related_name="applicant_player")