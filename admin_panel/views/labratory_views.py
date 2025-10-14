from django.shortcuts import render , redirect , get_object_or_404
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib import messages
from admin_panel.forms import labratory_forms
from Doctor.models import labratory

def is_superadmin(user):
    return user.is_authenticated and user.role =='superadmin'

def is_admin(user):
    return user.is_authenticated and user.role =='admin'

def is_staff(user):

    return user.is_authenticated and user.role =='staff'

def is_doctor(user):

    return user.is_authenticated and user.role =='doctor'

#lab list
@login_required

def lab_list(request):
    lab = labratory.objects.all()
    return render(request, 'admin_panel/admin/lab/list.html', {'lab': lab})


#lab add
@login_required
@user_passes_test(is_superadmin)
def lab_add(request):
    form =labratory_forms (request.POST or None)
    if form.is_valid():
        form.save()
        messages.success(request, 'آزمایشگاه اضافه شد.')
        return redirect('lab-list')
    return render(request, 'admin_panel/admin/lab/form.html', {'form': form, 'action':'add'})


#lab edit
@login_required
@user_passes_test(is_superadmin)
def lab_edit(request, pk):
    lab = get_object_or_404(labratory, pk=pk)
    form = labratory_forms(request.POST or None, instance=lab)
    if form.is_valid():
        form.save()
        messages.success(request, 'تغییرات ذخیره شد.')
        return redirect('lab-list')
    return render(request, 'admin_panel/admin/lab/form.html', {'form': form, 'action':'edit'})


#delete lab
@login_required
@user_passes_test(is_superadmin)
def lab_delete(request, pk):
    lab = get_object_or_404(labratory, pk=pk)
    if request.method == 'POST':
        lab.delete()
        messages.success(request, 'آزمایشگاه حذف شد.')
        return redirect('lab-list')
    return render(request, 'admin_panel/admin/lab/confirm_delete.html', {'object':'lab' })