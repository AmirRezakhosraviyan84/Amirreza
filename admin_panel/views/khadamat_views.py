from django.shortcuts import render , redirect , get_object_or_404
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib import messages
from admin_panel.forms import khadamat_forms
from Doctor.models import khadamat
def is_superadmin(user):
    return user.is_authenticated and user.role =='superadmin'

def is_admin(user):
    return user.is_authenticated and user.role =='admin'

def is_staff(user):

    return user.is_authenticated and user.role =='staff'

def is_doctor(user):

    return user.is_authenticated and user.role =='doctor'


#khadamat list
@login_required
@user_passes_test(is_staff)
def khadamat_list(request):
    khadamats = khadamat.objects.all()
    return render(request, 'admin_panel/admin/khadamat/list.html', {'khadamats': khadamats})


#khadamat add
@login_required
@user_passes_test(is_superadmin)
def khadamat_add(request):
    form =khadamat_forms (request.POST or None)
    if form.is_valid():
        form.save()
        messages.success(request, ' اضافه شد.')
        return redirect('khadamat-list')
    return render(request, 'admin_panel/admin/khadamat/add_form.html', {'form': form, 'action':'add'})



# khadamat edit
@login_required
@user_passes_test(is_superadmin)
def khadamat_edit(request, pk):
    khadamats = get_object_or_404(khadamat, pk=pk)
    form = khadamat_forms(request.POST or None, instance=khadamats)
    if form.is_valid():
        form.save()
        messages.success(request, 'تغییرات ذخیره شد.')
        return redirect('khadamat-list')
    return render(request, 'admin_panel/admin/khadamat/edit_form.html', {'form': form, 'action':'edit'})




#khadamat delete
@login_required
@user_passes_test(is_superadmin)
def khadamat_delete(request, pk):
    khadamats = get_object_or_404(khadamat, pk=pk)
    if request.method == 'POST':
        khadamats.delete()
        messages.success(request, ' حذف شد.')
        return redirect('khadamat-list')
    return render(request, 'admin_panel/admin/khadamat/confirm_delete.html', {'object':'khadamats' })