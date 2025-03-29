from django.contrib import admin
from .models import Product, ProjectMaster, BOQ, ProductCategory

admin.site.register(Product)
admin.site.register(ProductCategory)
admin.site.register(ProjectMaster)
admin.site.register(BOQ)
