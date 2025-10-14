from django.shortcuts import render , redirect , get_object_or_404
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required, user_passes_test


from django.contrib import messages
from admin_panel.forms import Paraclinicservices_form
from Doctor.models import  Paraclinicservices

# Create your views here.
def is_superadmin(user):
    return user.is_authenticated and user.role =='superadmin'

def is_admin(user):
    return user.is_authenticated and user.role =='admin'

def is_staff(user):

    return user.is_authenticated and user.role =='staff'

def is_doctor(user):

    return user.is_authenticated and user.role =='doctor'


#paraclinic list
@login_required

def paraclinic_list(request):
    paraclinics = Paraclinicservices.objects.all()
    return render(request, 'admin_panel/admin/paraclinic/list.html', {'paraclinics': paraclinics})


#paraclinic add
@login_required
@user_passes_test(is_superadmin)
def paraclinic_add(request):
    form =Paraclinicservices_form (request.POST or None)
    if form.is_valid():
        form.save()
        messages.success(request, 'پارا کلینیک اضافه شد.')
        return redirect('paracclinic-list')
    return render(request, 'admin_panel/admin/paraclinic/add_form.html', {'form': form, 'action':'add'})

#edit paraclinic
@login_required
@user_passes_test(is_superadmin)
def paraclinic_edit(request, pk):
    paraclinics = get_object_or_404(Paraclinicservices, pk=pk)
    form = Paraclinicservices_form(request.POST or None, instance=paraclinics)
    if form.is_valid():
        form.save()
        messages.success(request, 'تغییرات ذخیره شد.')
        return redirect('paraclinic_list')
    return render(request, 'admin_panel/admin/paraclinic/edit_form.html', {'form': form, 'action':'edit'})

#delete paraclinic
@login_required
@user_passes_test(is_superadmin)
def paraclinic_delete(request, pk):
    paraclinics = get_object_or_404(Paraclinicservices, pk=pk)
    if request.method == 'POST':
        paraclinics.delete()
        messages.success(request, ' حذف شد.')
        return redirect('paraclinics-list')
    return render(request, 'admin_panel/admin/paraclinic/confirm_delete.html', {'object':'paraclinics' })