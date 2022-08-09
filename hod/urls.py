from django.urls import path
from .import views

app_name = "hod"
urlpatterns = [
  path('studentdetails/',views.StudentdetailsView, name="studentdetails"),
  path('staffdetails/',views.StaffdetailsView, name="staffdetails"),
  path('addstudent/',views.AddStudentViews,name='addstudent')
,]