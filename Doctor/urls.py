from django.urls import path
from django.shortcuts import render 
from .views import (
    doctors_list,
    show_doctor_select,
    online_consultation,
     book_appointment,
     doctor_appointments,
     appointment_list,
     rate_doctor, 
     appointment_detail,
     payment,
     payment_verify,
     doctor_profile,
     Phone_appointment_list,
     text_appointment_list,
     doctor_review
)


urlpatterns = [
    #   List of all doctors

    path('doctors/', doctors_list, name='doctor_list'),

    # Choose a doctor to make an appointment with (optional)
    path('select/', show_doctor_select, name='select_doctor'),

    # Show slots for all doctors categorized (weekly)

    path('online/',online_consultation, name='online'),

    path('nobat/<int:appointment_id>/', book_appointment, name='nobat'),
    path('doctor/<int:doctor_id>/appointments/', doctor_appointments, name='doctor_appointments'),
    path('appointments/', appointment_list, name='appointment_list'),
    path('rate/<int:pk>/', rate_doctor , name='rate'),
    path('appointment_detail/<appointment_id>/',appointment_detail , name='appointment_detail' ),
     path('appointment/<int:appointment_id>/payment/', payment, name='payment'),
    path('appointment/<int:appointment_id>/payment/verify/', payment_verify, name='payment_verify'),
    path('doctor_profile/<int:pk>/', doctor_profile ,  name='doctor_profile'),
    path('phone/',  Phone_appointment_list , name ='phone_list'),
    path('text/', text_appointment_list , name = 'text_list'),
    path("doctor/<int:pk>/review/", doctor_review, name="doctor-review"),
]
