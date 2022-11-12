from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth import logout
from django.contrib.auth.models import User
from django.contrib import messages, auth
from django.contrib.auth.decorators import login_required
from schools.models import School
from django.contrib.auth import get_user_model

User = get_user_model()

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(
            username=username, password=password)

        if user is not None:
            auth.login(request, user)
            user_type = User.objects.filter(username=username).values_list('account_type',flat=True)
            print("user type:",user_type[0])
            if user_type[0] == "Driver":
                return render(request,'accounts/driver-dashboard.html')
            else:
                return render(request,'accounts/parent-dashboard.html')

        else:
            messages.warning(request, 'Invalid credentials')
            return redirect('login')

    return render(request, 'accounts/login.html')


def register(request):
    if request.method == 'POST':
        fullname = request.POST['fullname']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']
        account_type = request.POST['account_type']
        phone = request.POST['phone']
        location = request.POST['location']
        bus_route = request.POST['bus_route']
        school_name = request.POST['school_name']

        if password == confirm_password:
            if User.objects.filter(username=username).exists():
                messages.warning(request, 'Username already exists')
                return redirect('register')
            else:
                if User.objects.filter(email=email).exists():
                    messages.warning(request, 'Email already exists')
                    return redirect('register')
                else:
                    user = User.objects.create_user(
                        fullname=fullname, username=username,
                        email=email, password=password, account_type=account_type,
                        phone=phone,location=location
                    )
                    user.save()
                    school = School(school_name=school_name,bus_route=bus_route,user=user)
                    school.save()
                    messages.success(
                        request, 'Account registered successfully')
                    return redirect('login')
        else:
            messages.warning(request, 'Password donot match')
            return redirect('register')

    return render(request, 'accounts/register.html')

def logout_user(request):
    logout(request)
    return redirect('/')

def parent(request):
    return  render(request, 'accounts/parent-dashboard.html')

def driver(request):
    return  render(request, 'accounts/driver-dashboard.html')




    




