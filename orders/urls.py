from django.urls import path
from . import views
urlpatterns = [
    path('create/', views.order_create,name='order_create'),
    path('my_order/', views.my_order, name='my_order'),

]