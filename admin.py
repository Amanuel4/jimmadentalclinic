from django.contrib import admin
from .models import Customer, Dentist, CaseandPricing, Classroom,Appointment

# Register your models here.
admin.site.register(Customer)
admin.site.register(Dentist)
admin.site.register(CaseandPricing)
admin.site.register(Classroom)
admin.site.register(Appointment)