from django.forms import ModelForm
from .models import Bookings, Passenger
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms


class CreateUserForm(UserCreationForm):
	class Meta:
		model = User
		fields = ['username', 'email', 'password1', 'password2']

class PassengerForm(ModelForm):
    class Meta:
        model = Passenger
        fields = ['FName','MName','LName','Gender','Address','ContactNumber','Email','SwabTestResult']

class BookingForm(ModelForm):
    class Meta:
        model = Bookings
        fields = ['TravelDate','PickupTerminal','DropoffTerminal','BusPlateNo']
