from PassengerApp.models import Bookings, Passenger
from django.shortcuts import render, redirect
from .forms import PassengerForm, BookingForm, CreateUserForm
from .filters import BookingFilter, PassengerFilter

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .decorators import unauthenticated_user, allowed_users
from django.contrib.auth.models import Group

@unauthenticated_user
def registerPage(request):
	if request.user.is_authenticated:
		return redirect('login')

	else:
		form = CreateUserForm()

		if request.method == 'POST':
			form = CreateUserForm(request.POST)
			if form.is_valid():
				user = form.save()
				username = form.cleaned_data.get('username')

				group = Group.objects.get(name='passenger')
				user.groups.add(group)
				
				messages.success(request, 'Account was created for ' + username)

				return redirect('login')
			

		context = {'form':form}
		return render(request, 'html/user-setup.html', context)

@unauthenticated_user
def loginPage(request):
	username = None
	password = None

	if request.user.is_authenticated :
		return redirect('login')
	else:
		if request.method == 'POST':
			username = request.POST.get('username')
			password =request.POST.get('password')
        
		user = authenticate(request, username=username, password=password)

		if (user is not None and user.is_active):
		    login(request, user)
		    return redirect('welcomeuser')

	context = {}
	return render(request, 'html/login.html', context)


def logoutUser(request):
	logout(request)
	return redirect('login')

def home(request):
    return render(request, 'html/home.html')

#USER WELCOME PAGE FOR ACTIVE
@login_required(login_url='login') 
def welcomeuser(request):
    return render(request, 'html/home-profile.html')

#READ PROFILE FOR USER
@login_required(login_url='login')
def passenger(request, pk_test):
    passenger = Passenger.objects.get(id=pk_test)
    booking = passenger.bookings_set.all()
    pasbook = Bookings.objects.count()
    context = {'passenger': passenger, 'booking': booking, 'pasbook':pasbook}
    return render (request, 'html/profile.html', context)


#CREATE USER PROFILE (USER REGISTRATION)
@login_required(login_url='login')
@allowed_users(allowed_roles=['passenger'])
def profilesetup(request):
    if request.user.is_authenticated and request.user.is_superuser:
		    return redirect('adminaccess')

    form = PassengerForm()
    if request.method == 'POST':
        form = PassengerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/addbooking')
    context = {'form': form}
    return render(request, 'html/profile-setup.html', context)

#CREATE USER BOOKING (FOR EXISTING USERS)
@login_required(login_url='login')
@allowed_users(allowed_roles=['passenger'])
def addbooking(request):
    form = BookingForm()
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('welcomeuser')
    context = {'form': form}

    return render(request, 'html/addbook.html', context)

#READ USER FOR ADMIN
@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def adminaccess(request):   
    passengers = Passenger.objects.all()
    bookings = Bookings.objects.all()

    totreg = Passenger.objects.count()
    totbook = Bookings.objects.count()
    
    BookFilter = BookingFilter(request.GET, queryset=Bookings.objects.filter())
    bookings = BookFilter.qs

    PassFilter = PassengerFilter(request.GET, queryset=Passenger.objects.filter())
    passengers = PassFilter.qs
    context = {'passengers':passengers, 'bookings':bookings, 'totreg':totreg, 'totbook':totbook, 'BookFilter':BookFilter, 'PassFilter': PassFilter, }
    return render(request, 'html/adminaccess.html', context)

# 

def about(request):
    return render(request, 'html/about.html')







