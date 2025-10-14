from django.shortcuts import render , redirect , get_object_or_404
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required, user_passes_test


from django.contrib import messages
from admin_panel.forms import CitieswithDoctorToolaboratories_form
from core.models import CitieswithDoctorToolaboratories

def is_superadmin(user):
    return user.is_authenticated and user.role =='superadmin'

def is_admin(user):
    return user.is_authenticated and user.role =='admin'

def is_staff(user):

    return user.is_authenticated and user.role =='staff'

def is_doctor(user):

    return user.is_authenticated and user.role =='doctor'



def cities_with_doctor_to_labs_list(request):
    items = CitieswithDoctorToolaboratories.objects.all()
    return render(request, 'admin_panel/admin/city_lab/list.html', {'items': items})

def cities_with_doctor_to_labs_add(request):
    form = CitieswithDoctorToolaboratories_form(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('city-lab-list')
    return render(request, 'admin_panel/admin/city_lab/add_form.html', {'form': form})

def cities_with_doctor_to_labs_edit(request, pk):
    obj = get_object_or_404(CitieswithDoctorToolaboratories, pk=pk)
    form = CitieswithDoctorToolaboratories_form(request.POST or None, instance=obj)
    if form.is_valid():
        form.save()
        return redirect('city-lab-list')
    return render(request, 'admin_panel/admin/city_lab/edit_form.html', {'form': form})

def cities_with_doctor_to_labs_delete(request, pk):
    obj = get_object_or_404(CitieswithDoctorToolaboratories, pk=pk)
    obj.delete()
    return redirect('city-lab-list')