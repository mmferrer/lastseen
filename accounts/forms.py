from django import forms
from accounts.models import *
from django.forms import ModelForm
from django.contrib.sites.models import Site
from django.contrib.auth.models import User
from accounts.models import UserAccount
from django.contrib.auth.tokens import default_token_generator
from django.utils.http import int_to_base36
from django.template import Context, loader
from django import forms

class UserCreationForm(forms.ModelForm):
    username = forms.RegexField(label="Username", max_length=30, regex=r'^[\w.@+-]+$',
                                help_text="Required. 30 characters or fewer. Letters, digits and @/./+/-/_ only.",
                                error_messages = {'invalid': "This value may contain only letters, numbers and @/./+/-/_ characters."},
                                widget = forms.TextInput(attrs={'placeholder': 'Username'}))
    password = forms.CharField(label="Password", widget=forms.PasswordInput(attrs={'placeholder': 'Password'}))
    password2 = forms.CharField(label="Password confirmation", widget=forms.PasswordInput(attrs={'placeholder': 'Repeat Password'}),
                                help_text = "Enter the same password as above, for verification.")
    email1 = forms.EmailField(label="Email", max_length=75, widget = forms.TextInput(attrs={'placeholder': 'Email'}))
    email2 = forms.EmailField(label="Email confirmation", max_length=75,
                              help_text = "Enter your email address again. A confirmation email will be sent to this address.",
                              widget = forms.TextInput(attrs={'placeholder': 'Confirm Email'}))
#    captcha = CaptchaField()
    class Meta:
        model = UserAccount
        widgets = {
            'username': forms.TextInput(attrs={'placeholder': 'Username'}),
            'first_name': forms.TextInput(attrs={'placeholder': 'First Name'}),
            'last_name': forms.TextInput(attrs={'placeholder': 'Last Name'}),
            'email': forms.TextInput(attrs={'placeholder': 'Email'}),
            'address': forms.TextInput(attrs={'placeholder': 'Address'}),
            'facebook': forms.TextInput(attrs={'placeholder': 'Facebook'}),
            'twitter': forms.TextInput(attrs={'placeholder': 'Twitter'}),
            'gender': forms.RadioSelect(),
        }
        fields = ("username", "first_name", "last_name","birthday","address", "facebook", "twitter", "gender")

    def clean_password2(self):
        password = self.cleaned_data.get("password", "")
        password2 = self.cleaned_data["password2"]
        if password != password2:
            raise forms.ValidationError("The two password fields didn't match.")
        return password2
    
    def clean_email1(self):
        email1 = self.cleaned_data["email1"]
        users_found = User.objects.filter(email__iexact=email1)
        if len(users_found) >= 1:
            raise forms.ValidationError("A user with that email already exist.")
        return email1

    def clean_email2(self):
        email1 = self.cleaned_data.get("email1", "")
        email2 = self.cleaned_data["email2"]
        if email1 != email2:
            raise forms.ValidationError("The two email fields didn't match.")
        return email2