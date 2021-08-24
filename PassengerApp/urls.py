from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('register/', views.registerPage, name="register"),
    path('', views.loginPage, name="login"),  
    path('logout/', views.logoutUser, name="logout"),
    path('', views.home, name="home"),
    path('welcome-passenger', views.welcomeuser, name="welcomeuser"),
    path('profilesetup/', views.profilesetup, name="profilesetup"),
    path('addbooking/', views.addbooking, name="addbook"),
    path('adminaccess/', views.adminaccess, name="adminaccess"),
    path('about/', views.about, name="about"),
    path('passenger/<str:pk_test>/', views.passenger, name="passenger"),
    # path('updatepassenger/<str:pk>/', views.updatePassenger, name="updatepassenger"),
    # path('updatebooking/<str:pk>/', views.updateBooking, name="updatebooking"),
]

if settings.DEBUG:
     urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)