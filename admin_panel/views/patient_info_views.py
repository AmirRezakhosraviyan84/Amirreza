from django.shortcuts import render , redirect , get_object_or_404
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required, user_passes_test


from django.contrib import messages
from admin_panel.forms import PatientInfo_forms
from Doctor.models import PatientInfo

def is_superadmin(user):
    return user.is_authenticated and user.role =='superadmin'

def is_admin(user):
    return user.is_authenticated and user.role =='admin'

def is_staff(user):

    return user.is_authenticated and user.role =='staff'

def is_doctor(user):

    return user.is_authenticated and user.role =='doctor'



#info list
@login_required
@user_passes_test(is_staff)
def patient_info_list(request):
    info = PatientInfo.objects.all()
    return render(request, 'admin_panel/admin/info/list.html', {'info': info})




#info add
@login_required
@user_passes_test(is_superadmin)
def patient_info_add(request):
    form =PatientInfo_forms (request.POST or None)
    if form.is_valid():
        form.save()
        messages.success(request, ' اضافه شد.')
        return redirect('info-list')
    return render(request, 'admin_panel/admin/info/add_form.html', {'form': form, 'action':'add'})


# info edit
@login_required
@user_passes_test(is_superadmin)
def patient_info_edit(request, pk):
    info = get_object_or_404(PatientInfo, pk=pk)
    form = PatientInfo_forms(request.POST or None, instance=info)
    if form.is_valid():
        form.save()
        messages.success(request, 'تغییرات ذخیره شد.')
        return redirect('info-list')
    return render(request, 'admin_panel/admin/info/edit_form.html', {'form': form, 'action':'edit'})




# info delete
@login_required
@user_passes_test(is_superadmin)
def patient_info_delete(request, pk):
    info = get_object_or_404(PatientInfo, pk=pk)
    if request.method == 'POST':
        info.delete()
        messages.success(request, ' حذف شد.')
        return redirect('info-list')
    return render(request, 'admin_panel/admin/info/confirm_delete.html', {'object':'info' })