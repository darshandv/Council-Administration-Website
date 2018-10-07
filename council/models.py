from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
from django.db.models import CharField


class Users(AbstractUser):
    is_admin = models.BooleanField(default=False)
    is_member= models.BooleanField(default=False)
    username = models.CharField(max_length=40,unique=True,null=False)
    first_name = models.CharField(max_length=40)
    last_name = models.CharField(max_length=40)  # type: CharField
    roll = models.CharField(max_length=8,unique=True)
    year = models.IntegerField(null=True)
    branch = models.CharField(max_length=2)
    section = models.IntegerField(null=True)
    
    def __str__(self):
        return self.first_name+" "+self.last_name


