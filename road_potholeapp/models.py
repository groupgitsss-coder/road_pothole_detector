from django.db import models

# Create your models here.
class Logintable(models.Model):
    username=models.CharField(max_length=200, null=True, blank=True)
    password=models.CharField(max_length=200, null=True, blank=True)
    Usertype=models.CharField(max_length=100, null=True, blank=True)

class Usertable(models.Model):
    name=models.CharField(max_length=200, null=True, blank=True)
    image=models.FileField(max_length=200, null=True, blank=True)
    age=models.IntegerField(null=True, blank=True)
    gender=models.CharField(max_length=200, null=True, blank=True)
    email=models.CharField(max_length=200, null=True, blank=True)
    location=models.CharField(max_length=200, null=True, blank=True)
    phone=models.BigIntegerField(null=True, blank=True)
    login=models.ForeignKey(Logintable, on_delete=models.CASCADE, null=True, blank=True)

class Contractortable(models.Model):
    name=models.CharField(max_length=200, null=True, blank=True)
    place=models.CharField(max_length=200, null=True, blank=True)
    phone=models.BigIntegerField(null=True, blank=True)
    email=models.CharField(max_length=200, null=True, blank=True)
    specialisation=models.CharField(max_length=200, null=True, blank=True)
    experience=models.CharField(max_length=200, null=True, blank=True)
    login=models.ForeignKey(Logintable, on_delete=models.CASCADE, null=True, blank=True)

class Potholetable(models.Model):
    latitude=models.FloatField(max_length=200, null=True, blank=True)
    longitude=models.FloatField(max_length=200, null=True, blank=True)
    date=models.DateField(max_length=200, null=True, blank=True)
    user=models.ForeignKey(Usertable, on_delete=models.CASCADE, null=True, blank=True)

class Feedbacktable(models.Model):
    feedback=models.CharField(max_length=300, null=True, blank=True)
    date=models.DateField(max_length=200, null=True, blank=True)
    user=models.ForeignKey(Usertable, on_delete=models.CASCADE, null=True, blank=True)

class Complaintable(models.Model):
    complaint=models.CharField(max_length=300, null=True, blank=True)
    date=models.DateField(max_length=200, null=True, blank=True) 
    replay=models.CharField(max_length=300, null=True, blank=True) 
    user=models.ForeignKey(Usertable, on_delete=models.CASCADE, null=True, blank=True)

class Workassigntable(models.Model):
    pothole=models.ForeignKey(Potholetable, on_delete=models.CASCADE, null=True, blank=True)
    contractor=models.ForeignKey(Contractortable, on_delete=models.CASCADE, null=True, blank=True)
    description=models.CharField(max_length=300, null=True, blank=True)
    date=models.DateField(max_length=200, null=True, blank=True) 
    status=models.CharField(max_length=300, null=True, blank=True)

class Issuestable(models.Model):
    contractor=models.ForeignKey(Contractortable, on_delete=models.CASCADE, null=True, blank=True)
    date=models.DateField(max_length=200, null=True, blank=True) 
    description=models.CharField(max_length=300, null=True, blank=True)



    
    
    

