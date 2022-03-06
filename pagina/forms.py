from dataclasses import field
from statistics import mode
from django.forms import forms
from django import forms
from .models import *

class formu(forms.ModelForm):
    model = messages
    field = '__all__'