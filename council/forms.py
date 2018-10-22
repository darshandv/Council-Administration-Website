from django.contrib.auth.forms import UserCreationForm
from .models import Users

class UserForm(UserCreationForm):

    class Meta(UserCreationForm.Meta) :
        model = Users
        fields = ['first_name', 'last_name', 'roll', 'username', 'is_member',
                  'year', 'branch', 'section']