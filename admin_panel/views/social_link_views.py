from django.shortcuts import render , redirect , get_object_or_404
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required, user_passes_test

from django.contrib import messages
from admin_panel.forms import social_forms
from blog.models import Social_link
def is_superadmin(user):
    return user.is_authenticated and user.role =='superadmin'

def is_admin(user):
    return user.is_authenticated and user.role =='admin'

def is_staff(user):

    return user.is_authenticated and user.role =='staff'

def is_doctor(user):

    return user.is_authenticated and user.role =='doctor'




#social_link list
@login_required
@user_passes_test(is_staff)
def social_link_list(request):
    Social_links = Social_link.objects.all()
    return render(request, 'admin_panel/admin/socail_link/list.html', {'Social_links': Social_links})




#social_link  add
@login_required
@user_passes_test(is_superadmin)
def social_link_add(request):
    form =social_forms (request.POST or None)
    if form.is_valid():
        form.save()
        messages.success(request, ' اضافه شد.')
        return redirect('social-link-list')
    return render(request, 'admin_panle/admin/socail_link/add_form.html', {'form': form, 'action':'add'})


# social_link edit
@login_required
@user_passes_test(is_superadmin)
def social_link_edit(request, pk):
    social_links = get_object_or_404(Social_link, pk=pk)
    form = social_forms(request.POST or None, instance=social_links)
    if form.is_valid():
        form.save()
        messages.success(request, 'تغییرات ذخیره شد.')
        return redirect('social-link-list')
    return render(request, 'admin_panel/admin/socail_link/edit_form.html', {'form': form, 'action':'edit'})




# social_link delete
@login_required
@user_passes_test(is_superadmin)
def social_link_delete(request, pk):
    social_links = get_object_or_404(Social_link, pk=pk)
    if request.method == 'POST':
        social_links.delete()
        messages.success(request, ' حذف شد.')
        return redirect('social-link-list')
    return render(request, 'admin_panel/admin/socail_link/confirm_delete.html', {'object':'social_links' })