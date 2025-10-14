from django.shortcuts import render , redirect , get_object_or_404
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required, user_passes_test


from django.contrib import messages
from admin_panel.forms import TopClinics_form
from core.models import TopClinics

def is_superadmin(user):
    return user.is_authenticated and user.role =='superadmin'

def is_admin(user):
    return user.is_authenticated and user.role =='admin'

def is_staff(user):

    return user.is_authenticated and user.role =='staff'

def is_doctor(user):

    return user.is_authenticated and user.role =='doctor'




def top_clinics_list(request):
    items = TopClinics.objects.all()
    return render(request, 'admin_panel/admin/top_clinics/list.html', {'items': items})

def top_clinics_add(request):
    form = TopClinics_form(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('top-clinics-list')
    return render(request, 'admin_panel/admin/top_clinics/add_form.html', {'form': form})

def top_clinics_edit(request, pk):
    obj = get_object_or_404(TopClinics, pk=pk)
    form = TopClinics_form(request.POST or None, instance=obj)
    if form.is_valid():
        form.save()
        return redirect('top-clinics-list')
    return render(request, 'admin_panel/admin/top_clinics/edit_form.html', {'form': form})

def top_clinics_delete(request, pk):
    obj = get_object_or_404(TopClinics, pk=pk)
    obj.delete()
    return redirect('top-clinics-list')
