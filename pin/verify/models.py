from django.db import models

# Create your models here.
from __future__ import unicode_literals


from django.contrib.auth.models import User

class Verify(models.Model):
    number = models.CharField(max_length=16)
    name = models.CharField(max_length=100)
