from django.shortcuts import render , redirect , get_object_or_404
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required, user_passes_test

from django.contrib import messages
from admin_panel.forms import Symptoms_and_disease_forms
from core.models import Symptoms_and_disease
def is_superadmin(user):
    return user.is_authenticated and user.role =='superadmin'

def is_admin(user):
    return user.is_authenticated and user.role =='admin'

def is_staff(user):

    return user.is_authenticated and user.role =='staff'

def is_doctor(user):

    return user.is_authenticated and user.role =='doctor'




def symptoms_and_disease_list(request):
    items = Symptoms_and_disease.objects.all()
    return render(request, 'admin_panel/admin/symptoms/list.html', {'items': items})

def symptoms_and_disease_add(request):
    form = Symptoms_and_disease_forms(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('symptoms-list')
    return render(request, 'admin_panel/admin/symptoms/add_form.html', {'form': form})

def symptoms_and_disease_edit(request, pk):
    obj = get_object_or_404(Symptoms_and_disease, pk=pk)
    form = Symptoms_and_disease_forms(request.POST or None, instance=obj)
    if form.is_valid():
        form.save()
        return redirect('symptoms-list')
    return render(request, 'admin_panel/admin/symptoms/edit_form.html', {'form': form})

def symptoms_and_disease_delete(request, pk):
    obj = get_object_or_404(Symptoms_and_disease, pk=pk)
    obj.delete()
    return redirect('symptoms-list')