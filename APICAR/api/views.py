from django.shortcuts import render
from rest_framework.views import APIView

# Create your views here.
class Home(APIView):
    template_name = "Home/home.html"
    def get(self,request):
        return render(request,self.template_name)

class Admin(APIView):
    template_name = "Admin/admin.html"
    def get(self,request):
        return render(request,self.template_name)

class Login(APIView):
    template_name = "Authentication/login.html"
    def get(self,request):
        return render(request,self.template_name)

class Register(APIView):
    template_name = "Authentication/register.html"
    def get(self,request):
        return render(request,self.template_name)