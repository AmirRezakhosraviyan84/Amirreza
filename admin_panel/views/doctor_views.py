from django.shortcuts import render , redirect , get_object_or_404
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required, user_passes_test


from django.contrib import messages
from admin_panel.forms import doctor_form
from Doctor.models import Doctor


def is_superadmin(user):
    return user.is_authenticated and user.role =='superadmin'

def is_admin(user):
    return user.is_authenticated and user.role =='admin'

def is_staff(user):

    return user.is_authenticated and user.role =='staff'

def is_doctor(user):

    return user.is_authenticated and user.role =='doctor'


@login_required
def doctor_list(request):
    doctors =Doctor.objects.all()
    return render(request, 'admin_panel/admin/doctor/list.html',{'doctors':doctors})

@login_required
@user_passes_test(is_superadmin)
def doctor_add(request):
    form = doctor_form(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
        messages.success(request, 'پزشک اضافه شد.')
        return redirect('doctor-list')
    return render(request, 'admin_panel/admin/doctor/add_form.html', {'form': form, 'action':'add'})


@login_required
@user_passes_test(is_superadmin)
def doctor_edit(request, pk):
    doctor = get_object_or_404(Doctor, pk=pk)
    form = doctor_form(request.POST or None, request.FILES or None, instance=doctor)
    if form.is_valid():
        form.save()
        messages.success(request, 'تغییرات ذخیره شد.')
        return redirect('doctor-list')
    return render(request, 'admin_panel/admin/doctor/edit_form.html', {'form': form, 'action':'edit'})



@login_required
@user_passes_test(is_superadmin)

def doctor_delete(request, pk):
    doctor = get_object_or_404(Doctor, pk=pk)
    if request.method == 'POST':
        doctor.delete()
        messages.success(request, 'پزشک حذف شد.')
        return redirect('doctor-list')
    return render(request, 'admin_panel/admin/doctor/confirm_delete.html', {'object': doctor})