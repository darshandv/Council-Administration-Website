from django.shortcuts import render, redirect
from .forms import UserForm
from django.views import generic
from django.urls import reverse_lazy
from django.contrib.auth import authenticate,login

# Create your views here.
def index(request):
    return render(request,'council/index.html')

def signup(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('council:index')
    else:
        form = UserForm()
    return render(request, 'council/signup.html', {'form': form})



class UserFormView(generic.CreateView):
    form_class = UserForm
    template_name = 'council/signup.html'
    success_url = reverse_lazy('admin.html')




