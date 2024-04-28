from django.db import models
from contact.models import Contact
from account.models import Priority, Status
from django.contrib.auth.models import User
from datetime import date

class Task(models.Model):
	name = models.CharField(max_length=50)
	description = models.CharField(max_length=50)
	priority = models.ForeignKey(Priority, on_delete=models.CASCADE)
	status = models.ForeignKey(Status, on_delete=models.CASCADE)
	dueDate = models.DateField(default=date.today(), blank=True, null=True)
	createdOn = models.DateField(auto_now_add=True)
	relatedTo = models.ForeignKey(Contact, on_delete=models.CASCADE)
	assignedTo = models.ForeignKey(User, on_delete=models.CASCADE)
	createdBy = models.ForeignKey(User, on_delete=models.CASCADE, related_name="Task_createdBy")

	def __str__(self):
		return(f"{self.contact.name}")
