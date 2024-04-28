from django.db import models
from account.models import Stage
from lead.models import Lead
from django.contrib.auth.models import User

class Opportunity(models.Model):
	amount = models.CharField(max_length=50)
	probability = models.CharField(max_length=50)
	stage = models.ForeignKey(Stage, on_delete=models.CASCADE)
	closeDate = models.DateField()
	createdOn = models.DateField(auto_now_add=True)
	lastContact = models.DateField()
	lead = models.ForeignKey(Lead, on_delete=models.CASCADE)
	assignedTo = models.ForeignKey(User, on_delete=models.CASCADE)

	def __str__(self):
		return(f"{self.assignedTo.name}")
