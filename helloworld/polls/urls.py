from django.urls import path
from . import views


app_name = 'polls'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('api/', views.apiPost.as_view(), name='postTest'),
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    path('<int:pk>/results/', views.ResultsView.as_view(), name='results'),
    path('<int:question_id>/vote/', views.vote, name='vote'),
    path('api/<int:question_id>/choise/', views.getChoiseByApi, name='api1'),
    path('api/voteapi/', views.voteChoiseByApi, name='api2'),

]