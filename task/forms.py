from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import Task
from account.models import Status, Priority
from contact.models import Contact
from opportunity.forms import DateInput

class TaskForm(forms.ModelForm):

    name = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"Name", "class":"form-control"}), label="")
    description = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"Description", "class":"form-control"}), label="")
    dueDate = forms.DateField(widget=DateInput(
        attrs={"placeholder":"Due Date", "class":"form-control"})
        , label="Last Connect Date")

    priority = forms.ModelChoiceField(
        queryset=Priority.objects.all(), widget=forms.Select(
            attrs={"class":"form-control", "placeholder":"Priority"}))

    status = forms.ModelChoiceField(
        queryset=Status.objects.all(), widget=forms.Select(
            attrs={"class":"form-control", "placeholder":"Status"}))

    assignedTo = forms.ModelChoiceField(
        queryset=User.objects.all(), widget=forms.Select(
            attrs={"class":"form-control", "placeholder":"Assigned To"}))

    relatedTo = forms.ModelChoiceField(
        queryset=Contact.objects.all(), widget=forms.Select(
            attrs={"class":"form-control", "placeholder":"Related To"}))
    
    class Meta:
        model = Task
        exclude = ('createdBy',)