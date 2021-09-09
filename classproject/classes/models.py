from django.db import models

# Create your models here.
class Class(models.Model):
    title = models.CharField(max_length=100)
    platform = models.CharField(max_length=100)
    length = models.CharField(max_length=100)

