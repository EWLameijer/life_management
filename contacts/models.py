from django.db import models

# Create your models here.

NAME_LENGTH = 30

class Contact(models.Model):
    name = models.CharField(max_length=NAME_LENGTH)



