import json

from django.core import serializers
from django.http import HttpResponse , Http404, HttpResponse, HttpResponseRedirect, JsonResponse
from django.shortcuts import get_object_or_404, render
from django.template import loader
from django.views.decorators.csrf import csrf_exempt
from django.views import generic
from django.urls import reverse

from .models import Choice, Question


class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'
    
    def get_queryset(self):
        return Question.objects.order_by('-pub_date')[:5]

class DetailView(generic.DetailView):
    model = Question
    template_name = 'polls/detail.html'

class HomeView(generic.TemplateView):
    template_name = 'polls/home.html'

class ResultsView(generic.DetailView):
    model = Question
    template_name = 'polls/results.html'


class Vote(generic.TemplateView):   
    def post(self, request, question_id):
        question = get_object_or_404(Question, pk=question_id)
        
        try:
            selected_choice = question.choice_set.get(pk=request.POST['choice'])
        except (KeyError, Choice.DoesNotExist):
            return render(
                request,
                'polls/detail.html', {
                    'question': question,
                    'error_message': "You didn't select a choice.",
                }
            )
        else:
            selected_choice.votes += 1
            selected_choice.save()
            return HttpResponseRedirect(
                reverse('results', args=(question.id,))
            )
