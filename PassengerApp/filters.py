import django_filters
from .models import *

class BookingFilter(django_filters.FilterSet):
    class Meta:
        model = Bookings
        fields = ['TravelDate', 'BusPlateNo','PickupTerminal', 'DropoffTerminal']

class PassengerFilter(django_filters.FilterSet):
    class Meta:
        model = Passenger
        fields = ['FName', 'MName','LName', 'SwabTestResult']