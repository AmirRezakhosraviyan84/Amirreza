from django.shortcuts import render , redirect , get_object_or_404
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib import messages
from admin_panel.forms import InsuranceForm
from Doctor.models import Insurance
def is_superadmin(user):
    return user.is_authenticated and user.role =='superadmin'

def is_admin(user):
    return user.is_authenticated and user.role =='admin'

def is_staff(user):

    return user.is_authenticated and user.role =='staff'

def is_doctor(user):

    return user.is_authenticated and user.role =='doctor'

#بیمه لیست
@login_required

def insurance_list(request):
    insurances = Insurance.objects.all()
    return render(request, 'admin_panel/admin/insurance/list.html', {'insurances': insurances})

#افزودن بیمه
@login_required
@user_passes_test(is_superadmin)
def insurance_add(request):
    form = InsuranceForm(request.POST or None)
    if form.is_valid():
        form.save()
        messages.success(request, 'بیمه اضافه شد.')
        return redirect('insurance-list')
    return render(request, 'admin_panel/admin/insurance/add_form.html', {'form': form, 'action':'add'})


@login_required
@user_passes_test(is_superadmin)
def insurance_edit(request, pk):
    insurance = get_object_or_404(Insurance, pk=pk)  # ← کلاس با I بزرگ
    form = InsuranceForm(request.POST or None, instance=insurance)
    
    if form.is_valid():
        form.save()
        messages.success(request, 'تغییرات ذخیره شد.')
        return redirect('insurance-list')
    
    return render(
        request,
        'admin_panel/admin/insurance/edit_form.html',
        {'form': form, 'action': 'edit'}
    )



# حذف بیمه
@login_required
@user_passes_test(is_superadmin)
def insurance_delete(request, pk):
    insurance = get_object_or_404(Insurance, pk=pk)
    if request.method == 'POST':
        insurance.delete()
        messages.success(request, 'تخصص حذف شد.')
        return redirect('insurance-list')
    return render(request, 'admin_panel/admin/insurance/confirm_delete.html', {'object':'insurance' })
