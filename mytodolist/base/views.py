from django.shortcuts import render,redirect
from django.contrib import messages
from django.http import HttpResponse
from django.db.models import Q , Count
from .models import Tasks
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout,forms
from .forms import SigninForm

# Create your views here.


# def home(request):
#     context={'home':'hello'}
#     return render(request,'base/home.html',context)


def loginUser(request):
    page='login'
    #user=User.objects.get(username=username)
    if request.method=='POST':
        if request.method== 'POST':
            username=request.POST.get('username')
            password=request.POST.get('password')
            try:
                user=User.objects.get(username=username)
            except:
                messages.error(request,'user dosnt exist')

            user=authenticate(request,username=username,password=password)     

            if user is not None:
                login(request,user)
                return redirect('home')
            else:
                messages.error(request,"username or password is not correct")
    return render(request,'base/login.html',{'page':page})

def logoutUser(request):
    logout(request)
    return redirect('home')




def registerUser(request):
    page='register'
    form=SigninForm()
    if request.method=='POST':
      form=SigninForm(request.POST)
      if form.is_valid():
          form.save()
          
          return redirect('home')
    else:
          messages.error(request,'An error occured ')


    return render(request,'base/login.html',{'form':form})



def displaytasks(request):

    tasks=Tasks.objects.all()
    context={'tasks':tasks}
    return render(request,'base/home.html',context)