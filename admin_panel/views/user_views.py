from django.shortcuts import render , redirect , get_object_or_404
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required, user_passes_test


from django.contrib import messages
from admin_panel.forms import UserForm
from accounts.models import CustomUser

def is_superadmin(user):
    return user.is_authenticated and user.role =='superadmin'

def is_admin(user):
    return user.is_authenticated and user.role =='admin'

def is_staff(user):

    return user.is_authenticated and user.role =='staff'

def is_doctor(user):

    return user.is_authenticated and user.role =='doctor'



#یوزر لیست
@login_required

def user_list(request):
    users = CustomUser.objects.all()
    return render(request, 'admin_panel/admin/user/list.html', {'users': users})


#ساخت یوزر
@login_required
@user_passes_test(is_superadmin)
def user_add(request):
    form =UserForm (request.POST or None)
    if form.is_valid():
        form.save()
        messages.success(request, ' اضافه شد.')
        return redirect('user-list')
    return render(request, 'admin_panel/admin/user/add_form.html', {'form': form, 'action':'add'})


# ویرایش یوزر
@login_required
@user_passes_test(is_superadmin)
def user_edit(request, pk):
    user = get_object_or_404(CustomUser, pk=pk)
    form =UserForm (request.POST or None, instance=user)
    if form.is_valid():
        form.save()
        messages.success(request, 'تغییرات ذخیره شد.')
        return redirect('user-list')
    return render(request, 'admin_panel/admin/user/edit_form.html', {'form': form, 'action':'edit'})



# حذف یوزر
@login_required
@user_passes_test(is_superadmin)
def user_delete(request, pk):
    user = get_object_or_404(CustomUser, pk=pk)
    if request.method == 'POST':
        user.delete()
        messages.success(request, ' حذف شد.')
        return redirect('user-list')
    return render(request, 'admin_panel/admin/user/confirm_delete.html', {'object':'user' })