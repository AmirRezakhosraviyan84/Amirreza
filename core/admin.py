from django.contrib import admin
from . models import City , MedicalCenterType, Mostvisitedspecializations,Symptoms_and_disease,Onlinemedical,SpecialtiesofDoctorToomedicalcenters,Centersfordiagnosisandtreatmentofsymptomsanddiseases
from. models import Thelatestmedicalcenters,TopClinics,CitieswithDoctorToolaboratories,Comment,Symptomsanddiseasesofwomen, Medical_Centers
@admin.register(City)

class CityAdmin(admin.ModelAdmin):
    list_display =['name',]

@admin.register(MedicalCenterType)
class MedicalCenterTypeAdmin(admin.ModelAdmin):
  list_display = ['title',]    


@admin.register(Mostvisitedspecializations)
class MostvisitedspecializationsAdmin(admin.ModelAdmin):
   list_display = ['title',]

@admin.register(Symptoms_and_disease)
class Symptoms_and_diseaseAdmin(admin.ModelAdmin):
   list_display =['title','image']  


@admin.register(Onlinemedical)

class OnlinemedicalAdmin(admin.ModelAdmin):
   list_display = ['title',]

@admin.register(SpecialtiesofDoctorToomedicalcenters)

class SpecialtiesofDoctorToomedicalcentersAdmin(admin.ModelAdmin):
   list_display =['title','image',]

@admin.register(Centersfordiagnosisandtreatmentofsymptomsanddiseases)
class CentersfordiagnosisandtreatmentofsymptomsanddiseasesAdmin(admin.ModelAdmin):
   list_display = ['title',]


@admin.register(Thelatestmedicalcenters)

class ThelatestmedicalcentersAdmin(admin.ModelAdmin):

   list_display = ['title','image',]


@admin.register(TopClinics)   

class TopClinicsAdmin(admin.ModelAdmin):
   list_display = ['title','image','location']


@admin.register(CitieswithDoctorToolaboratories)

class CitieswithDoctorToolaboratoriesAdmin(admin.ModelAdmin):
   list_display = ['name',]

@admin.register(Comment)

class CommentAdmin(admin.ModelAdmin):
   list_display =['title','author']


@admin.register(Symptomsanddiseasesofwomen)

class SymptomsanddiseasesofwomenAdmin(admin.ModelAdmin):
   list_display =['title']

@admin.register(Medical_Centers)

class Medical_CentersAdmin(admin.ModelAdmin):
   list_display =['type', 'name']