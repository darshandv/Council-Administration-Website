xfrom django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django.utils import timezone
from django.template import loader

from django.urls import reverse


from .models import ClassElections,Candidate,Checker
from django.shortcuts import get_object_or_404, render

from django.http import Http404

# Create your views here.
from django.contrib.auth.decorators import login_required

@login_required
def index(request):
    latest_question_list = ClassElections.objects.all()
    context = {}
    voted = False

    if request.user.is_authenticated and not request.user.is_superuser:
        try:
            check=Checker.objects.get(user = request.user)
            print(check)
            voted= True
        except Exception as e:
            print(e)
            voted = False  
            print(voted)
                  
