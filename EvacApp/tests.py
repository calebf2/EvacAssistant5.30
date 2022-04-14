from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse
from django import forms

from EvacApp.forms import CustomUserCreationForm


class TestCustomUserCreationForm(TestCase):

    # Tests that the form has a field for username, password1 and password2
    def test_empty_form(self):
        form = CustomUserCreationForm()
        self.assertIn("username", form.fields)
        self.assertIn("password1", form.fields)
        self.assertIn("password2", form.fields)


