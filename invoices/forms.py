from django import forms
from .models import ProjectMaster, BOQ, Product

class ProjectForm(forms.ModelForm):
    # class Meta:
    #     model = ProjectMaster
    #     fields = ['client', 'projectName', 'dueDate']
    class Meta:
        model = ProjectMaster
        fields = ['client', 'projectName', 'dueDate']
        widgets = {
            'client': forms.Select(attrs={'class': 'form-control'}),
            'projectName': forms.TextInput(attrs={'class': 'form-control'}),
            'dueDate': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
        }

class InvoiceItemForm(forms.ModelForm):
    class Meta:
        model = BOQ
        fields = ['product', 'quantity', 'price_per_item']
    # class Meta:
    #     model = InvoiceItem
    #     fields = ['product', 'quantity', 'price_per_item']
    #     widgets = {
    #         'product': forms.Select(attrs={'class': 'form-control'}),
    #         'quantity': forms.DateInput(attrs={'class': 'form-control'}),
    #         'price_per_item': forms.DateInput(attrs={'class': 'form-control'}),
    #     }
