from django.db import models


class Sentiments(models.Model):
    word = models.CharField(max_length=200, blank=True, null=True)
    goodbad = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return self.word

    def was_good_or_bad(self):
        return self.goodbad
