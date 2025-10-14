from django.contrib import admin
from . models import Doctor,Specialty,Service,City,Insurance,Onlinemedicalconsultation,clinic,Paraclinicservices,pharmacy,labratory,Lab_specialty
from. models import khadamat,Pishnahad,PishnahadImage,Appointment,PatientInfo,DoctorRating,FAQ,Phone_Appointment , Text_Appointment ,Review
# Register your models here.
@admin.register(Doctor)

class DoctorAdmin(admin.ModelAdmin):
    list_display = ['name',]


@admin.register(Specialty)
class SpecialtyAdmin(admin.ModelAdmin):
    list_display =['name',]    

@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display =['name',] 


@admin.register(City)
class CityAdmin(admin.ModelAdmin):
    list_display =['name',] 



@admin.register(Insurance)
class InsuranceAdmin(admin.ModelAdmin):
    list_display =['name',]     


class ClinicAdmin(admin.ModelAdmin):
    list_display = ("name", "get_doctors")

    def get_doctors(self, obj):   # 👈 باید داخل کلاس admin باشه
        return ", ".join([d.name for d in obj.doctors.all()])
    get_doctors.short_description = "Doctors"

admin.site.register(clinic,ClinicAdmin )

@admin.register(Onlinemedicalconsultation)

class OnlinemedicalconsultationAdmin(admin.ModelAdmin):
    list_display =['doctor','specialty']


@admin.register(Paraclinicservices)

class ParaclinicservicesAdmin(admin.ModelAdmin):
    list_display=['name']


@admin.register(pharmacy)

class pharmacyAdmin(admin.ModelAdmin):
    list_display =['name']


@admin.register(labratory)

class labratoryAdmin(admin.ModelAdmin):
    list_display =['name']


@admin.register(Lab_specialty)

class Lab_specialtyAdmin(admin.ModelAdmin):
    list_display =['name']



@admin.register(khadamat)

class khadamatAdmin(admin.ModelAdmin):
    list_display =['name']


@admin.register(PishnahadImage)   

class PishnahadImageAdmin(admin.ModelAdmin):
    list_display =['pishnahad']


@admin.register(Pishnahad)    

class PishnahadAdmin(admin.ModelAdmin):
    list_display =['title']


@admin.register(Appointment)

class AppointmentAdmin(admin.ModelAdmin):
    list_display =['doctor','date']

@admin.register(PatientInfo)    

class PatientInfoAdmin(admin.ModelAdmin):

    list_display =['first_name','last_name']


@admin.register(DoctorRating)

class DoctorRatingAdmin(admin.ModelAdmin):

    list_display =['doctor','user','score',]


@admin.register(FAQ)


class FAQAdmin(admin.ModelAdmin):

    list_display=['question','answer', 'order']
    

@admin.register(Phone_Appointment)


class Phone_AppointmentAdmin(admin.ModelAdmin):

    list_display =['doctor', 'date', 'time']


@admin.register(Text_Appointment)


class Text_AppointmentAdmin(admin.ModelAdmin):

    list_display =['doctor', 'date', 'time']


@admin.register(Review)

class ReviewAdmin(admin.ModelAdmin):

    list_display =['doctor','user','overall']