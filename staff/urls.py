from django.urls import path
from .import views


app_name = "staff"

urlpatterns = [
    path('staff_home',views.staff_home,name='staff_home'),  
    path('add_stafflocation',views.add_stafflocation,name='add_stafflocation'),
    path('add_staffaddress',views.add_staffaddress,name='add_staffaddress'),
    path('add_staffprofile',views.add_staffprofile,name='add_staffprofile'),
    path('manage_profile',views.manage_staffprofile,name='manage_profile'),

]

