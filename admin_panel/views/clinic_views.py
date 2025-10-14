from django.shortcuts import render , redirect , get_object_or_404
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required, user_passes_test


from django.contrib import messages
from admin_panel.forms import clinic_form
from Doctor.models import clinic

def is_superadmin(user):
    return user.is_authenticated and user.role =='superadmin'

def is_admin(user):
    return user.is_authenticated and user.role =='admin'

def is_staff(user):

    return user.is_authenticated and user.role =='staff'

def is_doctor(user):

    return user.is_authenticated and user.role =='doctor'

#clinic list
@login_required

def clinic_list(request):
    clinics = clinic.objects.all()
    return render(request, 'admin_panel/admin/clinic/list.html', {'clinics': clinics})

#add clinic
@login_required
@user_passes_test(is_superadmin)
def clinic_add(request):
    form =clinic_form (request.POST or None)
    if form.is_valid():
        form.save()
        messages.success(request, 'کلینیک اضافه شد.')
        return redirect('clinic-list')
    return render(request, 'admin_panel/admin/clinic/add_form.html', {'form': form, 'action':'add'})

#edit clinic
@login_required
@user_passes_test(is_superadmin)
def clinic_edit(request, pk):
    clinics = get_object_or_404(clinic, pk=pk)
    form = clinic_form(request.POST or None, instance=clinics)
    if form.is_valid():
        form.save()
        messages.success(request, 'تغییرات ذخیره شد.')
        return redirect('clinic-list')
    return render(request, 'admin_panel/admin/clinic/form.html', {'form': form, 'action':'edit'})


#delete clinic
@login_required
@user_passes_test(is_superadmin)
def clinic_delete(request, pk):
    clinics = get_object_or_404(clinic, pk=pk)
    if request.method == 'POST':
        clinics.delete()
        messages.success(request, 'کلینیک حذف شد.')
        return redirect('clinics-list')
    return render(request, 'admin_panel/admin/clinic/confirm_delete.html', {'object':'clinics' })