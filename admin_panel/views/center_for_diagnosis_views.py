from django.shortcuts import render , redirect , get_object_or_404
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required, user_passes_test


from django.contrib import messages
from admin_panel.forms import Centers_for_diagnosis_and_treatment_of_symptoms_and_diseases_form
from core.models import Centersfordiagnosisandtreatmentofsymptomsanddiseases

def is_superadmin(user):
    return user.is_authenticated and user.role =='superadmin'

def is_admin(user):
    return user.is_authenticated and user.role =='admin'

def is_staff(user):

    return user.is_authenticated and user.role =='staff'

def is_doctor(user):

    return user.is_authenticated and user.role =='doctor'



def centers_for_diagnosis_and_treatment_list(request):
    items = Centersfordiagnosisandtreatmentofsymptomsanddiseases.objects.all()
    return render(request, 'admin_panel/admin/center/list.html', {'items': items})

def centers_for_diagnosis_and_treatment_add(request):
    form = Centers_for_diagnosis_and_treatment_of_symptoms_and_diseases_form(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('center_list')
    return render(request, 'admin_panel/admin/center/add_form.html', {'form': form})

def centers_for_diagnosis_and_treatment_edit(request, pk):
    obj = get_object_or_404(Centersfordiagnosisandtreatmentofsymptomsanddiseases, pk=pk)
    form = Centers_for_diagnosis_and_treatment_of_symptoms_and_diseases_form(request.POST or None, instance=obj)
    if form.is_valid():
        form.save()
        return redirect('center_list')
    return render(request, 'admin_panel/admin/center/edit_form.html', {'form': form})

def centers_for_diagnosis_and_treatment_delete(request, pk):
    obj = get_object_or_404(Centersfordiagnosisandtreatmentofsymptomsanddiseases, pk=pk)
    obj.delete()
    return redirect('center_list')