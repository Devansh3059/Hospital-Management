from django.conf.urls import url
from basic_app import views

app_name = 'basic_app'

urlpatterns = [
    url(r'^register_as_doctor/$',views.d_register,name= 'd_register'),
    url(r'^register_as_patient/$',views.p_register,name= 'p_register'),

]