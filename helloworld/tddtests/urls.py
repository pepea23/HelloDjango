from django.urls import path

from . import views


urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('/createwords', views.CreateWords.as_view(), name='createwords'),
]