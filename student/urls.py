from django.urls import path
from .import views


app_name = "student"

urlpatterns = [
    path('student_home',views.student_home,name='student_home'),
    path('student_profile',views.student_profile,name='student_profile'),
]
