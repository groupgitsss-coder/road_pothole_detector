"""
URL configuration for road_pothole project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from road_potholeapp.views import *

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('adminview',AdminhomeView.as_view(),name='adminview'),
    path('',LoginView.as_view(),name='login'),
    path('user',UserView.as_view(),name='user'),
    path('DeleteUser/<int:lid>',DeleteUser.as_view(),name='DeleteUser'),
    path('contractor',ContractorView.as_view(),name='contractor'),
    path('addcontactor',AddContactorView.as_view(),name='addcontactor'),
    path('DeleteContractor/<int:lid>',DeleteContractor.as_view(),name='DeleteContractor'),
    path('pothole',potholeView.as_view(),name='pothole'),
    path('Feedback',FeedbackView.as_view(),name='Feedback'),
    path('complaint',ComplaintView.as_view(),name='complaint'),
    path('workassign',WorkassignView.as_view(),name='Workassign'),
    path('issues',IssuesView.as_view(),name='issues'),
    path('reply/<int:id>',ReplyView.as_view(),name='reply'),
    



    

    




]
