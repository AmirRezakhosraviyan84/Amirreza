from django.shortcuts import render , redirect , get_object_or_404
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required, user_passes_test


from django.contrib import messages
from admin_panel.forms import Text_Appointment_forms
from Doctor.models import Text_Appointment

def is_superadmin(user):
    return user.is_authenticated and user.role =='superadmin'

def is_admin(user):
    return user.is_authenticated and user.role =='admin'

def is_staff(user):

    return user.is_authenticated and user.role =='staff'

def is_doctor(user):

    return user.is_authenticated and user.role =='doctor'



#text list
@login_required
@user_passes_test(is_staff)
def text_list(request):
    texts = Text_Appointment.objects.all()
    return render(request, 'admin_panel/admin/text/list.html', {'texts': texts})


#text add
@login_required
@user_passes_test(is_superadmin)
def text_add(request):
    form =Text_Appointment_forms (request.POST or None)
    if form.is_valid():
        form.save()
        messages.success(request, ' اضافه شد.')
        return redirect('text-list')
    return render(request, 'admin_panel/admin/text/add_form.html', {'form': form, 'action':'add'})


# text edit
@login_required
@user_passes_test(is_superadmin)
def text_edit(request, pk):
    texts = get_object_or_404(Text_Appointment, pk=pk)
    form = Text_Appointment_forms(request.POST or None, instance=texts)
    if form.is_valid():
        form.save()
        messages.success(request, 'تغییرات ذخیره شد.')
        return redirect('text_list')
    return render(request, 'admin_panel/admin/text/edit_form.html', {'form': form, 'action':'edit'})




# text delete
@login_required
@user_passes_test(is_superadmin)
def text_delete(request, pk):
    texts = get_object_or_404(Text_Appointment, pk=pk)
    if request.method == 'POST':
        texts.delete()
        messages.success(request, ' حذف شد.')
        return redirect('text_list')
    return render(request, 'admin_panel/admin/text/confirm_delete.html', {'object':'texts' })