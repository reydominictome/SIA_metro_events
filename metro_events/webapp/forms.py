from django import forms
from .models import *

#Create forms here

class RegistrationForm(forms.ModelForm):

   class Meta:
        model = User
        fields = ('first_name','middle_name','last_name','username','email','password')
