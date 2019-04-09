from django.shortcuts import render,redirect
from django.urls import reverse
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required

# Create your views here.
User = get_user_model()

@login_required
def check(request):
    user = User.objects.get(email=request.user.email)
    print(request.user)
    if user.is_admin:
        return redirect(reverse('council:admin_page'))
    else :
        return redirect(reverse('council:home'))