from django.shortcuts import render, redirect
from .models import *
from .forms import *
from django.contrib.auth import authenticate, login
from django.contrib import messages

# Create your views here.
def home(request):
    return render(request, 'Home/home.html')

def register(request):
 if request.method == 'POST':
  form = UserRegisterForm(request.POST)
  if form.is_valid():
   form.save()
   username = form.cleaned_data['username']
   messages.success(request, 'Usuario {username} creado')
   return redirect('login')
 else:
  form = UserRegisterForm()
 context = { 'form' : form }
 return render(request, 'Authentication/register.html', context)
