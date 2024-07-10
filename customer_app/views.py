from django.shortcuts import render
from .models import Service
# Create your views here.

def home(request):
    current_page = 'home'
    context = {
        'current_page': current_page
    }
    return render(request, 'customer_app/pages/home.html', context)

def about(request):
    current_page = 'about'
    context = {
        'current_page': current_page
    }
    return render(request, 'customer_app/pages/about.html', context)


def services(request):
    current_page = 'services'
    
    context = {
        'current_page':current_page,
        'services': services,

    }
    return render(request, 'customer_app/pages/services.html', context)

def contact(request):
    current_page = 'contact'
    context = {
        'current_page':current_page
    }
    return render(request, 'customer_app/pages/contact.html', context)

def services_details(request):
    current_page = 'services_details'
    context = {
        'current_page': current_page
    }
    return render(request, 'customer_app/pages/services_details.html', context)

def blog(request):
    current_page = 'blog'
    context = {
        'current_page': current_page
    }
    return render(request, 'customer_app/pages/blog.html', context)