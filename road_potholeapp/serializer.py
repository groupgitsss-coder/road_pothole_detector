from rest_framework import serializers
from road_potholeapp.models import *


class Loginserializer(serializers.ModelSerializer):
    class Meta:
        model = Logintable
        fields = ['username','password','Usertype']

class Userserializer(serializers.ModelSerializer):
    class Meta:     
        model=Usertable
        fields=['name','image','age','gender','email','location','phone','login']
    
class Contractorserializer(serializers.ModelSerializer):
    class Meta:
        model=Contractortable
        fields=['name','place','phone','email','specialisation','experience']

class Potholeserializer(serializers.ModelSerializer):
    class Meta:
        model=Potholetable
        fields=['latitude','longitude','date','user']

class Feedbackserializer(serializers.ModelSerializer):
    class Meta:
        model=Feedbacktable
        fields=['feedback','date','user']

class Workassignserializer(serializers.ModelSerializer):
    class Meta:
        model=Workassigntable
        fields=['pothole','contractor','description','date','status']

class Issuesserializer(serializers.ModelSerializer):
    class Meta:
        model=Issuestable
        fields=['contractor','date','description']


