from django.contrib import admin
from django.urls import path, include
from website.views import *
from django.views.generic.base import TemplateView

urlpatterns = [
    path('actor/<int:actor_id>/', actor_detail, name='actor_detail'),
    path('director/<int:director_id>/', director_detail, name='director_detail'),
    path('movie/<int:movie_id>/', movie_detail, name='movie_detail'),
    path("signup/", signup, name="signup"),  
    path('', home, name='home'),
]