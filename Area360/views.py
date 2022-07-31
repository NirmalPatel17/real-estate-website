import email
import uuid
from django.shortcuts import redirect, render
from django.contrib import messages
from django.conf import settings
from django.core.mail import send_mail
from .models import *
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

# Create your views here.
def index(request):
    return render(request,'index.html')

def user_register(request):

    if request.method == 'POST':
        Ownership = request.POST.get('ownership')
        FirstName = request.POST.get('firstname')
        LastName = request.POST.get('lastname')
        Mobile = request.POST.get('mobile')
        Email = request.POST.get('email')
        Password = request.POST.get('password')
        list1 = [Ownership,FirstName,LastName,Mobile,Email,Password]
        try:
            if len(Password) < 6:
                messages.error(request, 'Password is too short')
            else:
                if User.objects.filter(email=Email).first():
                    messages.success(request, 'Username is taken')
                    return redirect('/auth/register')
                auth_token = str(uuid.uuid4())
                user_obj = User(first_name=FirstName,last_name=LastName,email=Email,mobile=Mobile,ownership=Ownership,email_verification_token=auth_token)
                user_obj.set_password(Password)
                user_obj.save()
                send_verification_mail(Email, auth_token)
                return redirect('/')
        except Exception as e:
            print(e)
            messages.error(request, e)


    return render(request,'register.html')

def send_verification_mail(Email,token):
    subject = "Account varification"
    message = f'Hi paste the link to verify your account http://127.0.0.1:8000/verify/{token}'
    email_from = settings.EMAIL_HOST_USER
    recipient_list = [Email]
    send_mail(subject, message, email_from, recipient_list)

def verify(request, auth_token):
    try:
        user_obj = User.objects.filter(email_verification_token=auth_token).first()

        if user_obj.is_email_verified:
            messages.success(request, 'Your account is already verified')
            return redirect('/auth/login')

        if user_obj:
            user_obj.is_email_verified = True
            user_obj.save()
            messages.success(request, 'Your account has been verified')
            return redirect('/auth/login')
        else:
            messages.error(request, 'error')
            return redirect('/')
    except Exception as e:
        print(e)
        return redirect('/')

def user_login(request):
    if request.method == 'POST':
        Email = request.POST.get('email')
        Password = request.POST.get('password')

        user_obj = User.objects.filter(email = Email).first()

        if user_obj is None:
            messages.error(request, 'User not found')
            return redirect('/auth/login')
        
        user_obj = User.objects.filter(email=Email).first()

        if not user_obj.is_email_verified:
            messages.error(request, 'User is not verified pls check your mail')
            return redirect('/auth/login')

        user = authenticate(email = Email,password = Password)
        if user is not None:
            login(request, user)
            messages.success(request, 'Login successfully')
            return redirect('/auth/login')
        else:
            messages.error(request, 'Wrong password or email')
            return redirect('/auth/login')

    return render(request, 'login.html')

def user_logout(request):
    logout(request)
    messages.success(request, 'logged out')
    return redirect('/')

def property(request):
    return render(request,'property.html')

def propertysingle(request):
    return render (request,'property-single.html')

def about(request):
    return render(request,'about.html')

def contact(request):
    return render(request,'contact.html')
