from django.shortcuts import render , redirect , get_object_or_404
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required, user_passes_test

from django.contrib import messages
from admin_panel.forms import Onlinemedical_forms
from core.models import Onlinemedical
def is_superadmin(user):
    return user.is_authenticated and user.role =='superadmin'

def is_admin(user):
    return user.is_authenticated and user.role =='admin'

def is_staff(user):

    return user.is_authenticated and user.role =='staff'

def is_doctor(user):

    return user.is_authenticated and user.role =='doctor'


def online_medical_list(request):
    items = Onlinemedical.objects.all()
    return render(request, 'admin_panel/admin/online_medical/list.html', {'items': items})

def online_medical_add(request):
    form = Onlinemedical_forms(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('online-medical-list')
    return render(request, 'admin_panel/admin/online_medical/add_form.html', {'form': form})

def online_medical_edit(request, pk):
    obj = get_object_or_404(Onlinemedical, pk=pk)
    form = Onlinemedical_forms(request.POST or None, instance=obj)
    if form.is_valid():
        form.save()
        return redirect('online-medical-list')
    return render(request, 'admin_panel/admin/online_medical/edit_form.html', {'form': form})

def online_medical_delete(request, pk):
    obj = get_object_or_404(Onlinemedical, pk=pk)
    obj.delete()
    return redirect('online-medical-list')