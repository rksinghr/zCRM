from django.db import models
from django.contrib.auth.models import User
from company.models import Company

class ProductCategory(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Product(models.Model):
    activity = models.CharField(max_length=255, blank=True, null=True)
    category = models.ForeignKey(ProductCategory, on_delete=models.CASCADE)
    cost = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.category.name

class ProjectMaster(models.Model):
    client = models.ForeignKey(Company, on_delete=models.CASCADE)
    projectName = models.CharField(max_length=255, blank=True, null=True)
    dueDate = models.DateField()
    createDate = models.DateField(auto_now_add=True)
    # createdBy = models.ForeignKey("User", on_delete=models.CASCADE)

    def __str__(self):
        return f"Project #{self.id} for {self.client.name}"

class BOQ(models.Model):
    projectID = models.ForeignKey(ProjectMaster, related_name='BOQ_proj', on_delete=models.CASCADE)
    product = models.ForeignKey(Product, related_name='BOQ_prod', on_delete=models.CASCADE)
    quantity = models.IntegerField(null=True, blank=True)
    price_per_item = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    createDate = models.DateField(auto_now_add=True)
    # createdBy = models.ForeignKey("User", on_delete=models.CASCADE)

    def total_price(self):
        return self.quantity * self.price_per_item

    def __str__(self):
        return f"{self.product.activity} - {self.quantity} @ {self.price_per_item}"
