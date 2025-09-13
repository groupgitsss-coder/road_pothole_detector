from road_potholeapp.models import *
from django.forms import ModelForm  


class ComplaintForm(ModelForm):
    class Meta:
        model=Complaintable
        fields=['complaint', 'date', 'replay','user']

class Usertable(ModelForm):
    class Meta:
        model=Usertable
        fields=['name','image','age','gender','email','latitude','longitude','phone','login']
    
class Contractorform(ModelForm):
    class Meta:
        model=Contractortable
        fields=['name','place','phone','email','specialisation','experience']

class Potholetable(ModelForm):
    class Meta:
        model=Potholetable
        fields=['latitude','longitude','date','user']

class Feedbacktable(ModelForm):
    class Meta:
        model=Feedbacktable
        fields=['feedback','date','user']

class workassignform(ModelForm):
    class Meta:
        model=Workassigntable
        fields=['pothole','contractor','description','date']

class Issuestable(ModelForm):
    class Meta:
        model=Issuestable
        fields=['contractor','date','description']


