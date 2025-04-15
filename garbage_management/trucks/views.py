from django.shortcuts import render,redirect

from django.views import View

from .forms import TruckRegisterForm

from .models import GarbageTruck

from django.shortcuts import get_object_or_404




# Create your views here.
class TruckView(View):

    def get(self,request,*args,**kwargs):

        # trucks = GarbageTruck.objects.all()

        trucks = GarbageTruck.objects.filter(is_deleted=False)


        return render(request,'trucks/truck_list.html',{'trucks':trucks})
    

class TruckFormView(View):

    def get(self,request,*args,**kwargs):

        form = TruckRegisterForm()


        return render(request,'trucks/truck_register.html',{'form':form})
    def post(self,request,*args,**kwargs):

        form = TruckRegisterForm(request.POST,request.FILES)

        if form.is_valid():
            form.save()

            return redirect('trucks')


        else:

            form = TruckRegisterForm()

            return render(request,'trucks/truck_register.html',{'form':form})
    

class TruckUpdateView(View):

    def get(self, request, *args, **kwargs):

        uuid = kwargs.get('uuid')

        trucks = get_object_or_404(GarbageTruck, uuid=uuid)

        form = TruckRegisterForm(instance=trucks)

        return render(request, 'trucks/truck_update.html', {'form': form})

    def post(self, request, *args, **kwargs):

        uuid = kwargs.get('uuid')

        trucks = get_object_or_404(GarbageTruck, uuid=uuid)

        form = TruckRegisterForm(request.POST, request.FILES, instance=trucks)

        if form.is_valid():

            form.save()

            return redirect('trucks')
        
        return render(request, 'trucks/truck_register.html', {'form': form})
    

class TruckDeleteView(View):

    def get(self, request, *args, **kwargs):
        # Fetch the truck by UUID
        uuid = kwargs.get('uuid')
        truck = get_object_or_404(GarbageTruck, uuid=uuid,is_deleted=False)
        return render(request, 'trucks/truck_delete_confirm.html', {'truck': truck})

    def post(self, request, *args, **kwargs):
        # Fetch the truck by UUID
        uuid = kwargs.get('uuid')
        truck = get_object_or_404(GarbageTruck, uuid=uuid,is_deleted=False)

        # Delete the truck
        truck.delete()  # This will now just mark is_deleted = True

        return redirect('trucks')  # Redirect to the truck list view
