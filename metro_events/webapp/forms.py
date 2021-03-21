from django import forms
from .models import *

#Create forms here

class UserForm(forms.ModelForm):

   class Meta:
        model = User
        fields = (
           'first_name',
           'middle_name',
           'last_name',
           'username',
           'password',
           'email',
           'register_date',
           'status')
