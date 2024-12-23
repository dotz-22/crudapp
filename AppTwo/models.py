from django.db import models

# Create your models here.

class AuthorsModel(models.Model):
    name  = models.CharField(max_length=200)
    bio = models.TextField (blank=True, null=True)
    date_of_birth = models.DateField(blank=True)