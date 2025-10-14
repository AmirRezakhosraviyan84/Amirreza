from django.shortcuts import render , redirect , get_object_or_404
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required, user_passes_test


from django.contrib import messages
from admin_panel.forms import type_form
from blog.models import type

def is_superadmin(user):
    return user.is_authenticated and user.role =='superadmin'

def is_admin(user):
    return user.is_authenticated and user.role =='admin'

def is_staff(user):

    return user.is_authenticated and user.role =='staff'

def is_doctor(user):

    return user.is_authenticated and user.role =='doctor'




#type list
@login_required
@user_passes_test(is_staff)
def type_list(request):
    types = type.objects.all()
    return render(request, 'admin_panel/admin/type/list.html', {'types': types})




#type  add
@login_required
@user_passes_test(is_superadmin)
def type_add(request):
    form =type_form (request.POST or None)
    if form.is_valid():
        form.save()
        messages.success(request, ' اضافه شد.')
        return redirect('type-list')
    return render(request, 'admin_panel/admin/type/add_form.html', {'form': form, 'action':'add'})


# type edit
@login_required
@user_passes_test(is_superadmin)
def type_edit(request, pk):
    types = get_object_or_404(type, pk=pk)
    form = type_form(request.POST or None, instance=types)
    if form.is_valid():
        form.save()
        messages.success(request, 'تغییرات ذخیره شد.')
        return redirect('type-list')
    return render(request, 'admin_panel/admin/type/edit_form.html', {'form': form, 'action':'edit'})




# type delete
@login_required
@user_passes_test(is_superadmin)
def type_delete(request, pk):
    types = get_object_or_404(type, pk=pk)
    if request.method == 'POST':
        types.delete()
        messages.success(request, ' حذف شد.')
        return redirect('type-list')
    return render(request, 'admin_panel/admin/type/confirm_delete.html', {'object':'types' })