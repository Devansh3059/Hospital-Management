from django.db import models

# Create your models here.
class Doctors(models.Model):
    d_name = models.CharField(max_length=100)
    d_email = models.EmailField(max_length=100)

    def __str__(self):
        return self.d_name

class Patients(models.Model):
    p_name = models.CharField(max_length=100)
    p_email = models.EmailField(max_length=100)

    def __str__(self):
        return self.p_name