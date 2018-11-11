from django.contrib import admin

# Register your models here.

from .models import ClassElections,Candidate,Checker
@admin.register(ClassElections)
class ClassElectionsAdmin(admin.ModelAdmin):
    list_display = ('pk','student_year','student_branch','student_section')




@admin.register(Candidate)
class CandidateAdmin(admin.ModelAdmin):
    list_display = ('pk','ClassElection','Name')
    exclude = ('votes',)    


@admin.register(Checker)
class CheckerAdmin(admin.ModelAdmin):
    list_display = ('pk','user','has_voted_class')
    exclude = ('user',)    
