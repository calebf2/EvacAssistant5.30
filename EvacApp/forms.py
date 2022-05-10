from django.contrib.auth.models import User
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError
from django.forms.fields import EmailField
from django.forms.forms import Form
from .models import AddressProfile

# Form for registering users
class CustomUserCreationForm(UserCreationForm):

    # A username and 2 passwords will be in the form
    username = forms.CharField(label='Username', min_length=5, max_length=150)
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Confirm Password', widget=forms.PasswordInput)

    # Checks for already registered username
    def username_clean(self):
        username = self.cleaned_data['username'].lower()
        new = User.objects.filter(username=username)
        if new.count():
            raise ValidationError("User Already Exist")
        return username

    # Verifies the passwords match
    def clean_password2(self):
        password1 = self.cleaned_data['password1']
        password2 = self.cleaned_data['password2']

        if password1 and password2 and password1 != password2:
            raise ValidationError("Password don't match")
        return password2

    # Saves the username and passwords to the user
    def save(self, commit=True):
        user = User.objects.create_user(
            self.cleaned_data['username'],
            self.cleaned_data['password1'],
            self.cleaned_data['password2']
        )
        return user

# Form for registering places
class PlaceProfileForm(forms.ModelForm):
    address = forms.CharField(label='Address', min_length=5, max_length=100, required=True, widget=forms.HiddenInput())
    town = forms.CharField(label='Town', min_length=5, max_length=100, required=True, widget=forms.HiddenInput())
    county = forms.CharField(label='County', min_length=5, max_length=100, required=True, widget=forms.HiddenInput())
    zip_code = forms.CharField(label='ZIP', min_length=5, max_length=8, required=True, widget=forms.HiddenInput())
    country = forms.CharField(label='Country', min_length=5, max_length=40, required=True, widget=forms.HiddenInput())
    longitude = forms.CharField(label='Longitude', min_length=5, max_length=50, required=False, widget=forms.HiddenInput())
    latitude = forms.CharField(label='Latitude', min_length=5, max_length=50, required=False, widget=forms.HiddenInput())


    class Meta:
        model = AddressProfile
        fields = ('address', 'town', 'county', 'zip_code', 'country', 'longitude', 'latitude')