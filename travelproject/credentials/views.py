from django.contrib import messages,auth

from django.contrib.auth.models import User
from django.shortcuts import render, redirect


# Create your views here.
def login(request):
    if request.method=='POST':
        a=request.POST['username']
        e=request.POST['password']
        user=auth.authenticate(username=a,password=e)
        if user is not None:
            auth.login(request,user)
            return redirect('/')
        else:
            messages.info(request,"invalid login entry")
            return redirect('login')
    return render(request,'login.html')
def register(request):
    if request.method== 'POST':
        a=request.POST['username']
        b=request.POST['first_name']
        c=request.POST['last_name']
        d=request.POST['email']
        e=request.POST['password']
        f=request.POST['password1']
        if e==f:
            if User.objects.filter(username=a).exists():
                messages.info(request,"sorry username taken")
                return redirect('register')
            elif User.objects.filter(email=d).exists():
                messages.info(request,"sorry mailid already exist")
                return redirect('register')
            else:
                user = User.objects.create_user(username=a, first_name=b, last_name=c, email=d, password=e)
                user.save();
                return redirect('login')

        else:
            messages.info(request,'password not matching')
            return redirect('register')
        return redirect('/')
    return render(request,'register.html')

def logout(request):
    auth.logout(request)
    return redirect('/')
