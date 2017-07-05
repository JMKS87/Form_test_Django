from django.db import models

# Create your models here.


class Counters(models.Model):
    name = models.CharField(max_length=100, unique=True)
    counter = models.IntegerField()


    def __str__(self):
        return self.name