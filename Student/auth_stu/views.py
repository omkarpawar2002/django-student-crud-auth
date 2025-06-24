from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages

# Create your views here.

def signup(request):
    form = UserCreationForm()
    if(request.method == 'POST'):
        form = UserCreationForm(request.POST)
        if(form.is_valid()):
            form.save()
            return redirect('signin')
    template_name = 'auth_stu/signup.html'
    context = {'form':form}
    return render(request,template_name,context)

def signin(request):
    next_url = request.POST.get('next')

    if(request.method == 'POST'):
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username,password=password)
        print("user",user)
        print("username",username)
        print("password",password)
        if (user is not None):
            login(request,user)
            return redirect('show_student')
        else:
            messages.error(request, 'Invalid username or password.')
    template_name = 'auth_stu/signin.html'
    context = {}
    return render(request,template_name,context)

def signout(request):
    logout(request)
    return redirect('signin')

