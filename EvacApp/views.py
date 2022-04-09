from django.http import HttpResponse
from django.shortcuts import render
from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import forms
from .forms import CustomUserCreationForm


# Create your views here.

def index(request):
    return render(request, 'EvacApp/index.html', context={})


def register(request):
    if request.POST == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()

    else:
        form = UserCreationForm()
    context = {
        'form': form
    }
    return render(request, 'EvacApp/register.html', context)
