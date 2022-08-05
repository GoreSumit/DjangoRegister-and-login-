from django.db import models

class registration(models.Model):
    name = models.CharField(max_length=70)
    contact = models.CharField(max_length=70)
    email = models.CharField(max_length=70)
    password = models.CharField(max_length=70)
