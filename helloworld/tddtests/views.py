import json

from django.core import serializers
from django.http import HttpResponse, Http404, HttpResponse, HttpResponseRedirect, JsonResponse
from django.shortcuts import get_object_or_404, render
from django.template import loader
from django.views.decorators.csrf import csrf_exempt
from django.views import generic
from django.urls import reverse

from .models import Sentiments


class IndexView(generic.TemplateView):
    template_name = 'words/index.html'

class CreateWords(generic.View):
    pass