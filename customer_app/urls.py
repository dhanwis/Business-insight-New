from django.urls import path
from .views import home, about, contact, services_details,services

urlpatterns = [
    path('', home, name='home'),
    path('about/', about, name='about'),
    path('services/',services, name='services'),
    path('contact/',contact, name='contact'),
    path('services/details/',services_details,name='services_details'),
]