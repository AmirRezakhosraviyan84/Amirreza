from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views
urlpatterns = [
    path('',views.home_view , name='home'),
    path('search/', views.search_view, name='search'),
    path('nobatazmayeshgah',views.nobat_azemayeshgah, name='nobat_azmayeshgah'),
    path('medicalcenters/', views.medical_center_list, name='medicalcenter-list'),
    path('top_clinics/<int:pk>/',views.medical_center_view, name = 'top_clinic'),
    path('medical/',views.medical_center_list, name='medicalcenter_list'),
    path('top_clinic_detail/<int:pk>/',views.top_clinic_detail, name='top_clinic_detail'),
    path('medical-centers_detail/<int:pk>/', views.medical_center_detail, name='medical_center_detail'),
    path('medical_center_type_detail/<int:pk>/',views.medical_center_type_detail, name = 'type_detail'),
    path('city_detail/<int:pk>/',views.city_detail, name ='city_detail' ),
    path('specialty_detail/<int:pk>/', views.specialty_detail , name = 'specialty_detail'),
    path('latest_center_detail/<int:pk>/', views.latest_center_detail , name='latest_center_detail'),
    path('most_visited_detail/<int:pk>', views.most_visited_detail , name = 'visited_detail'),
    path('Symptoms_and_disease_detail/<int:pk>', views.Symptoms_and_disease_detail , name= 'Symptoms_and_disease_detail'),
    path('Online_detail/<int:pk>/', views.Online_detail , name = 'online_detail'),
    path('dr_tavloly_doctors/<int:clinic_id>/', views.clinics_doctor , name='clinic_doctors'),
    path('labratory_detail/<int:pk>/', views.labratory_detail , name='labratory_detail'),
     path('search_lab/', views.search_to_lab_detail, name='search_to_lab_detail'),
     path('doctor_to_services/', views.doctor_to_services , name = 'doctor_to_services'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

