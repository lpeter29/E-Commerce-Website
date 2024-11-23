from django.urls import path
from . import views

app_name = 'homepage'

urlpatterns = [
    path('accessories/', views.accessories, name='accessories'),
    path('clothing/', views.clothing, name='clothing'),
    path('furniture/', views.furniture, name='furniture'),
    path('food/', views.food, name='food'),
    path('toys/', views.toys, name='toys'),
    path('promo/', views.promo, name='promo'),
    path('free-shipping/', views.free_shipping, name='free-shipping'),
    path('10-off/', views.discounts, name='discounts'),
]
