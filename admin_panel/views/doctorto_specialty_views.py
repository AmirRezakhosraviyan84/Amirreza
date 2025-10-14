from django.shortcuts import render , redirect , get_object_or_404
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required, user_passes_test


from django.contrib import messages
from admin_panel.forms import SpecialtiesofDoctorToomedicalcenters_form
from core.models import SpecialtiesofDoctorToomedicalcenters

def is_superadmin(user):
    return user.is_authenticated and user.role =='superadmin'

def is_admin(user):
    return user.is_authenticated and user.role =='admin'

def is_staff(user):

    return user.is_authenticated and user.role =='staff'

def is_doctor(user):

    return user.is_authenticated and user.role =='doctor'





def specialties_doctor_to_medical_centers_list(request):
    items = SpecialtiesofDoctorToomedicalcenters.objects.all()
    return render(request, 'admin_panel/admin/doctorto_specialty/list.html', {'items': items})

def specialties_doctor_to_medical_centers_add(request):
    form = SpecialtiesofDoctorToomedicalcenters_form(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('doctorto-specialty-list')
    return render(request, 'admin_panel/admin/doctorto_specailty/add_form.html', {'form': form})

def specialties_doctor_to_medical_centers_edit(request, pk):
    obj = get_object_or_404(SpecialtiesofDoctorToomedicalcenters, pk=pk)
    form = SpecialtiesofDoctorToomedicalcenters_form(request.POST or None, instance=obj)
    if form.is_valid():
        form.save()
        return redirect('doctorto-specialty-list')
    return render(request, 'admin_panel/admin/doctorto_specailty/edit_form.html', {'form': form})

def specialties_doctor_to_medical_centers_delete(request, pk):
    obj = get_object_or_404(SpecialtiesofDoctorToomedicalcenters, pk=pk)
    obj.delete()
    return redirect('doctorto-specialty-list')