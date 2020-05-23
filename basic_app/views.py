from django.shortcuts import render
from basic_app.forms import DoctorRegistrationForm, PatientRegistrationForm

from django.views.generic import View,TemplateView,ListView, DetailView, CreateView, UpdateView, DeleteView
# Create your views here.

class IndexView(TemplateView):
    template_name  = 'index.html'

def d_register(request):
    d_registered = False
    if request.method == 'POST':
        doctor_form = DoctorRegistrationForm(data=request.POST)
        if doctor_form.is_valid():
            doctor = doctor_form.save()        
            doctor.set_password(doctor.d_password)       
            doctor.save()
            d_registered = True
        else:
            print(doctor_form.errors)
    else:
        doctor_form = DoctorRegistrationForm()
    return render(request,'basic_app/d_registration.html',{'doctor_form':doctor_form,
                                                            'd_registered':d_registered})

def p_register(request):
    p_registered = False
    if request.method == 'POST':
        patient_form = PatientRegistrationForm(data=request.POST)
        if patient_form.is_valid():
            patient = patient_form.save()        
            patient.set_password(patient.p_password)       
            patient.save()
            p_registered = True
        else:
            print(patient_form.errors)
    else:
        patient_form = PatientRegistrationForm()
    return render(request,'basic_app/registration.html',{'patient_form':patient_form,
                                                            'p_registered':p_registered})