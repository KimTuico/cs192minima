from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse

from .models import Choice, Question

# Create your views here.
def index(request):
    return render(request, 'polls/index.html', {
        'latest_question_list': Question.objects.order_by('-pub_date')[:5]
    })

def detail(request, question_id):
    return render(request, 'polls/detail.html', {
        'question': get_object_or_404(Question, pk=question_id)
    })

def results(request, question_id):
    return render(request, 'polls/results.html', {
        'question': get_object_or_404(Question, pk=question_id)
    })

def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    # retrieve selected choice value; otherwise raise exception
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except(KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form
        return render(request, 'polls/details.html', {
            'question': question,
            'error_message': "You did not select a choice."
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # redirect after form submission to avoid POST-ing twice (when user goes to previous page)
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))