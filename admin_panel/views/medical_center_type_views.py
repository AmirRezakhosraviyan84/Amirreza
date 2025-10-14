from django.shortcuts import render , redirect , get_object_or_404
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required, user_passes_test

from django.contrib import messages
from admin_panel.forms import MedicalCenterType_forms
from core.models import MedicalCenterType
def is_superadmin(user):
    return user.is_authenticated and user.role =='superadmin'

def is_admin(user):
    return user.is_authenticated and user.role =='admin'

def is_staff(user):

    return user.is_authenticated and user.role =='staff'

def is_doctor(user):

    return user.is_authenticated and user.role =='doctor'




def medical_center_type_list(request):
    types = MedicalCenterType.objects.all()
    return render(request, 'admin_panel/admin/medical_type/list.html', {'types': types})

def medical_center_type_add(request):
    form = MedicalCenterType_forms(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('medical-type-list')
    return render(request, 'admin_panel/admin/medical_type/add_form.html', {'form': form})

def medical_center_type_edit(request, pk):
    obj = get_object_or_404(MedicalCenterType, pk=pk)
    form = MedicalCenterType_forms(request.POST or None, instance=obj)
    if form.is_valid():
        form.save()
        return redirect('medical-type-list')
    return render(request, 'admin_panel/admin/medical_type/edit_form.html', {'form': form})

def medical_center_type_delete(request, pk):
    obj = get_object_or_404(MedicalCenterType, pk=pk)
    obj.delete()
    return redirect('medical-type-list')
