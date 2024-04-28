from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import Lead
from account.models import Status
from contact.models import Contact

class DateInput(forms.DateInput):
    input_type = 'date'

class LeadForm(forms.ModelForm):

    name = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"Name", "class":"form-control"}), label="")
    phone = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"Phone", "class":"form-control"}), label="")
    lastContact = forms.DateField(widget=DateInput(
        attrs={"placeholder":"Last connect Date", "class":"form-control"})
        , label="Last Contact Date")
    status = forms.ModelChoiceField(
        queryset=Status.objects.all(),
        widget=forms.Select(attrs={"class":"form-control", "placeholder":"Stage"}),
        label="Select Status")
    assignedTo = forms.ModelChoiceField(
        queryset=User.objects.all(),
        widget=forms.Select(attrs={"class":"form-control", "placeholder":"Stage"}),
        label="Select to Assign Lead")
    contact = forms.ModelChoiceField(
        queryset=Contact.objects.all(),
        widget=forms.Select(attrs={"class":"form-control", "placeholder":"Stage"}),
        label="Select Business Contact")
    
    class Meta:
        model = Lead
        exclude = ()