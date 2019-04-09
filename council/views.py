from django.shortcuts import render, redirect
from django.views.generic import CreateView,TemplateView
from django.urls import reverse, reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin,PermissionRequiredMixin
from .forms import *
from .models import *
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required,permission_required
from django.contrib.auth.models import Permission

import json

User = get_user_model()

class HomeView(TemplateView):
    template_name = "council/index.html"

    # def get_context_data(self, **kwargs):
    #     context = super(HomeView, self).get_context_data(**kwargs)
    #     context['user'] = User.objects.all()
    #     return context

class ClubCreateView(LoginRequiredMixin,PermissionRequiredMixin,CreateView):
    permission_required = 'council.add_club'
    form_class = ClubCreateForm
    template_name = 'council/club_create.html'
    model = Club
    success_url = reverse_lazy('council:check')

class TransactionCreateView(LoginRequiredMixin,PermissionRequiredMixin,CreateView):
    permission_required = 'council.add_transaction'
    form_class = TransactionCreateForm
    template_name = 'council/transaction_create.html'
    model = Transaction
    success_url = reverse_lazy('council:check')

class MeetCreateView(LoginRequiredMixin,PermissionRequiredMixin, CreateView):
    permission_required = 'council.add_meet'
    form_class = MeetCreateForm
    template_name = 'council/meet_create.html'
    model = Meet
    success_url = reverse_lazy('council:check')


@login_required
def admin_page(request):
    transactions = Transaction.objects.all().order_by('-time')
    clubs = Club.objects.all()
    meets = Meet.objects.all().order_by('-time')
    total_clubs = len(clubs)
    total_transactions = len(transactions)
    total_meets = len(meets)
    context = {
        'clubs' : clubs,
        'transactions' : transactions,
        'meets'        : meets,
        'total_clubs' : total_clubs,
        'total_transactions': total_transactions,
        'total_meets' : total_meets
    }
    return render(request, 'council/admin2.html', context)


def get_data(request):
    transactions = Transaction.objects.all()
    return json.dump({'transactions' : transactions})