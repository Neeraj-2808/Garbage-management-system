from django.shortcuts import render,redirect

from django.views import View

# Create your views here.
class DashboardView(View):
    
    def get(self,request,*args,**kwargs):
        
        
        return render(request,'garbage/home.html')
    
from django.views import View
from django.shortcuts import render

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

