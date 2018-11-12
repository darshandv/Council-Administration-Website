from django.db import models

	
import datetime

from registration.models import User
# Create your models here.

class ClassElections(models.Model):
    # id = db.MultiFieldPK("question_year","question_branch","question_section")

    student_year = models.IntegerField(u'Participating Year',null=True)
    student_branch = models.CharField(u'Branch',max_length=2,null=True)
    student_section = models.IntegerField(u'Section',null=True)
    def __str__(self):
        return str(self.pk)

    def details(self):
        return self.question_year

    class Meta:
        unique_together = (("student_year","student_branch","student_section"),)
        verbose_name = 'Class Elections'
        verbose_name_plural = 'Class Elections'
class Candidate(models.Model):
    ClassElection = models.ForeignKey(ClassElections, on_delete=models.CASCADE)
    Name = models.CharField(u'Candidate Name',max_length=20)
    Tag = models.CharField(u'Description',max_length=200,default='Vote Independently')
    image = models.ImageField(upload_to='profile_image',blank=True)
    posters = models.ImageField(upload_to='posters',blank=True)

    votes = models.IntegerField(u'Votes Gained',default=0)
   
    def __str__(self):
        return self.Name

        
    class Meta:
        unique_together = (("Name","votes"),)       
        verbose_name = 'Candidates List'
        verbose_name_plural = 'Candidates List'
    
class Checker(models.Model):
    user= models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )
    has_voted_class = models.BooleanField(default=False)
    # has_voted_council = models.BooleanField(default=False)
    def __str__(self):
        return "Voted"

        
    class Meta:
        verbose_name = 'Check participation'
        verbose_name_plural = 'Check participation'

 