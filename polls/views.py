from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django.utils import timezone
from django.template import loader

from django.urls import reverse


from .models import ClassElections,Candidate,Checker
from django.shortcuts import get_object_or_404, render

from django.http import Http404

# Create your views here.
from django.contrib.auth.decorators import login_required

@login_required
def index(request):
    latest_question_list = ClassElections.objects.all()
    context = {}
    
    if request.user.is_authenticated and not request.user.is_superuser:
        try:
            check=Checker.objects.get(user = request.user)
            print(check)
            voted= True
        except Exception as e:
            print(e)
            voted = False  
            print(voted)
                  
    # template = loader.get_template('polls/index.html') 
    context = {	
		'latest_question_list' : latest_question_list,
	    'voted':voted,
     }
   # output = ', '.join([q.question_text for q in latest_question_list])
   # return HttpResponse(output)
    #return HttpResponse(template.render(context,request))
    return render(request, 'polls/index.html', context)

def detail(request, student_year,student_branch, student_section):
	'''try:
		question = Question_objects.get(pk=question_id)
	except Question.DoesNotExist:
		raise Http404("Question does not exits") '''
	ClassElection = get_object_or_404(ClassElections, student_year=student_year, student_section=student_section)
	return render(request, 'polls/details.html',{'ClassElection': ClassElection})


def results(request):
    #response = "You're looking at the results of question %s."
    #return HttpResponse(response % question_id)
    print("reached results")
    if request.method == "POST":
        # print(request.POST)
        data = request.POST
        print(data['sel1'])
        print(data['sel2'])
        print(data['sel3'])
        student_year=data['sel1']
        student_branch=data['sel2']
        student_section=data['sel3']
        ClassElection = get_object_or_404(ClassElections, student_year=student_year , student_branch=student_branch , student_section=student_section )
    else:
        ClassElection = {}
    # ClassElection = get_object_or_404(ClassElections, student_year=student_year, students_section=students_section)
    return render(request, 'polls/results.html', {'question': ClassElection})


#def vote(request, question_id):ClassElections_id
   # return HttpResponse("You're voting on question %s." % question_id)
def vote(request, ClassElections_id):
    ClassElection = get_object_or_404(ClassElections, pk=ClassElections_id)
    try:
        selected_choice = ClassElection.candidate_set.get(pk=request.POST['candidate'])
    except (KeyError, Candidate.DoesNotExist):
        # Redisplay the question voting form.
        print("failure")

        return render(request, 'polls:index', {
            'ClassElection': ClassElection,
            'error_message': "You didn't select a choice.",
        })
    else:
        print("sucess")
        selected_choice.votes += 1
        selected_choice.save()
        checker = Checker()
        checker.user = request.user
        checker.has_voted_class = True
        checker.save()
        print(checker.has_voted_class)
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('polls:index',))

# def show_results(request,):


