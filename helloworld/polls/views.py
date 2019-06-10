import json

from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse , Http404, HttpResponse, HttpResponseRedirect, JsonResponse
from django.template import loader
from django.views import generic
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.core import serializers

from .models import Choice, Question


class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        """Return the last five published questions."""
        return Question.objects.order_by('-pub_date')[:5]
class DetailView(generic.DetailView):
    model = Question
    template_name = 'polls/detail.html'


class ResultsView(generic.DetailView):
    model = Question
    template_name = 'polls/results.html'

class apiPost(generic.TemplateView):
	template_name = 'polls/apipost.html'

# def index(request):    
# 	latest_question_list = Question.objects.order_by('-pub_date')[:5]
# 	template = loader.get_template('polls/index.html')
# 	context = {'latest_question_list': latest_question_list, }
# 	return HttpResponse(template.render(context, request))


# def detail(request, question_id):
#     # try:
#     #     question = get_object_or_404(pk=question_id)
#     # except Question.DoesNotExist:
#     #     raise Http404("Question does not exist")
#     # return render(request, 'polls/detail.html', {'question': question})
# 	question = get_object_or_404(Question, pk=question_id)
# 	return render(request, 'polls/detail.html', {'question': question})

# def results(request, question_id):
    # question = get_object_or_404(Question, pk=question_id)
    # return render(request, 'polls/results.html', {'question': question})  

def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))
# Create your views here.
def getChoiseByApi(request, question_id):
	# question = get_object_or_404(Question, pk=question_id)
	# selected_choice = get_object_or_404(Choice, fk= question_id)
	selected_choice = Choice.objects.filter(question=question_id).only("choice_text")
	selected_choice = serializers.serialize('json', selected_choice)

	return JsonResponse({'Question {question_id}':selected_choice})

@csrf_exempt 
def voteChoiseByApi(request):
		body_unicode = request.body.decode('utf-8')
		body = json.loads(body_unicode)
		body = body['test']
		return HttpResponse(body)
