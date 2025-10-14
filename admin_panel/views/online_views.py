from django.shortcuts import render , redirect , get_object_or_404
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required, user_passes_test


from django.contrib import messages
from admin_panel.forms import Onlinemedicalconsultation_forms
from Doctor.models import Onlinemedicalconsultation

def is_superadmin(user):
    return user.is_authenticated and user.role =='superadmin'

def is_admin(user):
    return user.is_authenticated and user.role =='admin'

def is_staff(user):

    return user.is_authenticated and user.role =='staff'

def is_doctor(user):

    return user.is_authenticated and user.role =='doctor'


#online list
@login_required
@user_passes_test(is_staff)
def online_list(request):
    on = Onlinemedicalconsultation.objects.all()
    return render(request, 'admin_panel/admin/online/list.html', {'on': on})


#online add
@login_required
@user_passes_test(is_superadmin)
def online_add(request):
    form =Onlinemedicalconsultation_forms (request.POST or None)
    if form.is_valid():
        form.save()
        messages.success(request, ' اضافه شد.')
        return redirect('online-list')
    return render(request, 'admin_panel/admin/online/add_form.html', {'form': form, 'action':'add'})



#online edit
@login_required
@user_passes_test(is_superadmin)
def online_edit(request, pk):
    on = get_object_or_404(Onlinemedicalconsultation, pk=pk)
    form = Onlinemedicalconsultation_forms(request.POST or None, instance=on)
    if form.is_valid():
        form.save()
        messages.success(request, 'تغییرات ذخیره شد.')
        return redirect('online-list')
    return render(request, 'admin_panel/admin/online/edit_form.html', {'form': form, 'action':'edit'})




#online delete
@login_required
@user_passes_test(is_superadmin)
def online_delete(request, pk):
    on = get_object_or_404(Onlinemedicalconsultation, pk=pk)
    if request.method == 'POST':
        on.delete()
        messages.success(request, 'نظر حذف شد.')
        return redirect('online_list')
    return render(request, 'admin_panel/admin/online/confirm_delete.html', {'object':'on' })