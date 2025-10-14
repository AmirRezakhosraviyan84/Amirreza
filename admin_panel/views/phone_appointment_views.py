from django.shortcuts import render , redirect , get_object_or_404
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required, user_passes_test


from django.contrib import messages
from admin_panel.forms import Phone_Appointment_forms
from Doctor.models import Phone_Appointment

def is_superadmin(user):
    return user.is_authenticated and user.role =='superadmin'

def is_admin(user):
    return user.is_authenticated and user.role =='admin'

def is_staff(user):

    return user.is_authenticated and user.role =='staff'

def is_doctor(user):

    return user.is_authenticated and user.role =='doctor'



#phone list
@login_required
@user_passes_test(is_staff)
def phone_list(request):
    phons = Phone_Appointment.objects.all()
    return render(request, 'admin_panel/admin/phone/list.html', {'phons': phons})


#Phone add
@login_required
@user_passes_test(is_superadmin)
def phone_add(request):
    form =Phone_Appointment_forms (request.POST or None)
    if form.is_valid():
        form.save()
        messages.success(request, ' اضافه شد.')
        return redirect('phone-list')
    return render(request, 'admin_panel/admin/phone/add_form.html', {'form': form, 'action':'add'})


# phone edit
@login_required
@user_passes_test(is_superadmin)
def phone_edit(request, pk):
    phones = get_object_or_404(Phone_Appointment, pk=pk)
    form = Phone_Appointment_forms(request.POST or None, instance=phones)
    if form.is_valid():
        form.save()
        messages.success(request, 'تغییرات ذخیره شد.')
        return redirect('phone-list')
    return render(request, 'admin_panel/admin/phone/edit_form.html', {'form': form, 'action':'edit'})




# phone delete
@login_required
@user_passes_test(is_superadmin)
def phone_delete(request, pk):
    phones = get_object_or_404(Phone_Appointment, pk=pk)
    if request.method == 'POST':
        phones.delete()
        messages.success(request, ' حذف شد.')
        return redirect('phone_list')
    return render(request, 'admin_panel/admin/phone/confirm_delete.html', {'object':'phones' })