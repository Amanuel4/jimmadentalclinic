"""dentalclinic URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from . import views

app_name="main"
urlpatterns = [
	path('', views.homepage, name='homepage'),
	path('doctors.html', views.doctors, name="doctors"),
	path('service.html', views.service, name="service"),
    path('about.html', views.about, name="about"),
    path('contactview.html', views.contactview, name="contactview"),
	path('appointment.html', views.appointment, name="appointment"),
    path('appointmentlist.html', views.appointmentlist, name="appointmentlist"),
    path("register.html", views.register, name="register"),
    path("contact.html", views.contact, name="contact"),
    path("logout/", views.logout_request, name='logout'),
    path("login.html", views.login_request, name='login'),
    path("join/", views.join, name="join"),
    path("subscribe.html", views.subscribe, name="subscribe"),
    path("join/", views.join, name="join"),
]
