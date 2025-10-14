from django.shortcuts import render , redirect , get_object_or_404
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required, user_passes_test


from django.contrib import messages
from admin_panel.forms import city_form
from Doctor.models import City

def is_superadmin(user):
    return user.is_authenticated and user.role =='superadmin'

def is_admin(user):
    return user.is_authenticated and user.role =='admin'

def is_staff(user):

    return user.is_authenticated and user.role =='staff'

def is_doctor(user):

    return user.is_authenticated and user.role =='doctor'


#لیست شهر
@login_required

def city_list(request):
    cities = City.objects.all()
    return render(request, 'admin_panel/admin/city/list.html', {'cities': cities})

#افزودن شهر
@login_required
@user_passes_test(is_superadmin)
def city_add(request):
    form =city_form (request.POST or None)
    if form.is_valid():
        form.save()
        messages.success(request, 'بیمه اضافه شد.')
        return redirect('city-list')
    return render(request, 'admin_panel/admin/city/add_form.html', {'form': form, 'action':'add'})


#ویرایش شهر
@login_required
@user_passes_test(is_superadmin)
def city_edit(request, pk):
    city = get_object_or_404(City, pk=pk)
    form = city_form(request.POST or None, instance=city)
    if form.is_valid():
        form.save()
        messages.success(request, 'تغییرات ذخیره شد.')
        return redirect('city-list')
    return render(request, 'admin_panel/admin/city/edit_form.html', {'form': form, 'action':'edit'})

#حذف شهر
@login_required
@user_passes_test(is_superadmin)
def city_delete(request, pk):
    city = get_object_or_404(City, pk=pk)
    if request.method == 'POST':
        city.delete()
        messages.success(request, 'تخصص حذف شد.')
        return redirect('city-list')
    return render(request, 'admin_panel/admin/city/confirm_delete.html', {'object':'city' })