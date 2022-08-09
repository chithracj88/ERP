from django.shortcuts import render
from .models import AddStudent,AddStaff
from .forms import AddStudentForm,AddStaffForm
# Create your views here.

def StudentdetailsView(request):
    return render (request,'hod/studentdetails.html',{
        'students':AddStudent.objects.all()
    })
def StaffdetailsView(request):
    return render (request,'hod/staffdetails.html',{
        'staff':AddStaff.objects.all()
    })

def AddStudentViews(request):
    if request.method == 'POST':
        form = AddStudentForm(request.POST)
        if form.is_valid():
          new_student_name = form.cleaned_data['name'] 
          new_course = form.cleaned_data['course'] 
          new_cgpa = form.cleaned_data['cgpa'] 


          new_student=AddStudent(
            name = new_student_name,
            course = new_course,
            cgpa = new_cgpa,

          )
          new_student.save()
          return render(request, 'hod/addstudent.html',{
            'form':AddStudentForm(),
            'success': True
          })
        else:
            form=AddStudentForm()
        return render (request,'hod/addstudent.html',{
            'form':AddStudentForm()
        })     

            


