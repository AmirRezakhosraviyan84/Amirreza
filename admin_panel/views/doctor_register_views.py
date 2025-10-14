from django.shortcuts import render , redirect , get_object_or_404
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required, user_passes_test


from django.contrib import messages
from admin_panel.forms import doctor_register_forms
from accounts.models import Doctor_register

def is_superadmin(user):
    return user.is_authenticated and user.role =='superadmin'

def is_admin(user):
    return user.is_authenticated and user.role =='admin'

def is_staff(user):

    return user.is_authenticated and user.role =='staff'

def is_doctor(user):

    return user.is_authenticated and user.role =='doctor'


#doctor-register list
@login_required
@user_passes_test(is_staff)
def doctor_register_list(request):
    registers = Doctor_register.objects.all()
    return render(request, 'admin_panel/admin/registers/list.html', {'registers': registers})




#doctor-register add
@login_required
@user_passes_test(is_superadmin)
def doctor_register_add(request):
    form =doctor_register_forms (request.POST or None)
    if form.is_valid():
        form.save()
        messages.success(request, ' اضافه شد.')
        return redirect('register-list')
    return render(request, 'admin_panel/admin/registers/add_form.html', {'form': form, 'action':'add'})


# doctor-register edit
@login_required
@user_passes_test(is_superadmin)
def doctor_register_edit(request, pk):
    registers = get_object_or_404(Doctor_register, pk=pk)
    form = doctor_register_forms(request.POST or None, instance=registers)
    if form.is_valid():
        form.save()
        messages.success(request, 'تغییرات ذخیره شد.')
        return redirect('register-list')
    return render(request, 'admin_panel/admin/registers/edit_form.html', {'form': form, 'action':'edit'})




# doctor_register delete
@login_required
@user_passes_test(is_superadmin)
def doctor_register_delete(request, pk):
    registers = get_object_or_404(Doctor_register, pk=pk)
    if request.method == 'POST':
        registers.delete()
        messages.success(request, ' حذف شد.')
        return redirect('register-list')
    return render(request, 'admin_panel/admin/registers/confirm_delete.html', {'object':'registers' })
