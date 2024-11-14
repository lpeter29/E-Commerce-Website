from django.urls import path
from . import views

urlpatterns = [
    path('', views.master, name = 'master'),
    path('home-page', views.home_page, name='home-page')
    
]
