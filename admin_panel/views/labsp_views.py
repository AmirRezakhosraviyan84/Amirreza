from django.shortcuts import render , redirect , get_object_or_404
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib import messages
from admin_panel.forms import Lab_specialty_forms
from Doctor.models import Lab_specialty
def is_superadmin(user):
    return user.is_authenticated and user.role =='superadmin'

def is_admin(user):
    return user.is_authenticated and user.role =='admin'

def is_staff(user):

    return user.is_authenticated and user.role =='staff'

def is_doctor(user):

    return user.is_authenticated and user.role =='doctor'

#labs list
@login_required
@user_passes_test(is_staff)
def labsp_list(request):
    labs = Lab_specialty.objects.all()
    return render(request, 'admin-panel/admin/labs/list.html', {'labs': labs})


#labs add
@login_required
@user_passes_test(is_superadmin)
def labsp_add(request):
    form =Lab_specialty_forms (request.POST or None)
    if form.is_valid():
        form.save()
        messages.success(request, 'تخصص اضافه شد.')
        return redirect('labs-list')
    return render(request, 'admin-panel/admin/labs/add_form.html', {'form': form, 'action':'add'})


#labs edit
@login_required
@user_passes_test(is_superadmin)
def labsp_edit(request, pk):
    labs = get_object_or_404(Lab_specialty, pk=pk)
    form = Lab_specialty_forms(request.POST or None, instance=labs)
    if form.is_valid():
        form.save()
        messages.success(request, 'تغییرات ذخیره شد.')
        return redirect('labs-list')
    return render(request, 'admin-panel/admin/labs/edit_form.html', {'form': form, 'action':'edit'})


#delete labs
@login_required
@user_passes_test(is_superadmin)
def labsp_delete(request, pk):
    labs = get_object_or_404(Lab_specialty, pk=pk)
    if request.method == 'POST':
        labs.delete()
        messages.success(request, 'تخصص حذف شد.')
        return redirect('labs-list')
    return render(request, 'admin-panel/admin/labs/confirm_delete.html', {'object':'labs' })