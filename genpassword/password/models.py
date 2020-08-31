from django.db import models
from django.contrib.auth.models import User
from django_cryptography.fields import encrypt

# Create your models here.
class Passwords(models.Model):
	name = models.CharField(max_length=200)
	password = encrypt(models.CharField(max_length=20))
	
