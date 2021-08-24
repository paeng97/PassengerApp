from django.db import models
from datetime import date

# Create your models here.

class Passenger(models.Model):
	Gchoices =	[
		('Male', 'Male'),
        ('Female', 'Female'),
	]
	category = 	[
		('Negative', 'Negative'),
        ('Positive', 'Positive'),
	]
	Email = models.EmailField(verbose_name="Email", max_length=70, help_text="Note: Provide your most used email account")
	Passcode = models.CharField(verbose_name="Password", max_length=50)
	Username = models.CharField(verbose_name="Username", max_length=50)
	FName = models.CharField(verbose_name="First Name", max_length=50 )
	MName = models.CharField(verbose_name="Middle Name",  max_length=50)
	LName = models.CharField(verbose_name="Last Name",  max_length=50)
	Gender = models.CharField(max_length=10, choices= Gchoices, verbose_name="Gender")
	Address = models.CharField(verbose_name="Address",  max_length=300, help_text="Note: Provide your present full address")
	ContactNumber = models.DecimalField(max_digits = 11, decimal_places=0, verbose_name="Contact Number", help_text="Note: Provide your active phone number")
	SwabTestResult = models.CharField(max_length=10, choices=category, verbose_name="Swab Test Result")
	DateRegistered = models.DateField(blank=True, auto_now_add=True, null=True, help_text="Today Date.")

	def __str__(self):
		return self.FName

class Bookings(models.Model):
	PickChoices =	[
		('Starmall - Alabang', 'Starmall - Alabang'),
		('Pilar Station - Las Pinas', 'Pilar Station - Las Pinas'),
		('Southmall - Las Pinas', 'Southmall - Las Pinas'),
		('Trasierra - Makati', 'Trasierra - Makati'),
	]
	DropChoices =	[
		('Pala-Pala - Dasmariñas', 'Pala-Pala - Dasmariñas'),
		('Vista Mall - Dasmariñas', 'Vista Mall - Dasmariñas'),
		('Camella Dasmariñas', 'Camella Dasmariñas'),
		('Savemore Salitran - Dasmariñas', 'Savemore Salitran - Dasmariñas'),
		('Seaoil Salawag - Dasmariñas', 'Seaoil Salawag - Dasmariñas'),
		('The District Imus', 'The District Imus'),
		('Vista Mall Nomo Bacoor', 'Vista Mall Nomo Bacoor'),
		('Vista Mall Daang Hari', 'Vista Mall Daang Hari'),
		('Noveleta', 'Noveleta'),
	]
	Name = models.ForeignKey(Passenger, null=True, on_delete=models.CASCADE)
	PickupTerminal = models.CharField(max_length=30, choices= PickChoices, verbose_name="Pickup Place")
	DropoffTerminal = models.CharField(max_length=30, choices= DropChoices, verbose_name="Dropoff Place")
	TravelDate = models.DateField(blank=True, default=date(2021, 12, 31), null=True, help_text="Note: Please follow this format YYYY-MM-DD*")
	BusPlateNo = models.CharField(max_length = 9, verbose_name = "Bus Plate No.")

	def __str__(self):
		return self.PickupTerminal


