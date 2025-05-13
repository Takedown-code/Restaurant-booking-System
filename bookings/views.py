from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Booking

class BookingListView(ListView):
    model = Booking
    template_name = 'bookings/booking_list.html'

class BookingCreateView(CreateView):
    model = Booking
    fields = ['user_name', 'table', 'start_time']
    template_name = 'bookings/booking_form.html'
    success_url = reverse_lazy('booking_list')

class BookingUpdateView(UpdateView):
    model = Booking
    fields = ['user_name', 'table', 'start_time']
    template_name = 'bookings/booking_form.html'
    success_url = reverse_lazy('booking_list')

class BookingDeleteView(DeleteView):
    model = Booking
    template_name = 'bookings/booking_confirm_delete.html'
    success_url = reverse_lazy('booking_list')
