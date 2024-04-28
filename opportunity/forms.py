from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import Opportunity
from account.models import Stage
from lead.models import Lead

class DateInput(forms.DateInput):
    input_type = 'date'

class OpportunityForm(forms.ModelForm):

    amount = forms.CharField(required=True, widget=forms.widgets.TextInput(
            attrs={"placeholder":"Amount", "class":"form-control"})
            , label="")

    probability = forms.CharField(required=True, widget=forms.widgets.TextInput(
        attrs={"placeholder":"Probability", "class":"form-control"})
        , label="")

    closeDate = forms.DateField(widget=DateInput(
        attrs={"placeholder":"Last connect Date", "class":"form-control"})
        , label="Close Date")

    lastContact = forms.DateField(widget=DateInput(
        attrs={"placeholder":"Last connect Date", "class":"form-control"})
        , label="Last Connect Date")

    stage = forms.ModelChoiceField(
        queryset=Stage.objects.all(), widget=forms.Select(
            attrs={"class":"form-control", "placeholder":"Stage"}))

    lead = forms.ModelChoiceField(
        queryset=Lead.objects.all(), widget=forms.Select(
            attrs={"class":"form-control", "placeholder":"Lead"}))

    assignedTo = forms.ModelChoiceField(
        queryset=User.objects.all(), widget=forms.Select(
            attrs={"class":"form-control", "placeholder":"Assigned To"}))
    
    class Meta:
        model = Opportunity
        exclude = ()