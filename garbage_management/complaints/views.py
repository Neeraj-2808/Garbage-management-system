from django.views import View

from .models import Complaint

from user.models import Users

from .forms import ComplaintRegisterForm

from django.shortcuts import render,redirect,get_object_or_404
# Create your views here.
class ComplaintView(View):

    def get(self,request,*args,**kwargs):

        # trucks = Complaint.objects.all()

        user = request.user

        if user.role == "Admin":
            # Admin can see all complaint entries
            complaints = Complaint.objects.filter(active_status = True).order_by('-created_at')
        elif user.role == "User":
            # Access the profile of the user (correctly getting profile here)
            customer = Users.objects.get(profile=request.user)  # This works if the user has a related profile
            # Assuming customer field in Complaint refers to the User model
            complaints = Complaint.objects.filter(customer=customer).order_by('-created_at')
        else:
            # Other roles (if any) get no access
            complaints = Complaint.objects.none()
        return render(request,'complaint/complaint-list.html',{'complaints':complaints})
    

class ComplaintFormView(View):

    def get(self,request,*args,**kwargs):

        form = ComplaintRegisterForm()


        return render(request,'complaint/complaint-register.html',{'form':form})
    def post(self,request,*args,**kwargs):

        form = ComplaintRegisterForm(request.POST,request.FILES)

        customer = Users.objects.get(profile=request.user)

        if form.is_valid():
            
            complaint = form.save(commit=False)
            complaint.customer = customer  # auto assign the logged-in user
            complaint.save()
            return redirect('complaintthanks')

        else:

            form = ComplaintRegisterForm()

            return render(request,'complaint/complaint-register.html',{'form':form})
        
class ComplaintDetailView(View):

    def get(self,request,uuid,*args,**kwargs):
        complaint = get_object_or_404(Complaint, uuid=uuid)
        return render(request, 'complaint/complaint-detail.html', {'complaint': complaint})
    
class ComplaintDeleteView(View):

    def get(self, request, *args, **kwargs):
        # Fetch the complaint by UUID
        uuid = kwargs.get('uuid')
        complaints = get_object_or_404(Complaint, uuid=uuid,active_status = True)
        return render(request, 'complaint/complaint_delete_confirm.html', {'complaints': complaints})

    def post(self, request, *args, **kwargs):
        # Fetch the complaints by UUID
        uuid = kwargs.get('uuid')
        complaints = get_object_or_404(Complaint, uuid=uuid,active_status = True)

        # Delete the complaints
        complaints.active_status = False
        complaints.save()
  # This will now just mark is_deleted = True

        return redirect('complaint')  # Redirect to the driver list view
    
class ComplaintThankyouView(View):

    def get(self,request,*args,**kwargs):


        return render(request,'complaint/thankyou.html')
