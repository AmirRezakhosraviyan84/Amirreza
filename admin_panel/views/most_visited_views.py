from django.shortcuts import render , redirect , get_object_or_404
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required, user_passes_test

from django.contrib import messages
from admin_panel.forms import Mostvisitedspecializations_form
from core.models import Mostvisitedspecializations
def is_superadmin(user):
    return user.is_authenticated and user.role =='superadmin'

def is_admin(user):
    return user.is_authenticated and user.role =='admin'

def is_staff(user):

    return user.is_authenticated and user.role =='staff'

def is_doctor(user):

    return user.is_authenticated and user.role =='doctor'




def most_visited_specializations_list(request):
    items = Mostvisitedspecializations.objects.all()
    return render(request, 'admin_panel/admin/most_visited/list.html', {'items': items})

def most_visited_specializations_add(request):
    form = Mostvisitedspecializations_form(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('ost-visited-list')
    return render(request, 'admin_panel/admin/most_visited/add_form.html', {'form': form})

def most_visited_specializations_edit(request, pk):
    obj = get_object_or_404(Mostvisitedspecializations, pk=pk)
    form = Mostvisitedspecializations_form(request.POST or None, instance=obj)
    if form.is_valid():
        form.save()
        return redirect('most-visited-list')
    return render(request, 'admin_panel/admin/most_visited/edit_form.html', {'form': form})

def most_visited_specializations_delete(request, pk):
    obj = get_object_or_404(Mostvisitedspecializations, pk=pk)
    obj.delete()
    return redirect('ost-visited-list')