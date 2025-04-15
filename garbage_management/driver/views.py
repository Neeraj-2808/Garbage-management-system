from django.shortcuts import render

# Create your views here.
from django.shortcuts import render,redirect

from django.views import View

from .models import Driver

from .forms import DriverRegisterForm

from django . db import transaction

from authentication.models import Profile

from user.utility import get_password,send_email

from django.shortcuts import get_object_or_404

from django.conf import settings

import threading





# Create your views here.
class DriverView(View):

    def get(self,request,*args,**kwargs):

        # drivers = Driver.objects.all()

        drivers= Driver.objects.filter(active_status = True)

        return render(request,'garbage/driver_list.html',{'drivers':drivers})
    
class DriverFormView(View):

    def get(self,request,*args,**kwargs):

        form = DriverRegisterForm()


        return render(request,'garbage/driver_register.html',{'form':form})
    def post(self,request,*args,**kwargs):

        form = DriverRegisterForm(request.POST,request.FILES)

        
        if form.is_valid():

            with transaction.atomic():
            
                user= form.save(commit=False)

                username = user.email

                password = get_password()

                print(password)

                profile=Profile.objects.create_user(username=username,password=password,role= 'Driver')

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

                return redirect('drivers')


        else:

            form = DriverRegisterForm()

            return render(request,'garbage/driver_register.html',{'form':form})
    

class DriverUpdateView(View):

    def get(self, request, *args, **kwargs):

        uuid = kwargs.get('uuid')

        drivers = get_object_or_404(Driver, uuid=uuid)

        form = DriverRegisterForm(instance=drivers)

        return render(request, 'garbage/driver_update.html', {'form': form})

    def post(self, request, *args, **kwargs):

        uuid = kwargs.get('uuid')

        drivers = get_object_or_404(Driver, uuid=uuid)

        form = DriverRegisterForm(request.POST, request.FILES, instance=drivers)

        if form.is_valid():

            form.save()

            return redirect('drivers')
        
        return render(request, 'garbage/driver_register.html', {'form': form})
    

class DriverDeleteView(View):

    def get(self, request, *args, **kwargs):
        # Fetch the driver by UUID
        uuid = kwargs.get('uuid')
        driver = get_object_or_404(Driver, uuid=uuid,active_status = True)
        return render(request, 'garbage/driver_delete_confirm.html', {'driver': driver})

    def post(self, request, *args, **kwargs):
        # Fetch the driver by UUID
        uuid = kwargs.get('uuid')
        driver = get_object_or_404(Driver, uuid=uuid,active_status = True)

        # Delete the driver
        driver.active_status = False
        driver.save()
  # This will now just mark is_deleted = True

        return redirect('drivers')  # Redirect to the driver list view
