from django.shortcuts import render,redirect,get_object_or_404

from django.views import View

from authentication.models import Profile

from .forms import GarbageRegisterForm

from user.forms import UserRegisterForm

from user.utility import get_password,send_email

from django . db import transaction

from .models import Garbage

from user.models import Users

from django.db.models import Sum,Count

from datetime import date

from django.utils import timezone

from trucks.models import GarbageTruck

from complaints.models import Complaint

#email related imports

from django.core.mail import EmailMultiAlternatives

from django.template.loader import  render_to_string

from django.conf import settings

import threading

from django.views.decorators.csrf import csrf_exempt

from django.utils.decorators import method_decorator

from django.core.mail import send_mail

from django.http import HttpResponseBadRequest

from payment.models import Payment


# Create your views here.

class Base(View):
    
    def get(self, request, *args, **kwargs):
        try:
            # Get the 'Users' object using the profile of the logged-in user
            customer = Users.objects.get(profile=request.user)
        except Users.DoesNotExist:
            customer = None  # In case no Users object exists for this user
        
        return render(request, 'base.html', {'customer': customer})


    
class DashboardView(View):
    
    def get(self,request,*args,**kwargs):
        
        # Get today's date
        today = timezone.now().date()

        # Calculate the total quantity for today's garbage
        garbages_today = Garbage.objects.filter(pick_up_date=today)
        total_quantity = garbages_today.aggregate(Sum('quantity'))['quantity__sum']

        # If no garbage is found for today, set the total_quantity to 0
        if total_quantity is None:
            total_quantity = 0

        # Calculate the sum of active trucks
        active_trucks_count = GarbageTruck.objects.filter(active_status=True).count()

        # Calculate the sum of active trucks
        complaint_count = Complaint.objects.filter(active_status=True).count()

        # Render the template and pass the total quantity to the context
        return render(request, 'garbage/dashboard.html', {'total_quantity': total_quantity,'active_trucks_count': active_trucks_count,'complaint_count':complaint_count})

class MapView(View):
    
    def get(self, request, *args, **kwargs):
        # district_data = [
        #     {"name": "Thiruvananthapuram", "lat": 8.5241, "lng": 76.9366, "color": "green"},
        #     {"name": "Ernakulam", "lat": 9.9816, "lng": 76.2999, "color": "blue"},
        #     {"name": "Kozhikode", "lat": 11.2588, "lng": 75.7804, "color": "red"},
        #     {"name": "Kannur", "lat": 11.8745, "lng": 75.3704, "color": "purple"},
        # ]
        return render(request, 'garbage/map.html')

 

class StatusUpdateView(View):

    def post(self,request,*args,**kwargs):

        status=request.POST.get('status')

        print(status)

        return render(request,'garbage/home.html',context={'status':status}) 
    
class SettingsView(View):

    def get(self,request,*args,**kwargs):

        return render(request,'settings/settings.html') 
class ReportsView(View):

    def get(self,request,*args,**kwargs):

        return render(request,'settings/reports.html') 
class GalleryView(View):

    def get(self,request,*args,**kwargs):

        return render(request,'settings/gallery.html') 
class AboutView(View):

    def get(self,request,*args,**kwargs):

        return render(request,'settings/about.html') 
class FaqView(View):

    def get(self,request,*args,**kwargs):

        return render(request,'settings/faq.html')
    
class GarbageRegisterView(View):

    def get(self,request,*args,**kwargs):

        form = GarbageRegisterForm()

        return render(request,'garbage/garbage_register.html',{'form':form}) 
    
    def post(self,request,*args,**kwargs):

        form  = GarbageRegisterForm(request.POST,request.FILES)

        # user_form = UserRegisterForm(request.POST,request.FILES)

        customer = Users.objects.get(profile=request.user)


        if form.is_valid():

            with transaction.atomic():
            
                garbage = form.save(commit=False)

                garbage.customer = customer

                garbage.save()

                #payment section

                Payment.objects.create(
                garbage=garbage,
                amount=50,
                customer=garbage.customer  # or any other logic to set the customer
                )

                subject = 'Pickup Confirmation'

                recepients = [customer.email]

                print(customer.email)

                template = 'email/pickup-credentials.html'

                context = {'name':customer.name,'garbage_type':garbage.garbage_type,'status':garbage.status,'quantity':garbage.quantity,
                           'pick_up_date':garbage.pick_up_date,'address':garbage.address}

                # send_email(subject,recepients,template,context)

                thread = threading.Thread(target=send_email,args=(subject,recepients,template,context))

                thread.start()

                return redirect('razorpay',uuid=garbage.uuid)
        else:

            data = {'form' : form}

            return render(request,'user/registration_form.html',context=data)
        


class GarbageView(View):

    def get(self, request):
        user = request.user

        if user.role == "Admin":
            # Admin can see all garbage entries
            garbages = Garbage.objects.filter(active_status= True).order_by('-created_at')
        elif user.role == "Driver":
            garbages = Garbage.objects.filter(active_status= True).order_by('-created_at')
        elif user.role == "User":
            # Access the profile of the user (correctly getting profile here)
            customer = Users.objects.get(profile=request.user)  # This works if the user has a related profile
            # Assuming customer field in Garbage refers to the User model
            garbages = Garbage.objects.filter(customer=customer).order_by('-created_at')
        else:
            # Other roles (if any) get no access
            garbages = Garbage.objects.none()

        return render(request, 'garbage/garbage_list.html', {'garbages': garbages})
    
class GarbageSectionView(View):

    def get(self, request):
    
        return render(request, 'garbage/garbage_section.html')
    


# @csrf_exempt
# def update_garbage_status(request, uuid):
#     if request.method == "POST":
#         garbage = get_object_or_404(Garbage, uuid=uuid)
#         new_status = request.POST.get("status")
#         if new_status:
#             garbage.status = new_status
#             garbage.save()
#             return redirect('garbage-list')
#         return HttpResponseBadRequest("Missing status value.")
#     return HttpResponseBadRequest("Invalid request method.")


@csrf_exempt
def update_garbage_status(request, uuid):
    if request.method == "POST":
        garbage = get_object_or_404(Garbage, uuid=uuid)
        new_status = request.POST.get("status")

        if new_status:
            garbage.status = new_status
            garbage.save()

            # Send email only if status is Cancelled and role is Admin or Driver
            if new_status == "Cancelled":
                user_role = request.user.role   # Assuming user has related Profile model

                if user_role in ["Admin", "Driver"]:
                    subject = 'Pickup Cancelled'
                    recipients = [garbage.customer.email]

                    print(garbage.customer.email)  # For debugging/logging

                    template = 'email/pickup-cancelled.html'  # Your cancellation email template

                    context = {
                        'name': garbage.customer.name,
                        'garbage_type': garbage.garbage_type,
                        'status': garbage.status,
                        'quantity': garbage.quantity,
                        'pick_up_date': garbage.pick_up_date,
                        'address': garbage.address,
                    }

                    thread = threading.Thread(target=send_email, args=(subject, recipients, template, context))
                    thread.start()

            return redirect('garbage-list')

        return HttpResponseBadRequest("Missing status value.")

    return HttpResponseBadRequest("Invalid request method.")

class GarbageUpdateView(View):

    def get(self, request, *args, **kwargs):

        uuid = kwargs.get('uuid')

        garbages = get_object_or_404(Garbage, uuid=uuid)

        form = GarbageRegisterForm(instance=garbages)

        return render(request, 'garbage/garbage_update.html', {'form': form})

    def post(self, request, *args, **kwargs):

        uuid = kwargs.get('uuid')

        garbages = get_object_or_404(Garbage, uuid=uuid)

        form = GarbageRegisterForm(request.POST, request.FILES, instance=garbages)

        if form.is_valid():

            form.save()

            return redirect('garbage-list')
        
        return render(request, 'garbage/garbage_register.html', {'form': form})
    

class GarbageDeleteView(View):

    def get(self, request, *args, **kwargs):
        # Fetch the user by UUID
        uuid = kwargs.get('uuid')
        garbages = get_object_or_404(Garbage, uuid=uuid,active_status = True)
        return render(request, 'user/user_delete_confirm.html', {'garbages': garbages})

    def post(self, request, *args, **kwargs):
        # Fetch the users by UUID
        uuid = kwargs.get('uuid')
        garbages = get_object_or_404(Garbage, uuid=uuid,active_status = True)

        # Delete the garbages
        garbages.active_status = False
        garbages.save()
  # This will now just mark is_deleted = True

        return redirect('garbage-list')  # Redirect to the driver list view
    
# def calculate_today_garbage(request):
#     today = timezone.now().date()
#     print(f"Today's date: {today}")  # Debugging print statement

#     # Filter for today's garbage
#     garbages_today = Garbage.objects.filter(pick_up_date=today)
#     print(f"Filtered garbages for today: {garbages_today}")  # Debugging print statement

#     # Calculate the total quantity for today
#     total_quantity = garbages_today.aggregate(Sum('quantity'))['quantity__sum']
#     print(f"Total quantity for today: {total_quantity}")  # Debugging print statement

#     print(f"Rendering home with total_quantity: {total_quantity}")

#     # If there's no data, set total_quantity to 0
#     if total_quantity is None:
#         total_quantity = 0
#     return render(request, 'garbage/home.html', {'today': today, 'total_quantity': total_quantity})

class HomeView(View):

    def get(self,request,*args,**kwargs):

        customer = Users.objects.get(profile=request.user)

        return render(request,'garbage/home.html',{'customer':customer}) 







