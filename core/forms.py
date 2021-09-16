from django import forms
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm,UsernameField
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _
class SignUpForm(UserCreationForm):
   password1=forms.CharField(label='Password',widget=forms.PasswordInput(attrs={'placeholder': 'Password' ,'class':'form-control'}))
   password2=forms.CharField(label='Confirm Password(again)',widget=forms.PasswordInput(attrs={'placeholder': 'Confirm Password','class':'form-control'}))
   class Meta:
    model=User
    fields=['username','first_name','last_name','email']
    labels={'username':'User Name','first_name':'First Name','last_name':'Last Name','email':'Email'}
    widgets={'username':forms.TextInput(attrs={'placeholder': 'Username','class':'form-control'}),
          'first_name':forms.TextInput(attrs={'placeholder': 'firstname' ,'class':'form-control'}),
          'last_name':forms.TextInput(attrs={'placeholder': 'lastname' ,'class':'form-control'}),
          'email':forms.EmailInput(attrs={'placeholder': 'email' ,'class':'form-control'})}

class LoginForm(AuthenticationForm):
    username=UsernameField(widget=forms.TextInput(attrs={'autofocus':True,'class':'form-control '}))
    password=forms.CharField(label=_('Password'), strip=False,
             widget=forms.PasswordInput(attrs={'autocomplete':'current-password','class':'form-control '}))
   


    