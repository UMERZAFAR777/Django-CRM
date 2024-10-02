from django.http import HttpResponse
from django.shortcuts import redirect,render,get_object_or_404
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from django.contrib.messages import *
from django.contrib.auth.models import User
from student.models import Student
from django.contrib.auth.decorators import login_required



def index(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        # Authenticate user
        user = authenticate(request, username=username, password=password)

        if user is not None:
            # Log in the user
            login(request, user)
            messages.success(request, 'You have been logged in!')
            return redirect('home')
        else:
            messages.error(request, 'There was an error. Please try again.')  
            return redirect('index')

    return render(request, 'index.html')  


def register(request):
    return render (request,'register.html')





def logout_user(request):
    print("Logout function called.")  # Debugging line
    logout(request)
    messages.success(request, 'You have been logged out.')
    return redirect('index')

def register(request):
    if request.method == "POST":
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']


        if password != password2:
            messages.success(request,'Both password doesnt match...!')
            return redirect ('register')
        
    try:
        user = User.objects.create_user(username= username,email=email,password=password)
        user.save()
        messages.success(request,'Register Successfully Sir..........!')
        return redirect ('index')
    except:
        pass
    return render (request,'register.html')    


@login_required(login_url = '/index')
def home(request):
    student = Student.objects.all()
    data = {
        'student':student,
    }
    return render(request, 'home.html',data)



def student_view(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        city = request.POST.get('city')

        student = Student(name = name,email = email,phone = phone,city = city)
        student.save()
        messages.success(request,'Record Add Successfully....!')
        return redirect ('home')
    return render (request,'student.html')


def student_show(request,pk):
    student = Student.objects.get(pk = pk)
    data = {
        'student':student
    }
    return render (request,'student_show.html',data)

def delete_student(request, student_id):
    student = get_object_or_404(Student, id=student_id)
    student.delete()  
    return redirect('home')



def edit_student(request, student_id):
    student = get_object_or_404(Student, id=student_id)
    
    if request.method == 'POST':
        
        student.name = request.POST.get('name', student.name)
        student.email = request.POST.get('email', student.email)
        student.phone = request.POST.get('phone', student.phone)
        student.city = request.POST.get('city', student.city)
        student.save()
        
        messages.success(request, 'Student details updated successfully!')
        return redirect('home') 
    
    
    return render(request, 'edit_student.html', {'student': student})  
