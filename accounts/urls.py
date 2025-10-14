from django.contrib import admin
from django.urls import path
from .views import register_doctor
from . import views

urlpatterns = [
    path('signup/',views.signup_view, name='signup'),
    path('doctor_register/', register_doctor, name='register_doctor'), 
    path('register/', views.Register_User, name='register'),
    path('verify-otp/<int:otp_id>/', views.verify_otp, name='verify_otp'),
    path('verify-doctor-otp/<int:otp_id>/', views.verify_doctor_otp, name='verify_doctor_otp'),
    path('resend-otp/<int:otp_id>/', views.Resend_otp_code, name='resend_otp'),
    path('resend-doctor-otp/<int:otp_id>/', views.resend_doctor_otp, name='resend_doctor_otp'),
    path('logout/', views.logout_view, name='Logout'),
    path("register-phone/", views.Register_phone, name="register_phone"),
    path("register-doctor-phone/", views.register_doctor_phone, name="register_doctor_phone"),
    path('profile/', views.profile_view, name='profile'),]
