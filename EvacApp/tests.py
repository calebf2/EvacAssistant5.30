from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse
from django import forms
from bs4 import BeautifulSoup
import requests

import EvacApp.templates.EvacApp
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


class TestHTMLPageLinks(TestCase):

    # Tests the index.html file has an href to the register page
    def test_home_page_link_to_register_page(self):

        soup = BeautifulSoup(open('EvacApp/templates/EvacApp/index.html', 'r'), 'html.parser')
        link_text = ""
        for a in soup.find_all('a', href=True):
            link_text = a['href']
        self.assertEquals(link_text, '../register/')
