from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings 


app_name = 'dcatz'

urlpatterns = [
    path('', views.home_page, name='home-page'),
    path('home-page/', views.home_page, name='home-page'),
    path('sign-in/', views.sign_in, name='sign_in'),
    path('sign-up/', views.sign_up, name='sign_up'),  
    path('cat-tree/', views.cat_tree, name='cat_tree'),  
    path('cart/', views.cart, name='cart'),  
    path('about/', views.about, name='about'),  
    path('logout/', views.logout_view, name='logout'),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
