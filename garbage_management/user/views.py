from django.shortcuts import render,redirect

from django.views import View

from .models import Users

from .forms import UserRegisterForm

from django . db import transaction

from authentication.models import Profile

from .utility import get_password,send_email

#email related imports

from django.core.mail import EmailMultiAlternatives

from django.template.loader import  render_to_string

from django.conf import settings

import threading

import datetime

# Create your views here.

class UserView(View):

    def get(self,request,*args,**kwargs):

        # users = Driver.objects.all()

        users= Users.objects.filter(active_status = True)

        return render(request,'user/user_list.html',{'users':users})
class UserRegistration(View):
    
    def get(self,request,*args,**kwargs):

        form =  UserRegisterForm()

        data = {'form' : form}
        
        return render(request,'user/registration_form.html',context=data)

    def post(self,request,*args,**kwargs):

        form  = UserRegisterForm(request.POST,request.FILES)

        if form.is_valid():

            with transaction.atomic():
            
                user= form.save(commit=False)

                username = user.email

                password = get_password()

                print(password)

                profile=Profile.objects.create_user(username=username,password=password,role= 'User')

                user.profile = profile

                user.save()

                #sending login credentails to user through mail

                subject = 'Login Credentials'

                recepients = [user.email]

                template = 'email/login-credentials.html'

                context = {'name' : f'{user.name}','username':username,'password': password}

                # send_email(subject,recepients,template,context)

                thread = threading.Thread(target=send_email,args=(subject,recepients,template,context))

                thread.start()

                return redirect('dashboard')
        else:

            data = {'form' : form}

            return render(request,'customer/registration_form.html',context=data)
        