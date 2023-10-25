from django.urls import path
from . import views
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path('', views.home, name='home'),
    path('register/', views.register, name='register'),
    path('login/', LoginView.as_view(template_name='Authentication/login.html'), name= 'login'),
    path('logout/', LogoutView.as_view(template_name='Authentication/logout.html'), name= 'logout'),
    path('dashboard/', views.dashboard_view, name='dashboard'),

]
