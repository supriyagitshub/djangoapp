from django.db import models

# Create your models here.
class person(models.Model):
	name=models.CharField(max_length=100)
	email=models.EmailField(max_length=100)
	location=models.CharField(max_length=100)