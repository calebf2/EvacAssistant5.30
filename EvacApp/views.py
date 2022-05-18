from django.http import HttpResponse
from django.shortcuts import render
from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import forms
from .forms import CustomUserCreationForm, PlaceProfileForm


# Create your views here.

def index(request):
    return render(request, 'EvacApp/index.html', context={})


def register(request):
    if request.POST.get('registerForm') == 'Register':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            # messages.success(request, f'Your account has been created. You are now able to login.')
            return redirect('/')
    else:
        form = CustomUserCreationForm()
    context = {
        'form': form
    }
    return render(request, 'EvacApp/register.html', context)


def register_place(request):
    if request.POST == 'POST':
        form = PlaceProfileForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, f'The profile for your safe space has been created.')
            return redirect('')

    else:
        form = PlaceProfileForm()
    context = {
        'form': form
    }
    return render(request, 'EvacApp/register_place.html', context)

def map(request):
    if request.POST == 'POST':
        form = DisplayMap(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, f'Map Display.')
            return redirect('')

    else:
        form = DisplayMap()
    context = {
        'form': form
    }
    return render(request, 'EvacApp/map.html', context)
