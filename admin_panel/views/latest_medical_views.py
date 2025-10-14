from django.shortcuts import render , redirect , get_object_or_404
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required, user_passes_test


from django.contrib import messages
from admin_panel.forms import The_latest_medical_centers_form
from core.models import Thelatestmedicalcenters

def is_superadmin(user):
    return user.is_authenticated and user.role =='superadmin'

def is_admin(user):
    return user.is_authenticated and user.role =='admin'

def is_staff(user):

    return user.is_authenticated and user.role =='staff'

def is_doctor(user):

    return user.is_authenticated and user.role =='doctor'




def latest_medical_centers_list(request):
    items = Thelatestmedicalcenters.objects.all()
    return render(request, 'admin_panel/admin/latest_medical/list.html', {'items': items})

def latest_medical_centers_add(request):
    form = The_latest_medical_centers_form(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('latest-medical-list')
    return render(request, 'admin_panel/admin/latest_medical/add_form.html', {'form': form})

def latest_medical_centers_edit(request, pk):
    obj = get_object_or_404(Thelatestmedicalcenters, pk=pk)
    form = The_latest_medical_centers_form(request.POST or None, instance=obj)
    if form.is_valid():
        form.save()
        return redirect('latest-medical-list')
    return render(request, 'admin_panel/admin/latest_medical/edit_form.html', {'form': form})

def latest_medical_centers_delete(request, pk):
    obj = get_object_or_404(Thelatestmedicalcenters, pk=pk)
    obj.delete()
    return redirect('latest-medical-list')