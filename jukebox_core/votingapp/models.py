from django.db import models
from django.utils import timezone
from datetime import datetime, timedelta

class Songs(models.Model):
    YoutubeLink = models.URLField(("Youtube Link"),max_length=128, db_index=True, unique=True, blank=True)
    votes = models.IntegerField(default=0)
    SongName = models.CharField(max_length=50)
    
    
    def __str__(self):
        return self.SongName

