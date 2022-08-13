from django import forms
from django.template.defaultfilters import add


class UserForm(add):
internet-app= forms.internet-app(max_length=100)
ktv-app= forms.CharField(max_length=100)
days-work= forms.CharField(max_length=100)
email= forms.EmailField()

