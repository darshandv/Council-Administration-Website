from django.shortcuts import render,redirect
from django.urls import reverse
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required, permission_required

# Create your views here.
User = get_user_model()

@login_required
@permission_required('sites.add_site',login_url='council:home')
def check(request):
    user = User.objects.get(email=request.user.email)
    print(request.user)
    return redirect(reverse('council:admin_page'))