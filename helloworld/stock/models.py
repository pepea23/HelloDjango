from django.db import models


class Travel(models.Model):
    name_travel = models.CharField(max_length=200)
    price = models.IntegerField(default=0)
    date = models.DateTimeField('date published')


