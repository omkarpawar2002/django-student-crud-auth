from django.shortcuts import render,redirect
from .forms import StudentForm
from .models import Students
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required(login_url='/signin/')
def add_stu(request):
    form = StudentForm()
    if(request.method == 'POST'):
        form = StudentForm(request.POST)
        if(form.is_valid()):
            form.save()
            return redirect('show_student')
    template_name = 'stu_info/add_stu.html'
    context = {'form':form}
    return render(request,template_name,context)

# @login_required(login_url='/signin')
def show_stu(request):
    stu = Students.objects.all()
    template_name = 'stu_info/show_stu.html'
    context = {'obj':stu}
    return render(request,template_name,context)

def update_stu(request,pk):
    obj = Students.objects.get(stu_id = pk)
    form = StudentForm(instance=obj)
    if(request.method == 'POST'):
        form = StudentForm(request.POST,instance=obj)
        if(form.is_valid()):
            form.save()
            return redirect('show_student')
    template_name = 'stu_info/update_stu.html'
    context = {'form':form}
    return render(request,template_name,context)

def delete_stu(request,pk):
    obj = Students.objects.get(stu_id = pk)
    if(obj is not None):
        if(request.method == 'POST'):
            obj.delete()
            return redirect('show_student')
    template_name = 'stu_info/delete_stu.html'
    context = {'obj':obj}
    return render(request,template_name,context)