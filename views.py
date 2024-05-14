from django.shortcuts import render,redirect
from django.http import HttpResponse
from .forms import *
from django.contrib import messages
from django.contrib.auth import authenticate,login as auth_login
from django.contrib.auth.models import User,auth
from django.contrib.auth.admin import UserAdmin

from django.contrib import auth
from django.contrib.auth import login

# Create your views here.
def index(request):
    return render(request,'index.html')




def result(request):
    return render(request,'result.html')



def schools(request):

    return render(request,"schools.html")


def selection(request):
    return render(request,'selection.html')

def aboutus(request):
    return render(request,'aboutus.html')


def registration(request):
 if request.method=='POST':
  reg = userCreationForm(request.POST)
  first_name=request.POST['first_name']
  midle_name=request.POST['midle_name']
  last_name=request.POST['last_name']
  date_of_birth=request.POST['date_of_birth']
  home_address=request.POST['home_address']
  physical_address=request.POST['physical_address']
  phone_number=request.POST['phone_number']
 
  if reg.is_valid():
    reg.save()
    return redirect('NextOfKin1')
 else:
     reg = userCreationForm()
     
    
     
           
          
            
 return render(request,"registration.html",{'reg':reg})



def NextOfKin1(request):
 if request.method=='POST':
  sql1= relative1createForm(request.POST)
 
 
  if sql1.is_valid():
    sql1.save()
    return redirect('NextOfKin2')

 else:
     sql1 = relative1createForm()
     
           
          
            
 return render(request,"relative.html",{'sql1':sql1})


def NextOfKin2(request):
 if request.method=='POST':
  sql2= relative2createForm(request.POST)
 
 
  if sql2.is_valid():
    sql2.save()
    return redirect('NextOfKin3')

 else:
     sql2 = relative2createForm()
     
           
          
            
 return render(request,"relative2.html",{'sql2':sql2})

def NextOfKin3(request):
 if request.method=='POST':
  sql3= relative3createForm(request.POST)
 
 
  if sql3.is_valid():
    sql3.save()
    return redirect('education')

 else:
     sql3 = relative2createForm()
     
           
          
            
 return render(request,"relative3.html",{'sql3':sql3})



def education(request):
    file = educationCreateForm()
    if request.method=='POST':
        file = educationCreateForm(request.POST,request.FILES)
        if file.is_valid():
            file.save()
            return redirect('home')
            
    else:
        file = educationCreateForm()      
            
    return render(request,"education.html",{'file':file})



def applicantinfo(request):
     
     data1 = registrationForm.objects.all()
     data2 = relative1Form.objects.all()
     data3 = relative2Form.objects.all()
     data4 = relative3Form.objects.all()
     data5 = educationForm.objects.all()
     context = {
        'data1':data1,
        'data2':data2,
        'data3':data3,
        'data4':data4,
        'data5':data5,
        
        
        
        
        
     }
      
  
     return render(request,'aplicantinfo.html',context)  
 
 
 
def userreg(request):
    if request.method == 'POST':
      form = RegisterForm(request.POST)
      if form.is_valid():
            form.save()
            return redirect('User')  # Redirect to login page after successful registration
    else:
         form = RegisterForm()
    return render(request, 'userlog.html',{'form':form})

       
    
  
  
def User(request):
    if request.method == 'POST':
      form = LoginForm(request.POST)
      if form.is_valid():
       username = form.cleaned_data['username']
       password = form.cleaned_data['password']
       user = authenticate(request, username=username, password=password)
       if user is not None:
            auth_login(request, user)
            return redirect('index')  # Redirect to home page after successful login
       else:
                # Authentication failed
                error_message = "Invalid username or password. Please try again."
                return render(request, 'User.html', {'form': form, 'error_message': error_message})
    else:
         form = LoginForm()

    return render(request,"user.html",{'form':form})


def userinfo(request):
     data = UserForm.objects.all()
     
     context = {
        'data':data,
        }
      
  
     return render(request,'userinfo.html',context) 
 
 
 
def home(request):
    return render(request,'home.html') 
  
 