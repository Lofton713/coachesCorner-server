from django.db import models

class Game(models.Model):
    player = models.ForeignKey("Player", on_delete=models.CASCADE)
    location = models.CharField(max_length=50)
    date = models.DateField()
    time = models.TimeField()
    description = models.TextField(max_length=100)
    attendees = models.ManyToManyField("Coach", through="Attendee", related_name="attending")