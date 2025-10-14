from django.shortcuts import render , redirect , get_object_or_404
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required, user_passes_test

from django.contrib import messages
from admin_panel.forms import userotp_forms
from accounts.models import UserOTP
def is_superadmin(user):
    return user.is_authenticated and user.role =='superadmin'

def is_admin(user):
    return user.is_authenticated and user.role =='admin'

def is_staff(user):

    return user.is_authenticated and user.role =='staff'

def is_doctor(user):

    return user.is_authenticated and user.role =='doctor'


#userotp list
@login_required
@user_passes_test(is_staff)
def userotp_list(request):
    userotps = UserOTP.objects.all()
    return render(request, 'admin_panel/admin/userotp/list.html', {'userotps': userotps})




#userotp add
@login_required
@user_passes_test(is_superadmin)
def userotp_add(request):
    form =userotp_forms (request.POST or None)
    if form.is_valid():
        form.save()
        messages.success(request, ' اضافه شد.')
        return redirect('userotp-list')
    return render(request, 'admin_panel/admin/userotp/add_form.html', {'form': form, 'action':'add'})


# userotp edit
@login_required
@user_passes_test(is_superadmin)
def userotp_edit(request, pk):
    userotps = get_object_or_404(UserOTP, pk=pk)
    form = userotp_forms(request.POST or None, instance=userotps)
    if form.is_valid():
        form.save()
        messages.success(request, 'تغییرات ذخیره شد.')
        return redirect('userotp-list')
    return render(request, 'admin_panel/admin/userotp/edit_form.html', {'form': form, 'action':'edit'})




# userotp delete
@login_required
@user_passes_test(is_superadmin)
def userotp_delete(request, pk):
    userotps = get_object_or_404(UserOTP, pk=pk)
    if request.method == 'POST':
        userotps.delete()
        messages.success(request, ' حذف شد.')
        return redirect('userotp-list')
    return render(request, 'admin_panel/admin/userotp/confirm_delete.html', {'object':'userotps' })