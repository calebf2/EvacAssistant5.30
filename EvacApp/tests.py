from django.contrib.auth.models import User
from django.test import TestCase, Client
from django.urls import reverse, resolve
from django import forms
from bs4 import BeautifulSoup
import requests
from EvacApp import views
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
            data={'username': 'username', 'password1': 'password', 'password2': 'password'}
        )

        if userForm.is_valid():
            user1 = userForm.save()
            self.assertEquals(user1.username, user.username)
            self.assertEquals(user1.password1, user.password)

    def test_form_password_validation(self):
        user = User.objects.create_user(
            username='username',
            password='12345678'
        )
        userForm = CustomUserCreationForm(
            data={'username': 'username', 'password1': 'password', 'password2': 'password'}
        )


class TestHTMLPageLinks(TestCase):

    # Tests the index.html file has an href to the register page
    def test_home_page_link_to_register_page(self):
        soup = BeautifulSoup(open('EvacApp/templates/EvacApp/index.html', 'r'), 'html.parser')
        link_text = ""
        for a in soup.find_all('a', href=True):
            link_text = a['href']
        self.assertEquals(link_text, '../register/')


class TestUrls(TestCase):

    def test_home_page(self):
        c = Client()
        response = c.post('')
        self.assertEquals(response.status_code, 200)

    def test_register_page(self):
        c = Client()
        response = c.post('/register/')
        self.assertEquals(response.status_code, 200)


class TestHTMLPageLinks(TestCase):

    # Tests the register.html file has an href to the index page
    def test_register_page_link_to_home_page(self):
        soup = BeautifulSoup(open('EvacApp/templates/EvacApp/register.html', 'r'), 'html.parser')
        link_text = ""
        for a in soup.find_all('a', href=True):
            link_text = a['href']
        # print("Link: " + link_text)
        self.assertEquals(link_text, '../')
