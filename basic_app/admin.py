from django.contrib import admin
from basic_app.models import Doctors, Patients

# Register your models here.
admin.site.register(Doctors)
admin.site.register(Patients)
