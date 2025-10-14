from django.db import models
from django.contrib.auth.models import AbstractBaseUser,PermissionsMixin,BaseUserManager
from django.contrib.auth import get_user_model
from phonenumber_field.modelfields import PhoneNumberField
from django.utils import timezone
from django.conf import settings


# Create your models here.




class CustomUserManager(BaseUserManager):
    use_in_migrations = True

    def create_user(self, phone_number, password=None, **extra_fields):
        if not phone_number:
            raise ValueError('شماره موبایل باید وارد شود')
        user = self.model(phone_number=phone_number, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, phone_number, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        if not extra_fields.get('is_staff'):
            raise ValueError('Superuser باید is_staff=True باشد')
        if not extra_fields.get('is_superuser'):
            raise ValueError('Superuser باید is_superuser=True باشد')
        return self.create_user(phone_number, password, **extra_fields)

    def get_by_natural_key(self, phone_number):
        return self.get(phone_number=phone_number)




class CustomUser(AbstractBaseUser, PermissionsMixin):
  
    GENDER_CHOICES =[
        ('male','آقا'),('famale','خانم')
    ]

    ROLE_CHOICES =[
        ('superadmin','مدیرکل'),
        ('admin','مدیر'),
        ('staff','کارمند'),
        ('doctor','دکتر'),
    ]

 #اطلاعات شخصی


    first_name=models.CharField(max_length=50, blank=True, null=True, verbose_name="نام")
    last_name =models.CharField(max_length=50, blank=True, null=True, verbose_name="نام خانوادگی")
    national_code =models.CharField(max_length=10, blank=True, null=True, verbose_name="کد ملی")
    birth_year = models.PositiveIntegerField(blank=True, null=True, verbose_name="سال تولد")
    is_foreign = models.BooleanField(default=False, verbose_name="اتباع خارجی")
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES, blank=True, null=True, verbose_name="جنسیت")
    city = models.ForeignKey('Doctor.City', on_delete=models.SET_NULL, null=True, blank=True, verbose_name="شهر")
    email = models.EmailField(blank=True, null=True, verbose_name="ایمیل")



    phone_number = models.CharField(max_length=20, unique=True)
    full_name = models.CharField(max_length=100, blank=True  , null= True) 
    role =models.CharField(max_length=20 , choices=ROLE_CHOICES ,default='doctor' )
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_doctor =models.BooleanField(default=False)
    is_patient =models.BooleanField(default=False)


    date_joined = models.DateTimeField(auto_now_add=True)

    objects = CustomUserManager()  # حتما اینجا Manager رو اختصاص بده

    USERNAME_FIELD = 'phone_number'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.phone_number

class Specialty(models.Model):
        title = models.CharField("عنوان تخصص", max_length=100)

        def __str__(self):
          return self.title

class Doctor_register(models.Model):
    MEDICAL_CODE_MAX_LENGTH = 20
    
    GENDER_CHOICES =[
        ('male','مرد'),
        ('famale','زن'),
        ('other','غیره'),
    ]

    mediacal_code = models.CharField("کد نظام پزشکی", max_length=MEDICAL_CODE_MAX_LENGTH)
    first_name = models.CharField('نام',max_length=50)
    last_name = models.CharField('نام خانوادگی', max_length=50)
    full_name_en = models.CharField('نام کامل به انگلیسی',max_length=60)
    national_id = models.CharField('کدملی', max_length=10)
    email_address =models.EmailField('ایمیل')
    gender = models.CharField('جنسیت', max_length=10 , choices=GENDER_CHOICES)
    specialties = models.ManyToManyField('Specialty', verbose_name="تخصص")


    def __str__(self):
        return f"{self.first_name}:{self.last_name}"
    


User = get_user_model()

#otp for user


class UserOTP(models.Model):
        user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
        code = models.CharField(default='123456')
        phone_number = models.CharField(max_length=14)  # به جای PhoneNumberField
        created_at = models.DateTimeField(auto_now_add=True)
        user_type =models.CharField(max_length=10,  null=True , blank=True , choices=(('user','User'), ('doctor','Doctor')))

        def is_expired(self):
            """بررسی می‌کند که OTP منقضی شده باشد یا نه (60 ثانیه)"""
            return (timezone.now() - self.created_at).total_seconds() > 60

        def __str__(self):
            return f"{self.phone_number} - {self.code}"



class Wallet(models.Model):
    user =models.ForeignKey(settings.AUTH_USER_MODEL , on_delete=models.CASCADE)
    balance =models.DecimalField(max_digits=10, decimal_places=2, default=0)

    def __str__(self):
        return " self.balance تومان"
    