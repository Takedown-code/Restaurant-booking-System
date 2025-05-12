from django.urls import path
from .views import *

urlpatterns = [
    path('', BookingListView.as_view(), name='booking_list'),
    path('create/', BookingCreateView.as_view(), name='booking_create'),
    path('update/<int:pk>/', BookingUpdateView.as_view(), name='booking_update'),
    path('delete/<int:pk>/', BookingDeleteView.as_view(), name='booking_delete'),
]
