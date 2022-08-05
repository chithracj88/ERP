from django.urls import path
from . import views

urlpatterns = [
    path('', views.HomeView, name="home"),
    path('about/', views.AboutView, name="about"),
    path('login/', views.LoginView, name="login"),
    path('logout/', views.LogoutView, name="logout"),
    
]