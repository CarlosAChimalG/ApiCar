from django.shortcuts import render, redirect
from .models import *
from .forms import *
from django.core.mail import send_mail
from django.shortcuts import render
from django.template.loader import render_to_string

# Create your views here.
def home(request):
    return render(request, 'Home/home.html')

def register(request):
 if request.method == 'POST':
  form = UserRegisterForm(request.POST)
  if form.is_valid():
   form.save()
   username = form.cleaned_data['username']
   print(request.POST)
   subject = 'Registro Éxitoso'
   message = ''
   from_email = 'chimalcarlos261198@gmail.com'
   recipient_list = [request.POST['email']]
   context = {
        'user': request.POST['username'],
        'password': request.POST['password1'],
   }
   html_content = render_to_string('Mail/registerMail.html', context)
   send_mail(subject, message, from_email, recipient_list, fail_silently=False, html_message=html_content)
   return redirect('login')
 else:
  form = UserRegisterForm()
 context = { 'form' : form }
 return render(request, 'Authentication/register.html', context)
