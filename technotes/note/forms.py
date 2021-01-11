from django.contrib.auth import get_user_model
from django import forms
from note.models import User
from django.contrib.auth.forms import UserCreationForm
from django.forms import ValidationError

class UserRegistrationForm(UserCreationForm):
    first_name = forms.CharField(max_length=20, required=True)
    last_name  = forms.CharField(max_length=20, required=True) 
    email      = forms.EmailField(required=True)
    password1  = forms.CharField(widget=forms.PasswordInput)
    password2  = forms.CharField(widget=forms.PasswordInput,max_length=28)

    def clean(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
                raise ValidationError("An account with this email already exists.")
        return self.cleaned_data

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'password1', 'password2']

User = get_user_model()