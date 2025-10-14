from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render , redirect , get_object_or_404
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib import messages
from admin_panel.forms import PishnahadImage_forms
from Doctor.models import PishnahadImage
def is_superadmin(user):
    return user.is_authenticated and user.role =='superadmin'

def is_admin(user):
    return user.is_authenticated and user.role =='admin'

def is_staff(user):

    return user.is_authenticated and user.role =='staff'

def is_doctor(user):

    return user.is_authenticated and user.role =='doctor'




#pishnahad-img list
@login_required
@user_passes_test(is_staff)
def pishnahadimg_list(request):
    pishnahad_imgs = PishnahadImage.objects.all()
    return render(request, 'admin_panel/admin/pishnahad_img/list.html', {'pishnahad_imgs': pishnahad_imgs})



#Pishnahad-img add
@login_required
@user_passes_test(is_superadmin)
def pishnahadimg_add(request):
    form =PishnahadImage_forms (request.POST or None)
    if form.is_valid():
        form.save()
        messages.success(request, ' اضافه شد.')
        return redirect('Pishnahadimg-list')
    return render(request, 'admin_panel/admin/Pishnahad_img/add_form.html', {'form': form, 'action':'add'})


# Pishnahad-img edit
@login_required
@user_passes_test(is_superadmin)
def pishnahadimg_edit(request, pk):
    Pishnahadimg = get_object_or_404(PishnahadImage, pk=pk)
    form = PishnahadImage_forms(request.POST or None, instance=Pishnahadimg)
    if form.is_valid():
        form.save()
        messages.success(request, 'تغییرات ذخیره شد.')
        return redirect('Pishnahadimg-list')
    return render(request, 'admin_panel/admin/Pishnahad_img/edit_form.html', {'form': form, 'action':'edit'})




# Pishnahad-img delete
@login_required
@user_passes_test(is_superadmin)
def pishnahadimg_delete(request, pk):
    Pishnahadimg = get_object_or_404(PishnahadImage, pk=pk)
    if request.method == 'POST':
        Pishnahadimg.delete()
        messages.success(request, ' حذف شد.')
        return redirect('Pishnahadimg-list')
    return render(request, 'admin_panel/admin/Pishnahad_img/confirm_delete.html', {'object':'Pishnahadimg' })