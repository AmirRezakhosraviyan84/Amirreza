from django.shortcuts import render , redirect , get_object_or_404
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib import messages
from admin_panel.forms import ServiceForm
from Doctor.models import Service
def is_superadmin(user):
    return user.is_authenticated and user.role =='superadmin'

def is_admin(user):
    return user.is_authenticated and user.role =='admin'

def is_staff(user):

    return user.is_authenticated and user.role =='staff'

def is_doctor(user):

    return user.is_authenticated and user.role =='doctor'

#سرویس لیست
@login_required

def service_list(request):
    services = Service.objects.all()
    return render(request, 'admin_panel/admin/service/list.html', {'services': services})

#افزودن سرویس
@login_required
@user_passes_test(is_superadmin)
def service_add(request):
    form = ServiceForm(request.POST or None)
    if form.is_valid():
        form.save()
        messages.success(request, 'سرویس اضافه شد.')
        return redirect('service-list')
    return render(request, 'admin_panel/admin/service/add_form.html', {'form': form, 'action':'add'})


# ویرایش سرویس
@login_required
@user_passes_test(is_superadmin)
def service_edit(request, pk):
    service = get_object_or_404(Service, pk=pk)
    form = ServiceForm(request.POST or None, instance=service)
    if form.is_valid():
        form.save()
        messages.success(request, 'تغییرات ذخیره شد.')
        return redirect('service-list')
    return render(request, 'admin_panel/admin/service/edit_form.html', {'form': form, 'action':'edit'})


# حذف سرویس
@login_required
@user_passes_test(is_superadmin)
def service_delete(request, pk):
    service = get_object_or_404(Service, pk=pk)
    if request.method == 'POST':
        service.delete()
        messages.success(request, ' حذف شد.')
        return redirect('service-list')
    return render(request, 'admin_panel/admin/service/confirm_delete.html', {'object':'service' })