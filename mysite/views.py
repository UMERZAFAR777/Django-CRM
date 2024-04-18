from django.http import HttpResponse
from django.shortcuts import redirect,render
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from .forms import SignUpForm,AddRecordForm
from website.models import Record
def home(request):
    records = Record.objects.all()
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate (request,username = username,password = password)
        if user is not None:
            login(request,user)
            messages.success(request,'You have been logged in ...!')
            return redirect ('home')
        else:
            messages.success(request,'There was a error plz try again....!')
            return redirect ('home')
        
    return render (request,'home.html',{'records':records})


def logout_user(request):
    logout(request)
    messages.success(request,'You have been logged out..!')
    return redirect ("home")


def register_user(request):
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data ['username']
            password = form.cleaned_data ['password1']
            user = authenticate(username = username ,password = password)
            login (request,user)
            messages.success(request,'You have been successfully register')
            return redirect ('home')
    else:
        form = SignUpForm()
        return render (request,'register.html',{'form':form})     
        
    return render (request,'register.html',{'form':form})

def record_user(request,pk):
    if request.user.is_authenticated:
        customer_record = Record.objects.get(id = pk)
    else:
        messages.success(request,'You have to login first......')
        return redirect ('home')    
    return render (request,'record.html',{'customer_record':customer_record})

def delete_user(request,pk):
    if request.user.is_authenticated:
        delete_it = Record.objects.get(id = pk)
        delete_it.delete()
        messages.success(request,'Profile is deleted')
        return redirect ('home')
    else:
        messages.success(request,'You have to login first......')
        return redirect ('home')     
    
def addrecord(request):
    form = AddRecordForm(request.POST or None)
    if request.user.is_authenticated:
        if request.method == "POST":
            if form.is_valid():
                form.save()
                messages.success(request,'Profile is added')
                return redirect ('home')
        else:    
            return render (request,'addrecord.html',{'form':form})
    else:    
        messages.success(request,'You have to login first......')
        return redirect ('home')  


def updaterecord_user(request,pk):
    if request.user.is_authenticated:
        current_record = Record.objects.get(id = pk)
        form = AddRecordForm(request.POST or None ,instance=current_record)
        if form.is_valid():
            form.save()
            messages.success(request,'Profile is updated')
            return redirect ('home')
        return render (request,'updaterecord.html',{'form':form})
    else:
        messages.success(request,'You have to login first......')
        return redirect ('home') 






