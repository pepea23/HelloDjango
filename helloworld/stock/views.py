from django.core import serializers
from django.http import HttpResponse , Http404, HttpResponse, HttpResponseRedirect, JsonResponse
from django.shortcuts import get_object_or_404, render
from django.template import loader
from django.views.decorators.csrf import csrf_exempt
from django.views import generic
from django.urls import reverse

from .models import Glass

class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'GlassList'
    
    def get_queryset(self):
        print(Glass.objects.all())
        return Glass.objects.all()