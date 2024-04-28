from django.db import models
from django.contrib.auth.models import User

class Stage(models.Model):
	name = models.CharField(max_length=50)
	description = models.CharField(max_length=50)

	def __str__(self):
		return(f"{self.name}")

class ActivityType(models.Model):
	name = models.CharField(max_length=50)
	description = models.CharField(max_length=50)

	def __str__(self):
		return(f"{self.name}")

class Status(models.Model):
	name = models.CharField(max_length=50)
	description = models.CharField(max_length=50)

	def __str__(self):
		return(f"{self.name}")

class Priority(models.Model):
	name = models.CharField(max_length=50)
	description = models.CharField(max_length=50)

	def __str__(self):
		return(f"{self.name}")