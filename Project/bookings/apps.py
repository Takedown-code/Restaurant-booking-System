from django.apps import AppConfig

class BookingsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'project.bookings'  # ✅ updated from restaurant_booking.bookings
