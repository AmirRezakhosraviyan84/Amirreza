from django.shortcuts import render , redirect , get_object_or_404
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required, user_passes_test

from django.contrib import messages
from admin_panel.forms import SpecialtyForm
from Doctor.models import Specialty
def is_superadmin(user):
    return user.is_authenticated and user.role =='superadmin'

def is_admin(user):
    return user.is_authenticated and user.role =='admin'

def is_staff(user):

    return user.is_authenticated and user.role =='staff'

def is_doctor(user):

    return user.is_authenticated and user.role =='doctor'

# لیست تخصص‌ها
@login_required

def specialty_list(request):
    specialties = Specialty.objects.all()
    return render(request, 'admin_panel/admin/specialty/list.html', {'specialties': specialties})

# افزودن تخصص
@login_required
@user_passes_test(is_superadmin)
def specialty_add(request):
    form = SpecialtyForm(request.POST or None)
    if form.is_valid():
        form.save()
        messages.success(request, 'تخصص اضافه شد.')
        return redirect('specialty-list')
    return render(request, 'admin_panel/admin/specialty/add_form.html', {'form': form, 'action':'add'})

# ویرایش تخصص
@login_required
@user_passes_test(is_superadmin)
def specialty_edit(request, pk):
    specialty = get_object_or_404(Specialty, pk=pk)
    form = SpecialtyForm(request.POST or None, instance=specialty)
    if form.is_valid():
        form.save()
        messages.success(request, 'تغییرات ذخیره شد.')
        return redirect('specialty-list')
    return render(request, 'admin_panel/admin/specialty/edit_form.html', {'form': form, 'action':'edit'})

# حذف تخصص
@login_required
@user_passes_test(is_superadmin)
def specialty_delete(request, pk):
    specialty = get_object_or_404(Specialty, pk=pk)
    if request.method == 'POST':
        specialty.delete()
        messages.success(request, 'تخصص حذف شد.')
        return redirect('specialty-list')
    return render(request, 'admin_panel/admin/specialty/confirm_delete.html', {'object': specialty})