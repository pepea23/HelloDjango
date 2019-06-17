import datetime

from django.db import models
from django.utils import timezone 

class Glass(models.Model):
    name_glass = models.CharField(max_length=200)
    price = models.IntegerField(default=0)
    quntity = models.IntegerField(default=0)
    date = models.DateTimeField('date published')

    def __str__(self):
        return self.name_glass
    
    def was_published_recently(self):
        return self.date >= timezone.now() - datetime.timedelta(days=1)


        

