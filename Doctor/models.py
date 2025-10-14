from django.db import models
from django.db.models import Avg
from django_jalali.db import models as jmodels  
from django.utils import timezone
from django.conf import settings
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from core.models import  TopClinics ,Symptoms_and_disease
from django.core.validators import MinValueValidator, MaxValueValidator
# Create your models here.

User = get_user_model()
class Specialty(models.Model):
    name = models.CharField(max_length=50)
     
    def __str__(self):
        return self.name
    
class City(models.Model):
    name = models.CharField(max_length=50)    

    def __str__(self):
        return self.name

class Service(models.Model):
    name = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=12, decimal_places=3 , blank=True , null=True ,default=100000000)
    city  =models.ForeignKey(City , on_delete=models.SET_NULL , blank=True , null=True)
    image = models.ImageField(blank=True , null=True)

    def __str__(self):
        return self.name

 
 

class Insurance(models.Model):  
    name = models.CharField(max_length=100)    

    def __str__(self):
        return self.name
    

class clinic (models.Model):
    name = models.CharField(max_length=50)
    address = models.TextField(null=True , blank=True)
    doctors = models.ManyToManyField("Doctor", related_name="clinics" )

    def __str__(self):
        return self.name
    


class Paraclinicservices(models.Model):
    name =models.CharField(max_length=50)
    city =models.ForeignKey(City , on_delete=models.SET_NULL , null=True , blank=True)

    def __str__(self):
        return self.name
    
class pharmacy(models.Model):
    name =models.CharField(max_length=50)
    city =models.ForeignKey(City, on_delete= models.CASCADE , null=True)

    def __str__(self):
        return self.name




class Lab_specialty(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name
    


class labratory(models.Model):
    name = models.CharField(max_length=50)
    city = models.ForeignKey(City , on_delete=models.SET_NULL , null=True , blank=True)
    specialty =models.ManyToManyField(Lab_specialty , blank=True)
    insurance =models.ManyToManyField(Insurance  , blank=True )
    address =models.TextField(null=True , blank=True)
    image =models.ImageField( blank=True)

 
    def __str__(self):
        return self.name    



class Doctor(models.Model):
    name = models.CharField(max_length=100)
    specialty = models.ForeignKey(Specialty,  on_delete=models.SET_NULL , blank =True  , null=True)
    services = models.ManyToManyField(Service ,   blank=True )
    city = models.ForeignKey(City, on_delete=models.SET_NULL, null=True)
    insurances = models.ManyToManyField(Insurance ,  blank=True)
    medical_code =models.CharField(max_length=20 , null=True , blank= True)
    clinic = models.ForeignKey(TopClinics , on_delete= models.CASCADE , related_name='doctors' , null=True , blank=True)
    image = models.ImageField( blank=True, null=True,default='images/default.jpg')
    address = models.TextField()
    phone_number = models.CharField(max_length=14 , null=True , blank=True)
    symptoms = models.ManyToManyField(Symptoms_and_disease, blank=True)
    success_appointments =models.PositiveIntegerField(default=0)
    date_time_created =models.DateTimeField(auto_now_add=True , null=True , blank=True)
    
      # فیلد برای مشاوره فوری
    urgent_consultation = models.BooleanField(default=False)
    # فیلد برای پزشکان دارای نوبت باز
    has_available_slots = models.BooleanField(default=False)

    def __str__(self):
        return self.name
    
    def average_rating(self):
        ratings = self.reviews.all()
        if ratings.exists():
            return round(sum([r.overall for r in ratings]) / ratings.count(), 1)
        return 0 
   
    
    def total_reviews(self):
    
     return self.ratings.count()
    
    def recommend_percent(self):
        total = self.reviews.count()
        if total == 0:
            return 0
        recs = self.reviews.filter(recommend=True).count()
        return int((recs / total) * 100)
    

WAITING_CHOICES = [
    ("0-15", "۰-۱۵ دقیقه"),
    ("15-45", "۱۵-۴۵ دقیقه"),
    ("45-90", "۴۵-۹۰ دقیقه"),
    ("90+", "بیش از ۹۰ دقیقه"),
]

REASON_CHOICES = [
    ("checkup", "ویزیت چکاپ عمومی"),
    ("followup", "ویزیت پیگیری"),
    ("treatment", "درمان خاص"),
    ("other", "سایر موارد"),
]



class Review(models.Model):
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE, related_name='reviews')
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)

    # امتیازها با محدودیت 0 تا 5
    overall = models.PositiveSmallIntegerField(
        default=0, 
        validators=[MinValueValidator(0), MaxValueValidator(5)]
    )
    recommend = models.BooleanField(default=True)

    behavior = models.PositiveSmallIntegerField(
        default=0,
        validators=[MinValueValidator(0), MaxValueValidator(5)]
    )
    explain = models.PositiveSmallIntegerField(
        default=0,
        validators=[MinValueValidator(0), MaxValueValidator(5)]
    )
    skill = models.PositiveSmallIntegerField(
        default=0,
        validators=[MinValueValidator(0), MaxValueValidator(5)]
    )
    reception = models.PositiveSmallIntegerField(
        default=0,
        validators=[MinValueValidator(0), MaxValueValidator(5)]
    )
    environment = models.PositiveSmallIntegerField(
        default=0,
        validators=[MinValueValidator(0), MaxValueValidator(5)]
    )

    wait_time = models.CharField(max_length=20, choices=WAITING_CHOICES, blank=True, null=True)
    reason = models.CharField(max_length=20, choices=REASON_CHOICES, blank=True, null=True)

    comment = models.TextField(blank=True, null=True)
    anonymous = models.BooleanField(default=False)

    created_at = models.DateTimeField(auto_now_add=True)


    def clean(self):
        # محدود کردن امتیازها به 0 تا 5
        for field in ['overall', 'behavior', 'explain', 'skill', 'reception', 'environment']:
            value = getattr(self, field)
            if value > 5:
                setattr(self, field, 5)
            elif value < 0:
                setattr(self, field, 0)

    def save(self, *args, **kwargs):
        self.clean()  # قبل از ذخیره مطمئن می‌شیم همه مقادیر معتبر هستند
        super().save(*args, **kwargs)

    def __str__(self):
        return f"Review for {self.doctor} ({self.overall})"

   



    
    


class DoctorRating(models.Model):
    doctor = models.ForeignKey(Doctor , on_delete=models.CASCADE , related_name='ratings', null= True , blank=True)
    user =models.ForeignKey(User , on_delete=models.CASCADE, null= True , blank=True)
    score =models.PositiveSmallIntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(5)], null= True , blank=True) #1>=score<=5

    class Meta:
        unique_together =('doctor','user')  #هر یوزر یک رای برای هر دکتر
    
    def __str__(self):
        return f"{self.doctor.name}"


class Onlinemedicalconsultation(models.Model):
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE , related_name='online_consultations',null=True, blank=True)
    specialty = models.ForeignKey(Specialty, on_delete=models.SET_NULL, null=True)



class khadamat(models.Model):
    name =models.CharField(max_length=50)
    image = models.ImageField(blank=True , null=True)
    zir_goroh =models.ManyToManyField(Service , blank=True) 
    

    def __str__(self):
        return self.name

class Pishnahad(models.Model):
    khadamat = models.ForeignKey(khadamat, on_delete=models.CASCADE, related_name="pishnahad_ha")
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE, related_name="pishnahad_ha")
    title = models.CharField(max_length=100)          # نام پکیج
    description = models.TextField(blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2) 

    def __str__(self):
        return self.title

class PishnahadImage(models.Model):
    pishnahad = models.ForeignKey(Pishnahad, on_delete=models.CASCADE, related_name="images")
    image = models.ImageField(upload_to="pishnahad/")

    def __str__(self):
        return self.pishnahad.title 
    
#کلاس نوبت دهی
class Appointment(models.Model):
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    date = models.DateField()
    time = models.TimeField()
    is_booked = models.BooleanField(default=False)
    booked_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)

    class Meta:
        unique_together = ('doctor', 'date', 'time')  # جلوگیری از نوبت تکراری

    def __str__(self):
        return f"{self.doctor.name} - {self.date} {self.time}"
    

class Phone_Appointment(models.Model):
    doctor = models.ForeignKey(Doctor , on_delete=models.CASCADE)
    date   =   models.DateField()
    time   = models.TimeField()
    durstion =models.IntegerField(help_text='مدت زمان تماس  (دقیقه)')   
    price =models.IntegerField()
    is_reserved = models.BooleanField(default=False) 
    created_at =models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"مشاوره تلفنی {self.doctor} - {self.date} {self.time}"
    

class Text_Appointment(models.Model):
    doctor =models.ForeignKey(Doctor  , on_delete=models.CASCADE)
    date =models.DateField()
    time =models.TimeField()
    price =models.IntegerField()
    is_reserved =models.BooleanField(default=False)
    created_at =models.DateTimeField(auto_now_add=True)

    def __str__(self):
        
     return f"مشاوره متنی {self.doctor} - {self.date}"    



class PatientInfo(models.Model):
    first_name = models.CharField(max_length=50,  null=True, blank=True)
    last_name = models.CharField(max_length=50,  null=True, blank=True )
    national_code = models.CharField(max_length=10,  null=True, blank=True )
    gender = models.CharField(max_length=10,  null=True, blank=True)
    birth_year = models.IntegerField( null=True, blank=True)
    city = models.CharField(max_length=50,  null=True, blank=True)
    appointment = models.ForeignKey(Appointment, on_delete=models.CASCADE ,  null=True, blank=True)



class FAQ(models.Model):
    question=models.CharField(max_length=500)
    answer =models.TextField()
    order =models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.question


class Order(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    order_number = models.CharField(max_length=50)
    date = models.DateField()
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=50, default="در حال پردازش")  # یا هر استاتوس دیگری

    def __str__(self):
        return f"{self.order_number} - {self.user}"