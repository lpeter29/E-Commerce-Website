from django.contrib import admin
from django.urls import path, include
from Dcatz import views

urlpatterns = [
    path('', views.home_page, name='home-page'),
    path('home-page/', views.home_page, name='home-page'),
    path('sign-in/', views.sign_in, name='sign_in'),
    path('sign-up/', views.sign_up, name='sign_up'),
    path('cat-tree/', views.cat_tree, name='cat_tree'),
    path('cart/', views.cart, name='cart'),
    path('checkout/', views.checkout, name='checkout'),
    path('about/', views.about, name='about'),
    path('logout/', views.logout_view, name='logout'),
    path('homepage/', include('Dcatz.homepage_urls')),
    path('admin/', admin.site.urls),
]
