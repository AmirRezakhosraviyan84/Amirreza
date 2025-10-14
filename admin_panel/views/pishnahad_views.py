from django.shortcuts import render , redirect , get_object_or_404
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib import messages
from admin_panel.forms import Pishnahad_forms
from Doctor.models import Pishnahad
def is_superadmin(user):
    return user.is_authenticated and user.role =='superadmin'

def is_admin(user):
    return user.is_authenticated and user.role =='admin'

def is_staff(user):

    return user.is_authenticated and user.role =='staff'

def is_doctor(user):

    return user.is_authenticated and user.role =='doctor'



#pishnahad list
@login_required
@user_passes_test(is_staff)
def pishnahad_list(request):
    pishnahads = Pishnahad.objects.all()
    return render(request, 'admin_panel/admin/pishnahad/list.html', {'pishnahads': pishnahads})




#Pishnahad add
@login_required
@user_passes_test(is_superadmin)
def pishnahad_add(request):
    form =Pishnahad_forms (request.POST or None)
    if form.is_valid():
        form.save()
        messages.success(request, ' اضافه شد.')
        return redirect('Pishnahad-list')
    return render(request, 'admin_panel/admin/Pishnahad/add_form.html', {'form': form, 'action':'add'})



# Pishnahad edit
@login_required
@user_passes_test(is_superadmin)
def pishnahad_edit(request, pk):
    Pishnahads = get_object_or_404(Pishnahad, pk=pk)
    form = Pishnahad_forms(request.POST or None, instance=Pishnahads)
    if form.is_valid():
        form.save()
        messages.success(request, 'تغییرات ذخیره شد.')
        return redirect('Pishnahad-list')
    return render(request, 'admin_paneel/admin/Pishnahad/edit_form.html', {'form': form, 'action':'edit'})




# Pishnahad delete
@login_required
@user_passes_test(is_superadmin)
def pishnahad_delete(request, pk):
    Pishnahads = get_object_or_404(Pishnahad, pk=pk)
    if request.method == 'POST':
        Pishnahads.delete()
        messages.success(request, ' حذف شد.')
        return redirect('Pishnahad-list')
    return render(request, 'admin_panel/admin/Pishnahad/confirm_delete.html', {'object':'Pishnahads' })