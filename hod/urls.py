from django.urls import path
from .import views


app_name = "hod"

urlpatterns = [
    #session year
    path('session_year',views.SessionView.as_view(),name='session_year'),
    #login and registration
    path('admin_home',views.admin_home,name='admin_home'),
    path('register_user',views.Register.as_view(),name="register_user"),
    
    #department
    path('add_department',views.AddDepartment,name='add_department'),
    path('list_department',views.All_Department, name='list_department'),
    path('<int:pk>/delete_department',views.DepartmentDelete.as_view(),name='delete_department'),
    #course
    path('add_course',views.add_course,name='add_course'),
    path('manage_course',views.manage_course,name='manage_course'),
    path('<int:pk>/delete_course',views.CourseDelete.as_view(), name='delete_course'),
    #staff
    path('assign_staff',views.assign_staff,name='assign_staff'),
    path('manage_staff',views.manage_staff,name='manage_staff'),
    path('<int:pk>/delete_staff',views.StaffDelete.as_view(), name='delete_staff'),
    path('<pk>/update_staff',views.StaffUpdate.as_view(), name='update_staff'),
    #student
    path('enroll',views.enroll,name='enroll'),
    path('student',views.StudentView.as_view(),name='student'),
    path('manage_student',views.manage_student,name='manage_student'),
    path('<int:pk>/delete_student',views.StudentDelete.as_view(), name='delete_student'),
    path('<pk>/update_student',views.StudentUpdate.as_view(), name='update_student'),
   ]
