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
  #  send_mail(subject, message, from_email, recipient_list, fail_silently=False, html_message=html_content)
   return redirect('login')
 else:
  form = UserRegisterForm()
 context = { 'form' : form }
 return render(request, 'Authentication/register.html', context)

def dashboard_view(request):
  packageGrande = Question.objects.filter(package="Grande").count()
  packageMediano = Question.objects.filter(package="Mediano").count()
  packagePequeño = Question.objects.filter(package="Pequeño").count()
  
  packagingBolsa = Question.objects.filter(packaging="En bolsa").count()
  packagingCaja = Question.objects.filter(packaging="En Caja").count()
  packagingPlastico = Question.objects.filter(packaging="En plástico").count()
  
  personFamilia = Question.objects.filter(person="Para la familia").count()
  personMismo = Question.objects.filter(person="Para si mismo").count()
  personHogar = Question.objects.filter(person="Para el hogar").count()
  
  sendSi = Question.objects.filter(send="Si").count()
  sendNo = Question.objects.filter(send="No").count()
  
  categoryEyT = Question.objects.filter(category="Electrónicos y tecnología").count()
  categoryJyE = Question.objects.filter(category="Juguetes y entretenimiento").count()
  categoryA = Question.objects.filter(category="Alimentos").count()
  categoryAH = Question.objects.filter(category="Artículos para el hogar").count()
  categoryR = Question.objects.filter(category="Ropa").count()
  categoryHC = Question.objects.filter(category="Higiene y cuidado personal").count()
  
  reason_purchaseHM = Question.objects.filter(reasonPurchase="Historia de la marca").count()
  reason_purchaseRM = Question.objects.filter(reasonPurchase="Reputación de la marca").count()
  reason_purchaseC = Question.objects.filter(reasonPurchase="Calidad").count()
  reason_purchaseP = Question.objects.filter(reasonPurchase="Precio").count()
  
  markNike = Question.objects.filter(mark="Nike").count()
  markApple = Question.objects.filter(mark="Apple").count()
  markSamsung = Question.objects.filter(mark="Samsung").count()
  markBimbo = Question.objects.filter(mark="Bimbo").count()
  markMcDonald = Question.objects.filter(mark="McDonald's").count()
  
  articleVU = Question.objects.filter(article="Varios usos").count()
  articleUD = Question.objects.filter(article="Un único y desechable").count()
  articleUND = Question.objects.filter(article="Un único uso y no desechable").count()
  
  context = {
        'package_labels': ['Grande', 'Mediano', 'Pequeño'],
        'package_values' : [packageGrande, packageMediano, packagePequeño],
        'packaging_labels': ['En bolsa', 'En Caja', 'En plástico'],
        'packaging_values' : [packagingBolsa, packagingCaja, packagingPlastico],
        'person_labels': ['Para la familia', 'Para si mismo', 'Para el hogar'],
        'person_values' : [personFamilia, personMismo, personHogar],
        'send_labels': ['Si', 'No'],
        'send_values' : [sendSi, sendNo],
        'category_labels': ['Electrónicos y tecnología', 'Juguetes y entretenimiento', 'Alimentos', 'Artículos para el hogar', 'Ropa', 'Higiene y cuidado personal'],
        'category_values' : [categoryEyT, categoryJyE, categoryA, categoryAH, categoryR, categoryHC],
        'reason_purchase_labels': ['Historia de la marca', 'Reputación de la marca', 'Calidad', 'Precio'],
        'reason_purchase_values' : [reason_purchaseHM, reason_purchaseRM, reason_purchaseC, reason_purchaseP],
        'mark_labels': ['Nike', 'Apple', 'Samsung', 'Bimbo', "McDonald's"],
        'mark_values' : [markNike, markApple, markSamsung, markBimbo, markMcDonald],
        'article_labels': ['Varios usos', 'Un único y desechable', 'Un único uso y no desechable'],
        'article_values' : [articleVU, articleUD, articleUND],
   }
  return render(request, 'Admin/dashboard.html',context)
