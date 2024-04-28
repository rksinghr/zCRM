from django.db import models
# from django.contrib.auth.models import User
from company.models import Company

class Contact(models.Model):
	name = models.CharField(max_length=50)
	email = models.EmailField()
	phone = models.CharField(max_length=50)
	address1 = models.CharField(max_length=50)
	address2 = models.CharField(max_length=50)
	city = models.CharField(max_length=50)
	state = models.CharField(max_length=50)
	company = models.ForeignKey(Company, on_delete=models.CASCADE)

	def __str__(self):
		return(f"{self.name}")
