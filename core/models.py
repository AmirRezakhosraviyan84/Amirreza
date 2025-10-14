from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
from django.utils import timezone



# Create your models here.
class core(models.Model):
    covers =models.ImageField(blank=True , upload_to='covers/')


class City(models.Model):
    name =models.CharField(max_length=100)

    def __str__(self):
        return self.name



class MedicalCenterType(models.Model):
    title =models.CharField(max_length=100) 
    image =models.ImageField(upload_to='icon')
    description = models.CharField(max_length=100,blank=True , null=True)   
    city = models.ForeignKey(City, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.title     
    

class Medical_Centers(models.Model):
    
    type =models.ForeignKey(MedicalCenterType, on_delete=models.CASCADE)
    name =models.CharField(max_length=100)
    image = models.ImageField(upload_to='icons')

    def __str__(self):
        return self.name


    
class Mostvisitedspecializations(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='icon')
    description=models.CharField(max_length=100,blank=True, null = True) 
    specialties =models.ManyToManyField('Doctor.Specialty', blank=True)
    city = models.ForeignKey(City, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.title
    

class Symptoms_and_disease(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='icon', null= True , blank=True)
    city = models.ForeignKey(City, on_delete=models.SET_NULL, null=True, blank=True)
    specialties = models.ManyToManyField('Doctor.Specialty', blank=True)

    def __str__(self):
        return self.title
    


   
    

class SpecialtiesofDoctorToomedicalcenters(models.Model):
    title = models.CharField(max_length=50)
    image = models.ImageField(upload_to='icons')
        
    def __str__(self):
        return self.title
   
    
class Centersfordiagnosisandtreatmentofsymptomsanddiseases (models.Model):
    title = models.CharField(max_length=50)
   
    def __str__(self):
       return self.title

class Thelatestmedicalcenters(models.Model):
    title = models.CharField(max_length=50)
    image = models.ImageField(upload_to='icons')

    def __str__(self):
        return self.title   
    
class TopClinics(models.Model):
    title = models.CharField(max_length=50)
    image = models.ImageField(upload_to='icons')
    location =models.CharField(max_length=50)
    rating =models.FloatField(default=5.0)

    def __str__(self):
        return self.title
    

class CitieswithDoctorToolaboratories(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name    


class Comment(models.Model):
    title = models.CharField(max_length=50)
    author =models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    text = models.TextField() 
    image =models.ImageField(upload_to='icons' , null=True , blank=True)
    date_time_created = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.text[:50]
    

class Symptomsanddiseasesofwomen(models.Model):
    title =models.CharField(max_length=50)


    def __str__(self):
        return self.title 
    


class Onlinemedical(models.Model):
    title = models.CharField(max_length=50)
    image = models.ImageField(upload_to='icons')
    specialties = models.ManyToManyField('Doctor.Specialty', related_name='core_online_specialties'  , blank=True)
    price = models.DecimalField(max_digits=10 , decimal_places=5 , blank=True , null=True)

    def __str__(self):
        return self.title