from django.shortcuts import render , redirect , get_object_or_404
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required, user_passes_test


from django.contrib import messages
from admin_panel.forms import Symptomsanddiseasesofwomen_form
from core.models import Symptomsanddiseasesofwomen

def is_superadmin(user):
    return user.is_authenticated and user.role =='superadmin'

def is_admin(user):
    return user.is_authenticated and user.role =='admin'

def is_staff(user):

    return user.is_authenticated and user.role =='staff'

def is_doctor(user):

    return user.is_authenticated and user.role =='doctor'



def symptoms_and_diseases_of_women_list(request):
    items = Symptomsanddiseasesofwomen.objects.all()
    return render(request, 'admin_panel/admin/symptoms_women/list.html', {'items': items})

def symptoms_and_diseases_of_women_add(request):
    form = Symptomsanddiseasesofwomen_form(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('symptoms-women-list')
    return render(request, 'admin_panel/admin/symptoms_women/add_form.html', {'form': form})

def symptoms_and_diseases_of_women_edit(request, pk):
    obj = get_object_or_404(Symptomsanddiseasesofwomen, pk=pk)
    form = Symptomsanddiseasesofwomen_form(request.POST or None, instance=obj)
    if form.is_valid():
        form.save()
        return redirect('symptoms-women-list')
    return render(request, 'admin_panel/admin/symptoms_women/edit_form.html', {'form': form})

def symptoms_and_diseases_of_women_delete(request, pk):
    obj = get_object_or_404(Symptomsanddiseasesofwomen, pk=pk)
    obj.delete()
    return redirect('symptoms-women-list')