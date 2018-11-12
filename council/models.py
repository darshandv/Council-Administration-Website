from django.db import models
from django.utils import timezone
from django.contrib.auth import get_user_model
from django.urls import reverse
# Create your models here.
User = get_user_model()

class Club(models.Model):
    name = models.CharField(max_length=256)
    convenor = models.CharField(max_length=256)
    no_of_members = models.IntegerField()

    def __str__(self):
        return self.name


class Transaction(models.Model):
    reason = models.CharField(max_length=256)
    from_club = models.ForeignKey(Club,on_delete=models.CASCADE,related_name='from_club')
    to_club = models.ForeignKey(Club, on_delete=models.CASCADE,related_name='to_club')
    amount = models.FloatField()
    time = models.DateTimeField(editable=False)

    def save(self, *args,**kwargs):
        if not self.id:
            self.time = timezone.now()

        return super(Transaction,self).save(*args,**kwargs)

class Meet(models.Model):
    name = models.CharField(max_length=256)
    summary = models.TextField()
    detail  = models.TextField()
    time    = models.DateTimeField()

    def save(self, *args,**kwargs):
        if not self.id:
            self.time = timezone.now()

        return super(Meet,self).save(*args,**kwargs)