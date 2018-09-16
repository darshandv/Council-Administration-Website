from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class Users(AbstractUser):
    is_admin = models.BooleanField(default=False)
    is_member= models.BooleanField(default=False)
    first_name = models.CharField(max_length=40)
    last_name = models.CharField(max_length=40)
    user_id = models.CharField(primary_key=True,max_length=30)




