from django.contrib.auth.models import User
from django.test import TestCase, Client
from django.urls import reverse, resolve
from django import forms

from EvacApp import views
from EvacApp.forms import CustomUserCreationForm


class TestCustomUserCreationForm(TestCase):

    # Tests that the form has a field for username, password1 and password2
    def test_empty_form(self):
        form = CustomUserCreationForm()
        self.assertIn("username", form.fields)
        self.assertIn("password1", form.fields)
        self.assertIn("password2", form.fields)

    # Tests that the form saves the username and password
    def test_form_saves_user_info(self):
        user = User.objects.create_user(
            username='username',
            password='password123'
        )
        userForm = CustomUserCreationForm(
            data={'username': 'username', 'password1': 'password', 'password2': 'password'})

        if userForm.is_valid():
            user1 = userForm.save()
            self.assertEquals(user1.username, user.username)
            self.assertEquals(user1.password1, user.password)


class TestUrls(TestCase):

    def test_homepage(self):
        c = Client()
        response = c.post('')
        self.assertEquals(response.status_code, 200)

    def test_registerpage(self):
        c = Client()
        response = c.post('/register/')
        self.assertEquals(response.status_code, 200)
