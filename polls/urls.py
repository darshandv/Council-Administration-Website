from django.urls import path

from . import views

app_name = 'polls'

urlpatterns = [
    path('', views.index, name='index'), 
 	
    # ex: /polls/5/results/
    # ex: /polls/5/vote/
    path('<int:ClassElections_id>/vote', views.vote, name='vote'),
   
    path('results', views.results, name='results'),

	path('latest', views.index),
	
    path('<int:student_year>/<str:student_branch>/<int:student_section>', views.detail, name='detail'),
#unique_together
]

