from django.urls import path
from . import views

urlpatterns = [
    path('', views.master, name = 'master'),
    path('home-page', views.home_page, name='home-page'),
    path('sign-in', views.sign_in, name='sign_in'),
    path('sign-up', views.sign_up, name='sign_up'),  
    path('cat-tree', views.cat_tree, name='cat_tree'),  
]
