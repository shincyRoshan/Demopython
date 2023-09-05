from django.db import models

# Create your models here.
class Tasks(models.Model):
    name=models.CharField(max_length=250)
    priorites=models.IntegerField()

