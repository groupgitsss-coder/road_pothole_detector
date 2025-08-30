from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views import View

from road_potholeapp.forms import *
from road_potholeapp.models import *

# Create your views here.
class LoginView(View):
    def get(self,request):
        return render(request, 'login.html')
    def post(self,request):
        username=request.POST.get('username')
        password=request.POST.get('password')
        obj=Logintable.objects.get(username=username,password=password)
        if obj.Usertype=='admin':
            return HttpResponse('''<script>alert('login successful');window.location='/adminview'</script>''')
        elif obj.Usertype=='Contractor':
            return HttpResponse('''<script>alert('login successful');window.location='/contractorhome'</script>''')
        
    
class UserView(View):
    def get(self,request):
        obj = Usertable.objects.all()
        return render(request, 'USER.HTML', {'val': obj})
    
class DeleteUser(View):
    def get(self,request, lid):
        obj = Logintable.objects.get(id=lid)
        obj.delete()
        return redirect('user')
    
class ContractorView(View):
    def get(self,request):
        obj = Contractortable.objects.all()
        return render(request, 'contracter.html',{'val': obj})

class DeleteContractor(View):
    def get(self,request, lid):
        obj = Logintable.objects.get(id=lid)
        obj.delete()
        return redirect('contractor')
    
class EditContractor(View):
    def get(self,request, id):
        obj = Contractortable.objects.get(id=id)
        return render(request, "editcontractor.html", {'val': obj})
    def post(self, request, id):
        obj = Contractortable.objects.get(id=id)
        form = Contractorform(request.POST, instance=obj)
        if form.is_valid():
            form.save()
            return redirect('contractor')
    
class potholeView(View):
    def get(self,request):
        obj = Potholetable.objects.all()
        return render(request, 'POTHOLE.HTML',{'val': obj})
    
class FeedbackView(View):
    def get(self,request):
        obj = Feedbacktable.objects.all()
        return render(request, 'FEEDBACK.html',{'val': obj})
    
class ComplaintView(View):
    def get(self,request):
        obj = Complaintable.objects.all()
        print(obj)
        return render(request, 'COMPLAIN.html',{'val': obj})
    
class WorkassignView(View):
    def get(self,request):
        return render(request, 'workassign.html')
    
class IssuesView(View):
    def get(self,request):
        return render(request, 'issues.html')

class AdminhomeView(View):
    def get(self,request):
        return render(request, 'home.html')
    
class AddContactorView(View):
    def get(self,request):
        return render(request, 'add_contractor.html')
    def post(self, request):
        form = Contractorform(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            login_obj = Logintable.objects.create(username=request.POST['Username'], password=request.POST['Password'], Usertype="Contractor")
            user.login=login_obj
            user.save()
            return redirect('contractor')
            

class ReplyView(View):
    def get(self,request, id):
        c=Complaintable.objects.get(id=id)
        return render(request, 'reply.html', {'c':c})
        
    def post(self, request, id):
        c=Complaintable.objects.get(id=id)
        r=ComplaintForm(request.POST, instance=c)
        if r.is_valid():
            r.save()
            return redirect('complaint')
        
class ContractorhomeView(View):
    def get(self,request):
        return render(request,'contractorhome.html')
    
class AssignedworksView(View):
    def get(self,request):
        return redirect('assignedworkhome')
    
class UpdateworkView(View):
    def get(self,request):
        return redirect('updatework')
    
class SendcomplainView(View):
    def get(self,request):
        return redirect('sendcomplain')
    
class AssignedworkView(View):
    def get(self,request):
        return redirect('assignedwork')

class ContractorcomplaintView(View):
    def get(self,request):
        return redirect('contractorcomplaint.html')

    
    

    

    
    
    
    