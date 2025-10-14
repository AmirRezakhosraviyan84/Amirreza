from django import forms
from Doctor.models import (Doctor, Specialty, Service, City, Insurance,clinic,Paraclinicservices,pharmacy,Lab_specialty,labratory,Review,Onlinemedicalconsultation,khadamat,
Pishnahad,PishnahadImage,Phone_Appointment,Text_Appointment,PatientInfo,FAQ,Order,Appointment)
from accounts.models import (CustomUser,UserOTP,Wallet,Doctor_register)
from blog.models import (type,Post,Social_link,FAQ)
from core.models import(MedicalCenterType,Medical_Centers,Mostvisitedspecializations,Symptoms_and_disease,
SpecialtiesofDoctorToomedicalcenters,Centersfordiagnosisandtreatmentofsymptomsanddiseases,Thelatestmedicalcenters,
TopClinics,CitieswithDoctorToolaboratories,Comment,Symptomsanddiseasesofwomen,Onlinemedical)
from blog.models import Post

class AdminLoginForm(forms.Form):
    phone_number =forms.CharField(
        max_length=11,
        label='شماره موبایل',
        widget=forms.TextInput(attrs={
            'class':'form-control',
            'placeholder': 'مثلاً 09120000000' 
        })
    )

    password =forms.CharField(
        label='رمز عبور',
        widget=forms.PasswordInput(attrs={
            'class':'form-control',
            'placeholder':'رمز عبور'
        })
    )

#  start doctor model forms
class doctor_form(forms.ModelForm):

    class Meta:
        model=Doctor
        fields ='__all__'

class SpecialtyForm(forms.ModelForm):
    class Meta:
        model = Specialty
        fields = '__all__'


class ServiceForm(forms.ModelForm):
    class Meta:
        model = Service
        fields ='__all__'   


class InsuranceForm(forms.ModelForm):
    class Meta:
        model = Insurance
        fields = '__all__'



class AppointmentForm(forms.ModelForm):
    class Meta:
        model = Appointment
        fields = '__all__'



class city_form(forms.ModelForm):

    class Meta:
        model =City
        fields ='__all__'

class clinic_form(forms.ModelForm):
    class Meta:
        model =clinic
        fields ='__all__'

class Paraclinicservices_form(forms.ModelForm):

    class Meta:
        model =Paraclinicservices
        fields ='__all__'

class pharmacy_forms(forms.ModelForm):

    class Meta:
        model =pharmacy
        fields ='__all__'


class Lab_specialty_forms(forms.ModelForm):

    class Meta:
        model =Lab_specialty
        fields ='__all__'

class labratory_forms(forms.ModelForm):

    class Meta:
        model = labratory  
        fields ='__all__'   


class Review_forms(forms.ModelForm):

    class Meta:
        model = Review 
        fields ='__all__'


class Onlinemedicalconsultation_forms(forms.ModelForm):

    class Meta:
        model =Onlinemedicalconsultation
        fields ='__all__'

class khadamat_forms(forms.ModelForm):

    class Meta:
        model = khadamat    
        fields ='__all__'


class Pishnahad_forms(forms.ModelForm):

    class Meta:
        model =  Pishnahad
        fields ='__all__'

class PishnahadImage_forms(forms.ModelForm):

    class Meta:
        model = PishnahadImage 
        fields ='__all__'


class Phone_Appointment_forms(forms.ModelForm):

    class Meta:
        model = Phone_Appointment   
        fields ='__all__'


class Text_Appointment_forms(forms.ModelForm):

    class Meta:
        model =Text_Appointment  
        fields ='__all__'


class PatientInfo_forms(forms.ModelForm):


    class Meta:
        model =  PatientInfo   
        fields ='__all__'



class faq_forms(forms.ModelForm):

    class Meta:

        model =FAQ
        fields ='__all__'


class order_forms(forms.ModelForm):

    class Meta:

        model = Order

        fields ='__all__'

#end doctor models form


#start account models forms

class UserForm(forms.ModelForm):
    password = forms.CharField(required=False, widget=forms.PasswordInput, help_text="اگر می‌خواهید رمز را تغییر دهید بنویسید.")
        
    class Meta:
        model = CustomUser
        fields = ['phone_number','full_name','role','is_active','password']

    def save(self, commit=True):
        user = super().save(commit=False)
        pwd = self.cleaned_data.get('password')
        if pwd:
            user.set_password(pwd)
        if commit:
            user.save()
        return user
    

class userotp_forms(forms.ModelForm):

    class Meta:
        model =UserOTP
        fields ='__all__'


class wallet_forms(forms.ModelForm):

    class Meta:
        model =Wallet   
        fields ='__all__'


class doctor_register_forms(forms.ModelForm):    

    class Meta:
        model =Doctor_register
        fields ='__all__'   

#end account model forms


#start blog model forms

class type_form(forms.ModelForm):

    class Meta:

        model =type
        fields ='__all__'

class post_form(forms.ModelForm):

    class Meta:

        model =Post
        fields ='__all__'   

class social_forms(forms.ModelForm):

    class Meta:

        model = Social_link
        fields ='__all__'

class FAQ_forms(forms.ModelForm):

    class Meta:
        model =FAQ                     
        fields ='__all__'

 #end blog models form

#start core models form

class MedicalCenterType_forms(forms.ModelForm):

    class Meta:

        model =MedicalCenterType
        fields ='__all__'

class Medical_Centers_forms(forms.ModelForm):

    class Meta:

        model =Medical_Centers
        fields ='__all__'

class Mostvisitedspecializations_form(forms.ModelForm): 

    class Meta:

        model =Mostvisitedspecializations
        fields ='__all__'


class Symptoms_and_disease_forms(forms.ModelForm):

    class Meta:
        model =Symptoms_and_disease
        fields ='__all__'


class SpecialtiesofDoctorToomedicalcenters_form(forms.ModelForm):

    class Meta:

        model =SpecialtiesofDoctorToomedicalcenters
        fields ='__all__'  

class Centers_for_diagnosis_and_treatment_of_symptoms_and_diseases_form(forms.ModelForm):

    class Meta:
        model =  Centersfordiagnosisandtreatmentofsymptomsanddiseases  
        fields ='__all__'


class The_latest_medical_centers_form(forms.ModelForm):

    class Meta:
        model = Thelatestmedicalcenters
        fields = '__all__'



class TopClinics_form(forms.ModelForm):
     class meta:
         model =TopClinics           
         fields ='__all__'


class CitieswithDoctorToolaboratories_form(forms.ModelForm):

    class Meta:

        model =CitieswithDoctorToolaboratories
        fields ='__all__'

class Comment_form(forms.ModelForm):

    class Meta:

        model =Comment  
        fields ='__all__'

class Symptomsanddiseasesofwomen_form(forms.ModelForm):

    class Meta:
        model = Symptomsanddiseasesofwomen
        fields ='__all__'


class Onlinemedical_forms(forms.ModelForm):

    class Meta:
        model = Onlinemedical  
        fields ='__all__'            
