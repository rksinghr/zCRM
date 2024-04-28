from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import Note
from account.models import Status
from contact.models import Contact

class NoteForm(forms.ModelForm):

    # name = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"Name", "class":"form-control"}), label="")
    # phone = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"Phone", "class":"form-control"}), label="")
    # lastContact = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"Last connect Date", "class":"form-control"}), label="")

    widgets = {
        'name': forms.TextInput(attrs={"placeholder":"Name", "class":"form-control"}),
        'description': forms.TextInput(attrs={"placeholder":"Phone", "class":"form-control"}),
        'relatedTo': forms.Select(attrs={"placeholder":"Contact Name", "class":"form-control"}),
    }
    
    class Meta:
        model = Note
        exclude = ('createdBy', 'createdOn',)