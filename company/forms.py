from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import Company

class CompanyForm(forms.ModelForm):

    name = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"Name", "class":"form-control"}), label="")
    industry = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"Industry", "class":"form-control"}), label="")
    email = forms.CharField(required=True, widget=forms.widgets.EmailInput(attrs={"placeholder":"E-mail", "class":"form-control"}), label="")
    phone = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"Phone", "class":"form-control"}), label="")
    website = forms.CharField(required=True, widget=forms.widgets.URLInput(attrs={"placeholder":"Company Website", "class":"form-control"}), label="")
    address1 = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"Address Line1", "class":"form-control"}), label="")
    address2 = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"Address Line2", "class":"form-control"}), label="")
    city = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"City", "class":"form-control"}), label="")
    state = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"State", "class":"form-control"}), label="")
    
    class Meta:
        model = Company
        exclude = ()