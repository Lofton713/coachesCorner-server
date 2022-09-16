from django.db import models

class Game(models.Model):
    player = models.ForeignKey("Player", on_delete=models.CASCADE)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    date = models.DateField()
    time = models.TimeField()
    description = models.TextField(max_length=100)
    attendees = models.ManyToManyField("Coach", through="Attendee", related_name="attending")
    
@property
def joined(self):
    return self.__joined

@joined.setter
def joined(self, value):
    self.__joined = value