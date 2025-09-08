from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views import View
from django.shortcuts import get_object_or_404
from road_potholeapp.serializer import Loginserializer, Userserializer
from road_potholeapp.forms import *
from road_potholeapp.models import *
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST, HTTP_500_INTERNAL_SERVER_ERROR, HTTP_401_UNAUTHORIZED


# Create your views here.

class LoginView(View):
    def get(self,request):
        return render(request, 'login.html')
    def post(self,request):
        username=request.POST.get('username')
        password=request.POST.get('password')
        obj=Logintable.objects.get(username=username,password=password)
        request.session['user_id'] = obj.id
        print(request.session['user_id'])
        if obj.Usertype=='admin':
            return HttpResponse('''<script>alert('login successful');window.location='/adminview'</script>''')
        elif obj.Usertype=='contractor':
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
    def get(self, request):
        potholes = Potholetable.objects.all()
        print(potholes,'8888888888888')
        contractors = Contractortable.objects.all()
        print(contractors,'************')
        return render(request, 'workassign.html', {
            'potholes': potholes,
            'contractors': contractors
        })

    def post(self, request,):
        form = workassignform(request.POST)
        if form.is_valid():
            f=form.save(commit=False)
            f.status = "PENDING"
            f.save()
           
        return redirect('workassign')
class contractorviewwork(View):
    def get(self, request):
        obj = Workassigntable.objects.filter(contractor__login_id=request.session['user_id'])
        return render(request, 'workassigned.html',{"val":obj})
    
 
class UpdateStatus(View):
    def get(self, request, id):
        obj = Workassigntable.objects.get(id=id)
        obj.status = "completed"
        obj.save()
        return redirect('contractorviewwork')


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
    


    # /////////////////////////////////////////////////////////// API /////////////////////////////////////////////////////////



class studentreg(APIView):
    def post(self, request):
        print('==============================',request.data)
        reg_serial=Userserializer(data=request.data)
        login_serial=Loginserializer(data=request.data)

        regvalid=reg_serial.is_vaqlid()
        loginvalid=login_serial.is_valid()

        if regvalid and loginvalid:
            login = login_serial.save(user_type='student')
            reg_serial.save(LOGINID=login)
            return Response({'message':'Registration successful'}, status=HTTP_200_OK)
        else:
            return Response({'Registration error': reg_serial.errors if not regvalid else None,
                             'Login error': login_serial if not loginvalid else None}, status=HTTP_400_BAD_REQUEST)
        


class LoginApiView(APIView):
    def post(self, request):
        Response_dict={}
        username=request.data.get('username')
        password=request.data.get('password')
        usertype=request.data.get('Usertype')
        try:
            if not username or not password:
                return Response({'Response': 'Login failed'}, status=HTTP_400_BAD_REQUEST)
            uname=Logintable.objects.filter(username=username, password=password).first()
            if not uname:
                return Response({'Response':'Login failed!'}, status=HTTP_400_BAD_REQUEST)
            else:
                Response_dict['message'] = 'Login successful'
                Response_dict['user_type'] = uname.user_type
                Response_dict['userid'] = uname.id
                return Response(Response_dict, status=HTTP_200_OK)
        except Exception as e:
            return Response({'Response':'internal server error'}, status=HTTP_500_INTERNAL_SERVER_ERROR)









    
    
    

    

    
    
    
    