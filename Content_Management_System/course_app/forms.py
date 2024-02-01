# course_app/forms.py
from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import CustomUser

class SignUpForm(UserCreationForm):
    class Meta:
        model = CustomUser 
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']

class SignInForm(AuthenticationForm):
    class Meta:
        model = CustomUser 
        fields = ['username', 'password']


        
class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ['first_name', 'last_name','username']  # Add other fields as needed

    # Override the default widget for each field to make them not required
    first_name = forms.CharField(required=False)
    last_name = forms.CharField(required=False)
    username = forms.CharField(required=False)

    


