# Generated by Django 3.2.6 on 2021-08-24 05:38

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Passenger',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Email', models.EmailField(help_text='Note: Provide your most used email account', max_length=70, verbose_name='Email')),
                ('Passcode', models.CharField(max_length=50, verbose_name='Password')),
                ('Username', models.CharField(max_length=50, verbose_name='Username')),
                ('FName', models.CharField(max_length=50, verbose_name='First Name')),
                ('MName', models.CharField(max_length=50, verbose_name='Middle Name')),
                ('LName', models.CharField(max_length=50, verbose_name='Last Name')),
                ('Gender', models.CharField(choices=[('Male', 'Male'), ('Female', 'Female')], max_length=10, verbose_name='Gender')),
                ('Address', models.CharField(help_text='Note: Provide your present full address', max_length=300, verbose_name='Address')),
                ('ContactNumber', models.DecimalField(decimal_places=0, help_text='Note: Provide your active phone number', max_digits=11, verbose_name='Contact Number')),
                ('SwabTestResult', models.CharField(choices=[('Negative', 'Negative'), ('Positive', 'Positive')], max_length=10, verbose_name='Swab Test Result')),
                ('DateRegistered', models.DateField(auto_now_add=True, help_text='Today Date.', null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Bookings',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('PickupTerminal', models.CharField(choices=[('Starmall - Alabang', 'Starmall - Alabang'), ('Pilar Station - Las Pinas', 'Pilar Station - Las Pinas'), ('Southmall - Las Pinas', 'Southmall - Las Pinas'), ('Trasierra - Makati', 'Trasierra - Makati')], max_length=30, verbose_name='Pickup Place')),
                ('DropoffTerminal', models.CharField(choices=[('Pala-Pala - Dasmari??as', 'Pala-Pala - Dasmari??as'), ('Vista Mall - Dasmari??as', 'Vista Mall - Dasmari??as'), ('Camella Dasmari??as', 'Camella Dasmari??as'), ('Savemore Salitran - Dasmari??as', 'Savemore Salitran - Dasmari??as'), ('Seaoil Salawag - Dasmari??as', 'Seaoil Salawag - Dasmari??as'), ('The District Imus', 'The District Imus'), ('Vista Mall Nomo Bacoor', 'Vista Mall Nomo Bacoor'), ('Vista Mall Daang Hari', 'Vista Mall Daang Hari'), ('Noveleta', 'Noveleta')], max_length=30, verbose_name='Dropoff Place')),
                ('TravelDate', models.DateField(blank=True, default=datetime.date(2021, 12, 31), help_text='Note: Please follow this format YYYY-MM-DD*', null=True)),
                ('BusPlateNo', models.CharField(max_length=9, verbose_name='Bus Plate No.')),
                ('Name', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='PassengerApp.passenger')),
            ],
        ),
    ]
