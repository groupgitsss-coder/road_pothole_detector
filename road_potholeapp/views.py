from django.http import HttpResponse
from django.shortcuts import render
from django.views import View

from road_potholeapp.models import *

# Create your views here.
class LoginView(View):
    def get(self,request):
        return render(request, 'login.html')
    def post(self,request):
        username=request.POST.get('username')
        password=request.POST.get('password')
        obj=Logintable.objects.get(username=username,password=password)
        if obj.type=='admin':
            return HttpResponse('''<script>alert('login successful');window.location='/adminview'</script>''')
        
    
class UserView(View):
    def get(self,request):
        return render(request, 'USER.HTML')
    
class ContractorView(View):
    def get(self,request):
        return render(request, 'contracter.html')
    
class potholeView(View):
    def get(self,request):
        return render(request, 'POTHOLE.HTML')
    
class FeedbackView(View):
    def get(self,request):
        return render(request, 'FEEDBACK.html')
    
class ComplaintView(View):
    def get(self,request):
        return render(request, 'COMPLAIN.html')
    
class WorkassignView(View):
    def get(self,request):
        return render(request, 'workassign.html')
    
class IssuesView(View):
    def get(self,request):
        return render(request, 'issues.html')
class AdminhomeView(View):
    def get(self,request):
        return render(request, 'home.html')

    
    


    

    
    
    
    