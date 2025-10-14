from django.contrib import admin
from django.urls import path

from .views import * 

urlpatterns = [
    path('dashboard/', dashboard, name='admin_dashboard'),
    path('admin-login/', adminlogin, name='admin_login'),
    path('admin-logout/', admin_logout, name='admin_logout'),

     path('doctor_list/',doctor_list  , name ='doctor-list'),
     path('doctor_add/', doctor_add , name ='doctor-add'),
     path('doctor_edit/<int:pk>', doctor_edit , name ='doctor-edit'),
     path('doctor_delete/<int:pk>', doctor_delete , name ='doctor-delete'),

     path('specialty_list/', specialty_list , name ='specialty-list'),
     path('specialty_add/', specialty_add , name ='specialty-add'),
     path('specialty_edit/<int:pk>', specialty_edit , name ='specialty-edit'),
     path('specialty_delete/<int:pk>', specialty_delete , name ='specialty-delete'),

     path('service_list/',service_list  , name ='service-list'),
     path('service_add/', service_add , name ='service-add'),
     path('service_edit/<int:pk>', service_edit , name ='service-edit'),
     path('service_delete/<int:pk>', service_delete , name ='service-delete'),

     path('insurance_list/',insurance_list  , name ='insurance-list'),
     path('insurance_add/', insurance_add , name ='insurance-add'),
     path('insurance_edit/<int:pk>', insurance_edit , name ='insurance-edit'),
     path('insurance_delete/<int:pk>', insurance_delete , name ='insurance-delete'),


     path('appointment_list/', appointment_list  , name ='appointment-list'),
     path('appointment_add/', appointment_add , name ='appointment-add'),
     path('appointment_edit/<int:pk>', appointment_edit , name ='appointment-edit'),
     path('appointment_delete/<int:pk>', appointment_delete , name ='appointment-delete'),
    

     path('city_list/',city_list  , name ='city-list'),
     path('city_add/', city_add , name ='city-add'),
     path('city_edit/<int:pk>', city_edit , name ='city-edit'),
     path('city_delete/<int:pk>', city_delete , name ='city-delete'),


     
     path('clinic_list/',clinic_list  , name ='clinic-list'),
     path('clinic_add/', clinic_add , name ='clinic-add'),
     path('clinic_edit/<int:pk>', clinic_edit , name ='clinic-edit'),
     path('clinic_delete/<int:pk>', clinic_delete , name ='clinic-delete'),
   

     path('paraclinic_list/',paraclinic_list  , name ='paraclinic-list'),
     path('paraclinic_add/', paraclinic_add , name ='paraclinic-add'),
     path('paraclinic_edit/<int:pk>', paraclinic_edit , name ='paraclinic-edit'),
     path('paraclinic_delete/<int:pk>', paraclinic_delete , name ='paraclinic-delete'),

     path('pharmacy_list/',pharmacy_list  , name ='pharmacy-list'),
     path('pharmacy_add/', pharmacy_add , name ='pharmacy-add'),
     path('pharmacy_edit/<int:pk>', pharmacy_edit , name ='pharmacy-edit'),
     path('pharmacy_delete/<int:pk>', pharmacy_delete , name ='pharmacy-delete'),

     

     
     path('labsp_list/',labsp_list  , name ='labs-list'),
     path('labsp_add/', labsp_add , name ='labs-add'),
     path('labsp_edit/<int:pk>', labsp_edit , name ='labs-edit'),
     path('labsp_delete/<int:pk>', labsp_delete , name ='labs-delete'),


     path('review_list/',review_list  , name ='review-list'),
     path('review_add/', review_add , name ='review-add'),
     path('review_edit/<int:pk>', review_edit , name ='review-edit'),
     path('review_delete/<int:pk>', review_delete , name ='review-delete'),



     path('online_list/',online_list  , name ='online-list'),
     path('online_add/', online_add , name ='online-add'),
     path('online_edit/<int:pk>', online_edit , name ='online-edit'),
     path('online_delete/<int:pk>', online_delete , name ='online-delete'),

     path('khadamat_list/',khadamat_list  , name ='khadamat-list'),
     path('khadamat_add/', khadamat_add , name ='khadamat-add'),
     path('khadamat_edit/<int:pk>', khadamat_edit , name ='khadamat-edit'),
     path('khadamat_delete/<int:pk>', khadamat_delete , name ='khadamat-delete'),



     path('pishnahad_list/',pishnahad_list  , name ='pishnahad-list'),
     path('pishnahad_add/', pishnahad_add , name ='pishnahad-add'),
     path('pishnahad_edit/<int:pk>', pishnahad_edit , name ='pishnahad-edit'),
     path('pishnahad_delete/<int:pk>', pishnahad_delete , name ='pishnahad-delete'),


     path('pishnahad_img_list/',pishnahadimg_list  , name ='pishnahadimg-list'),
     path('pishnahad_img_add/', pishnahadimg_add , name ='pishnahadimg-add'),
     path('pishnahad_img_edit/<int:pk>', pishnahadimg_edit , name ='pishnahadimg-edit'),
     path('pishnahad_img_delete/<int:pk>', pishnahadimg_delete , name ='pishnahadimg-delete'),



     path('phone_list/',phone_list  , name ='phone-list'),
     path('phone_add/', phone_add , name ='phone-add'),
     path('phone_edit/<int:pk>', phone_edit , name ='phone-edit'),
     path('phone_delete/<int:pk>', phone_delete , name ='phone-delete'),

     path('text_list/',text_list  , name ='text-list'),
     path('text_add/', text_add , name ='text-add'),
     path('text_edit/<int:pk>', text_edit , name ='text-edit'),
     path('text_delete/<int:pk>', text_delete , name ='text-delete'),


     path('info_list/',patient_info_list  , name ='info-list'),
     path('info_add/', patient_info_add , name ='info-add'),
     path('info_edit/<int:pk>', patient_info_edit , name ='info-edit'),
     path('info_delete/<int:pk>', patient_info_delete , name ='info-delete'),



     path('faq_list/',faq_list  , name ='faq-list'),
     path('faq_add/', faq_add , name ='faq-add'),
     path('faq_edit/<int:pk>', faq_edit , name ='faq-edit'),
     path('faq_delete/<int:pk>', faq_delete , name ='faq-delete'),




     path('user_list/',user_list  , name ='user-list'),
     path('user_add/', user_add , name ='user-add'),
     path('user_edit/<int:pk>', user_edit , name ='user-edit'),
     path('user_delete/<int:pk>', user_delete , name ='user-delete'),



     path('userotp_list/',userotp_list  , name ='userotp-list'),
     path('userotp_add/', userotp_add , name ='userotp-add'),
     path('userotp_edit/<int:pk>', userotp_edit , name ='userotp-edit'),
     path('userotp_delete/<int:pk>', userotp_delete , name ='userotp-delete'),


     path('wallet_list/',wallet_list  , name ='wallet-list'),
     path('wallet_add/', wallet_add , name ='wallet-add'),
     path('wallet_edit/<int:pk>', wallet_edit , name ='wallet-edit'),
     path('wallet_delete/<int:pk>', wallet_delete , name ='wallet-delete'),



     path('register_list/',doctor_register_list  , name ='register-list'),
     path('register_add/', doctor_register_add , name ='register-add'),
     path('register_edit/<int:pk>', doctor_register_edit , name ='register-edit'),
     path('register_delete/<int:pk>', doctor_register_delete , name ='register-delete'),




     path('type_list/',type_list  , name ='type-list'),
     path('type_add/', type_add , name ='type-add'),
     path('type_edit/<int:pk>', type_edit , name ='type-edit'),
     path('type_delete/<int:pk>', type_delete , name ='type-delete'),
     

     path('post_list/',post_list  , name ='post-list'),
     path('post_add/', post_add , name ='post-add'),
     path('post_edit/<int:pk>', post_edit , name ='post-edit'),
     path('post_delete/<int:pk>', post_delete , name ='post-delete'),



     path('social_list/',social_link_list  , name ='social-link-list'),
     path('social_add/', social_link_add , name ='social-add'),
     path('social_edit/<int:pk>', social_link_edit , name ='social-edit'),
     path('social_delete/<int:pk>', social_link_delete , name ='social-delete'),



     path('blog_faq_list/',blog_faq_list  , name ='blog-faq-list'),
     path('blog_faq_add/', blog_faq_add , name ='blog-faq-add'),
     path('blog_faq_edit/<int:pk>', blog_faq_edit , name ='blog-faq-edit'),
     path('blog_faq_delete/<int:pk>', blog_faq_delete , name ='blog-faq-delete'),




     path('medical_type_list/',medical_center_type_list  , name ='medical-type-list'),
     path('medical_type_add/', medical_center_type_add, name ='medical-type-add'),
     path('medical_type_edit/<int:pk>', medical_center_type_edit , name ='medical-type-edit'),
     path('medical_type_delete/<int:pk>', medical_center_type_delete , name ='medical-type-delete'),



     path('most_visited_list/',most_visited_specializations_list  , name ='most-visited-list'),
     path('most_visited_add/', most_visited_specializations_add, name ='most-visited-add'),
     path('most_visited_edit/<int:pk>', most_visited_specializations_edit , name ='most-visited-edit'),
     path('most_visited_delete/<int:pk>', most_visited_specializations_delete , name ='most-visited-delete'),




     path('sympots_list/',symptoms_and_disease_list  , name ='sympots-list'),
     path('sympots_add/', symptoms_and_disease_add , name ='sympots-add'),
     path('sympots_edit/<int:pk>', symptoms_and_disease_edit , name ='sympots-edit'),
     path('sympots_delete/<int:pk>', symptoms_and_disease_delete , name ='sympots-delete'),



     path('center_list/',centers_for_diagnosis_and_treatment_list  , name ='center-list'),
     path('center_add/', centers_for_diagnosis_and_treatment_add , name ='center-add'),
     path('center_edit/<int:pk>', centers_for_diagnosis_and_treatment_edit , name ='center-edit'),
     path('center_delete/<int:pk>', centers_for_diagnosis_and_treatment_delete , name ='center-delete'),



     path('latset_list/',latest_medical_centers_list  , name ='latest-medical-list'),
     path('latset_add/', latest_medical_centers_add , name ='latest-medical-add'),
     path('latset_edit/<int:pk>', latest_medical_centers_edit , name ='latset-medical-edit'),
     path('latset_delete/<int:pk>', latest_medical_centers_delete , name ='latset-medical-delete'),



     path('top_list/',top_clinics_list  , name ='top-clinics-list'),
     path('top_add/', top_clinics_add , name ='top-clinics-add'),
     path('top_edit/<int:pk>', top_clinics_edit, name ='top-clinics-edit'),
     path('top_delete/<int:pk>', top_clinics_delete, name ='top-clinics-delete'),



     path('city_lab_list/',cities_with_doctor_to_labs_list , name ='city-lab-list'),
     path('city_lab_add/', cities_with_doctor_to_labs_add , name ='city-lab-add'),
     path('city_lab_edit/<int:pk>', cities_with_doctor_to_labs_edit, name ='city-lab-edit'),
     path('city_lab_delete/<int:pk>', cities_with_doctor_to_labs_delete, name ='city-lab-delete'),




     path('comment_list/',comment_list  , name ='comment-list'),
     path('comment_add/', comment_add , name ='comment-add'),
     path('comment_edit/<int:pk>', comment_edit , name ='comment-edit'),
     path('comment_delete/<int:pk>', comment_delete , name ='comment-delete'),



     
     path('sympots_women_list/', symptoms_and_diseases_of_women_list  , name ='sympots-women-list'),
     path('sympots_women_add/', symptoms_and_diseases_of_women_add , name ='sympots-women-add'),
     path('sympots_women_edit/<int:pk>', symptoms_and_diseases_of_women_edit , name ='sympots-women-edit'),
     path('sympots_women_delete/<int:pk>', symptoms_and_diseases_of_women_delete, name ='sympots-women-delete'),


     path('online_medical_list/',online_medical_list , name ='online-medical-list'),
     path('online_medical_add/', online_medical_add , name ='online-medical-add'),
     path('online_medical_edit/<int:pk>', online_medical_edit , name ='online-medical-edit'),
     path('online_medical_delete/<int:pk>', online_medical_delete , name ='online-medical-delete'),

    path('lab_list/',lab_list , name ='lab-list'),
     path('lab_add/', lab_add , name ='lab-add'),
     path('lab_edit/<int:pk>', lab_edit , name ='lab-edit'),
     path('lab_delete/<int:pk>', lab_delete , name ='lab-delete'),
]


