from django.urls import path
from .views import *

urlpatterns = [
    path("bikes/", bikeview, name="bike-list"),
    path('bikes/<int:pk>/', BikeView.as_view(), name='bike-detail'),
    path('orders/', OrderListView.as_view(), name='order-list'),
    path('order/<int:pk>', OrderDetailView.as_view(), name='order-detail')
]
