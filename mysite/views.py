from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from record.models import Student
from mysite.forms import StudentForm


def login_user(request):
    if request.method == "POST":
        identity = request.POST.get('username')
        password = request.POST.get('password')
        user = None

        if '@' in identity:
            try:
                user_obj = User.objects.get(email=identity)
                user = authenticate(request, username=user_obj.username, password=password)
            except User.DoesNotExist:
                user = None
        else:
            user = authenticate(request, username=identity, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'There was an error in Email / Username or Password')

    return render(request, 'registration/login.html',{'user':request.user})


def register(request):
    if request.method == "POST":
        email = request.POST.get('email')
        username = request.POST.get('username')
        password = request.POST.get('password')
        password2 = request.POST.get('password2')

        if password != password2:
            messages.error(request, 'Passwords do not match!')
            return redirect ('register')

        if User.objects.filter(email=email).exists():
            messages.error(request, 'Email already taken!')
            return redirect ('register')

        if User.objects.filter(username=username).exists():
            messages.error(request, 'Username already taken!')
            return redirect ('register')

        user = User.objects.create_user(email=email, username=username)
        user.set_password(password)
        user.save()

        messages.success(request, 'Account created successfully! Please log in.')
        return redirect('login') 

    return render(request, 'register.html')




def home(request):
    student = Student.objects.all()
    data = {
        'student':student,
    }
    return render (request,'home.html',data)


def logout_user(request):
    logout(request,)
    return redirect ('login')


def studentrecord(request,pk):
    student = Student.objects.get(pk = pk)

    data = {
        'student':student
    }

    return render (request,'studentrecord.html', data)



def addrecord(request):
    if request.method == "POST":
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        phone_number = request.POST.get('phone_number')
        city = request.POST.get('city')

        eu = Student(first_name = first_name , last_name = last_name , email = email , phone_number = phone_number , city = city)
        eu.save()

        messages.success (request,'Rocord Add Successfully........!')
        return redirect ('home')

    return render (request,'addrecord.html')




def delete(request,pk):
    student = Student.objects.get(pk = pk)
    student.delete()
    messages.success (request,'Record Deleted Successfully........!')
    return redirect ('home')




def editrecord(request, pk):
    try:
        student = Student.objects.get(pk=pk)
    except Student.DoesNotExist:
        messages.error(request, "Record not found.")
        return redirect('home')

    if request.method == "POST":
        form = StudentForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            messages.success(request, 'Record edited successfully!')
            return redirect('home')  
    else:
        form = StudentForm(instance=student)

    return render(request, 'editrecord.html', {'form': form})









