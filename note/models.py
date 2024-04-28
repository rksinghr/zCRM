from django.db import models
from contact.models import Contact
from account.models import ActivityType
from django.contrib.auth.models import User

class Note(models.Model):
	name = models.CharField(max_length=50)
	description = models.CharField(max_length=50)
	relatedTo = models.ForeignKey(Contact, on_delete=models.CASCADE)
	createdOn = models.DateField(auto_now_add=True)
	createdBy = models.ForeignKey(User, on_delete=models.CASCADE)

	def __str__(self):
		return(f"{self.contact.name}")

class Activity(models.Model):
	activityType = models.ForeignKey(ActivityType, on_delete=models.CASCADE)
	name = models.CharField(max_length=50)
	description = models.CharField(max_length=50)
	relatedTo = models.ForeignKey(Contact, on_delete=models.CASCADE)
	createdOn = models.DateField(auto_now_add=True)
	createdBy = models.ForeignKey(User, on_delete=models.CASCADE)

	def __str__(self):
		return(f"{self.name}")
