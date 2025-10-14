from django.shortcuts import render , redirect , get_object_or_404
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required, user_passes_test


from django.contrib import messages
from admin_panel.forms import AppointmentForm
from Doctor.models import Appointment

def is_superadmin(user):
    return user.is_authenticated and user.role =='superadmin'

def is_admin(user):
    return user.is_authenticated and user.role =='admin'

def is_staff(user):

    return user.is_authenticated and user.role =='staff'

def is_doctor(user):

    return user.is_authenticated and user.role =='doctor'


#نوبت لیست
@login_required

def appointment_list(request):
    appointments = Appointment.objects.all()
    return render(request, 'admin_panel/admin/appointment/list.html', {'appointments': appointments})


#ساخت نوبت
@login_required
@user_passes_test(is_superadmin)
def appointment_add(request):
    form =AppointmentForm (request.POST or None)
    if form.is_valid():
        form.save()
        messages.success(request, 'بیمه اضافه شد.')
        return redirect('appointment-list')
    return render(request, 'admin_panel/admin/appointment/add_form.html', {'form': form, 'action':'add'})



# ویرایش نوبت
@login_required
@user_passes_test(is_superadmin)
def appointment_edit(request, pk):
    appointment = get_object_or_404(Appointment, pk=pk)
    form = AppointmentForm(request.POST or None, instance=appointment)
    if form.is_valid():
        form.save()
        messages.success(request, 'تغییرات ذخیره شد.')
        return redirect('appointment-list')
    return render(request, 'admin_panel/admin/appointment/form.html', {'form': form, 'action':'edit'})


# حذف نوبت
@login_required
@user_passes_test(is_superadmin)
def appointment_delete(request, pk):
    appointment = get_object_or_404(Appointment, pk=pk)
    if request.method == 'POST':
        appointment.delete()
        messages.success(request, 'تخصص حذف شد.')
        return redirect('appointment-list')
    return render(request, 'admin_panel/admin/appointment/confirm_delete.html', {'object':'appointment' })