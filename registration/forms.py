# from django.contrib.auth.forms import UserCreationForm
# from .models import Users
#
# class UserForm(UserCreationForm):
#
#     class Meta(UserCreationForm.Meta) :
#         model = Users
#         fields = ['first_name', 'last_name', 'roll', 'username', 'is_member',
#                   'year', 'branch', 'section']

from django.contrib.auth import get_user_model
from .models import User
from django import forms

class SignupForm(forms.ModelForm):
    # first_name = forms.CharField(max_length=30, label='First Name', required = True)
    # last_name = forms.CharField(max_length=30, label='Last Name', required=True)

    class Meta:
        model = get_user_model()
        fields = ['first_name', 'last_name', 'roll', 'year', 'branch', 'section']

    def signup(self, request, user):
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.roll = self.cleaned_data['roll']
        user.year = self.cleaned_data['year']
        user.section = self.cleaned_data['section']
        user.branch = self.cleaned_data['branch']
        user.save()
