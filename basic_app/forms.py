from django import forms
from basic_app.models import Doctors, Patients


class DoctorRegistrationForm(forms.ModelForm):
    d_password = forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model = Doctors
        fields = ('d_name', 'd_email',"d_password") 

class PatientRegistrationForm(forms.ModelForm):
    p_password = forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model = Patients
        fields = ('p_name', 'p_email','p_password') 