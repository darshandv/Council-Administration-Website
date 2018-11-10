"""council_website URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.conf.urls import url
from django.urls import path,include
from . import views

app_name = 'council'

urlpatterns = [
        url(r'^$', views.HomeView.as_view(), name='home'),
        url(r'^checkpoint/',views.check,name='check'),
        url(r'admin_page/',views.admin_page, name='admin_page'),
        url(r'clubCreate/',views.ClubCreateView.as_view(),name='club_create'),
        url(r'transactionCreate/',views.TransactionCreateView.as_view(),name='transaction_create'),
        url(r'meetCreate/',views.MeetCreateView.as_view(),name='meet_create'),
        url(r'getData/',views.get_data, name='get_data'),
]
