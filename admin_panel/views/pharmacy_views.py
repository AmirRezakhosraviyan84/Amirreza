from django.shortcuts import render , redirect , get_object_or_404
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib import messages
from admin_panel.forms import pharmacy_forms
from Doctor.models import pharmacy
def is_superadmin(user):
    return user.is_authenticated and user.role =='superadmin'

def is_admin(user):
    return user.is_authenticated and user.role =='admin'

def is_staff(user):

    return user.is_authenticated and user.role =='staff'

def is_doctor(user):

    return user.is_authenticated and user.role =='doctor'






#pharmacy list
@login_required

def pharmacy_list(request):
    pharmacies = pharmacy.objects.all()
    return render(request, 'admin_panel/admin/pharmacy/list.html', {'pharmacies': pharmacies})

#pharmacy add
@login_required
@user_passes_test(is_superadmin)
def pharmacy_add(request):
    form =pharmacy_forms (request.POST or None)
    if form.is_valid():
        form.save()
        messages.success(request, 'داروخانه اضافه شد.')
        return redirect('pharmacy-list')
    return render(request, 'admin_panel/admin/pharmacy/add_form.html', {'form': form, 'action':'add'})


#pharmacy edit
@login_required
@user_passes_test(is_superadmin)
def pharmacy_edit(request, pk):
    pharmacies = get_object_or_404(pharmacy, pk=pk)
    form = pharmacy_forms(request.POST or None, instance=pharmacies)
    if form.is_valid():
        form.save()
        messages.success(request, 'تغییرات ذخیره شد.')
        return redirect('pharmacy-list')
    return render(request, 'admin_panel/admin/pharmacy/edit_form.html', {'form': form, 'action':'edit'})

#delete pharmacy
@login_required
@user_passes_test(is_superadmin)
def pharmacy_delete(request, pk):
    pharmacies = get_object_or_404(pharmacy, pk=pk)
    if request.method == 'POST':
        pharmacies.delete()
        messages.success(request, 'کلینیک حذف شد.')
        return redirect('pharmacy-list')
    return render(request, 'admin_panel/admin/pharmacy/confirm_delete.html', {'object':'pharmacies' })
