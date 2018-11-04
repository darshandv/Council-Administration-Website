from django.shortcuts import render, redirect
from django.views import generic
from django.urls import reverse_lazy,reverse
from django.contrib.auth import authenticate,login

# Create your views here.
# def index(request):
#     return render(request,'council/admin.html')
#
# def signup(request):
#     if request.method == 'POST':
#         form = UserForm(request.POST)
#         if form.is_valid():
#             form.save()
#             username = form.cleaned_data.get('username')
#             raw_password = form.cleaned_data.get('password1')
#             user = authenticate(username=username, password=raw_password)
#             login(request, user)
#             return redirect('council:index')
#     else:
#         form = UserForm()
#     return render(request, 'council/signup.html', {'form': form})



# class UserFormView(generic.CreateView):
#     form_class = UserForm
#     template_name = 'council/signup.html'
#     success_url = reverse_lazy('admin.html')

from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import get_user_model

User = get_user_model()

class HomeView(TemplateView):
    template_name = "council/index.html"

def check(request):
    user = User.objects.get(email=request.user.email)
    print(request.user)
    if user.is_admin:
        return render(request,'council/admin.html')
    else :
        return redirect(reverse('council:home'))
