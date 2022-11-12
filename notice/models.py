from dataclasses import dataclass
from pyexpat import model
from django.db import models

# Create your models here.
class Notic(models.Model):
    title = models.CharField(max_length=200)
    desc = models.TextField()
    date_time = models.DateTimeField()

    def __str__(self):
        return self.title

