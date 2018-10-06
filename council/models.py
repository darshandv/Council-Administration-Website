from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
from django.db.models import CharField


class Users(AbstractUser):
    is_admin = models.BooleanField(default=False)
    is_member= models.BooleanField(default=False)
    first_name = models.CharField(max_length=40)
    last_name = models.CharField(max_length=40)  # type: CharField
    roll = models.CharField(max_length=8,unique=True)
    year = models.IntegerField()
    branch = models.CharField(max_length=2,default="NA")
    section = models.IntegerField()
    
    def __str__(self):
        return self.first_name+" "+self.last_name


