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

    # Test the form validates the passwords
    def test_form_password_validation(self):
        # Invalid password, password less than 8 characters and all numerical
        user1 = User.objects.create_user(
            username='username',
            password='123'
        )
        userForm = CustomUserCreationForm(
            data={'username': user1.username, 'password1': user1.password, 'password2': user1.password}
        )
        self.assertIs(userForm.is_valid(), False)

        # Invalid password, password less than 8 characters
        user2 = User.objects.create_user(
            username='username2',
            password='abc4567'
        )
        userForm2 = CustomUserCreationForm(
            data={'username': user2.username, 'password1': user2.password, 'password2': user2.password}
        )
        self.assertIs(userForm2.is_valid(), False)

        # Invalid password, more than 8 characters but not alphanumeric
        user3 = User.objects.create_user(
            username='user3Valid',
            password='12121212'
        )
        userForm3 = CustomUserCreationForm(
            data={'username': user3.username, 'password1': user3.password, 'password2': user3.password}
        )
        self.assertIs(userForm3.is_valid(), False)


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

            # Tests the register_place.html file has an href to the index page
    def test_register_place_page_link_to_home_page(self):
        soup = BeautifulSoup(open('EvacApp/templates/EvacApp/register_place.html', 'r'), 'html.parser')
        link_text = ""
        for a in soup.find_all('a', href=True):
            link_text = a['href']
        # print("Link: " + link_text)
        self.assertEquals(link_text, '../')
