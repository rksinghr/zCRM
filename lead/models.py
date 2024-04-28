from django.db import models
from account.models import Status
from contact.models import Contact
from django.contrib.auth.models import User

class Lead(models.Model):
	name = models.CharField(max_length=50)
	status = models.ForeignKey(Status, on_delete=models.CASCADE)
	createdOn = models.DateField(auto_now_add=True)
	lastContact = models.DateField()
	contact = models.ForeignKey(Contact, on_delete=models.CASCADE)
	assignedTo = models.ForeignKey(User, on_delete=models.CASCADE)

	def __str__(self):
		return(f"{self.name}")
