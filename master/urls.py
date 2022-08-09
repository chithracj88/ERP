from django.urls import path
from .import views

app_name = "master"
urlpatterns = [
    path('', views.HomeView, name="home"),
    path('contact/', views.AboutView, name="contact"),
    path('login/', views.LoginView, name="login"),
    path('logout/', views.LogoutView, name="logout"),
    path('registration/', views.RegistrationView, name="registration"),
]