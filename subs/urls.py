from django.urls import path
from . import views

urlpatterns = [
    path('analyse', views.analyse, name='analyse'),
    path('score', views.score, name='score'),
]