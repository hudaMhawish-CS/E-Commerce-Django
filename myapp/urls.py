from django.urls import path
from . import views

urlpatterns = [
    path('', views.product_list,name='product_list'),
    path('<slug:slug>/', views.product_detail,name='product_detail'),
    path('category/<slug:slug>/', views.category_detail, name='category_detail'),

    # path('cart/', views.cart, name='cart'),
    # path('checkout/', views.checkout, name='checkout'),
    # path('order_success/', views.order_success, name='order_success'),
    # path('track_order/', views.track_order, name='track_order'),

]