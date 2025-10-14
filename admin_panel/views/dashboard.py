from django.shortcuts import render , redirect , get_object_or_404
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse
from django.contrib.auth.decorators import login_required, user_passes_test


from django.contrib import messages
from ..forms import *
from ..models import *
# Create your views here.
def is_superadmin(user):
    return user.is_authenticated and user.role =='superadmin'

def is_admin(user):
    return user.is_authenticated and user.role =='admin'

def is_staff(user):

    return user.is_authenticated and user.role =='staff'

def is_doctor(user):

    return user.is_authenticated and user.role =='doctor'


@login_required
@user_passes_test(lambda u: u.role =='superadmin')
def dashboard(request):
      
    context ={
          'models': [
            {'name': 'پزشکان', 'count': Doctor.objects.count(), 'url':reverse('doctor-list')},
            {'name': 'تخصص‌ها', 'count': Specialty.objects.count(), 'url': reverse('specialty-list')},
            {'name': 'خدمات', 'count': Service.objects.count(), 'url': reverse('service-list')},
            {'name': 'بیمه‌ها', 'count': Insurance.objects.count(), 'url': reverse('insurance-list')},
            {'name': 'نوبت‌ها', 'count': Appointment.objects.count(), 'url': reverse('appointment-list')},
            {'name': 'کاربران', 'count': CustomUser.objects.count(), 'url':reverse('user-list')},
            {'name': 'پست‌ها', 'count': Post.objects.count(), 'url':reverse('post-list') },
            {'name': 'َشهرها', 'count': City.objects.count(), 'url': reverse('city-list')},
            {'name': 'کلینیک ها', 'count': clinic.objects.count(), 'url': reverse('clinic-list')},
            {'name': 'خدمات پاراکلینکی', 'count': Paraclinicservices.objects.count(), 'url': reverse('paraclinic-list')},
            {'name': 'داروخانه', 'count': pharmacy.objects.count(), 'url':reverse('pharmacy-list') },
            {'name': 'آزمایشگاه', 'count': labratory.objects.count(), 'url':reverse('lab-list') },
            {'name': 'تخصص های آزمایشگاه', 'count': Lab_specialty.objects.count(), 'url':reverse('labs-list')},
            



          ]
      }

    return render ( request ,'admin_panel/admin/index.html', context)