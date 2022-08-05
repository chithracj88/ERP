from django.contrib import admin
from .models import Location,Address,Profile,SessionYearModel,Department,Course,Staff,Student,Enroll

# Register your models here.
admin.site.register (Location)
admin.site.register (Address)
admin.site.register (Profile)
admin.site.register (SessionYearModel)
admin.site.register (Department)
admin.site.register (Course)
admin.site.register (Staff)
admin.site.register (Student)
admin.site.register (Enroll)
