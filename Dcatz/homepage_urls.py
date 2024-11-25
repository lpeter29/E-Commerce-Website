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
    path('discounts/', views.discounts, name='discounts'),
    path('cat-tree/', views.cat_tree, name='cat_tree'),
    path('add-to-cart/', views.add_to_cart, name='add_to_cart'),
    path('remove-from-cart/<int:item_id>/', views.remove_from_cart, name='remove_from_cart'),
    path('update-cart-quantity/<int:item_id>/', views.update_cart_quantity, name='update_cart_quantity'),
]
