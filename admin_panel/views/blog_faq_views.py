from django.shortcuts import render , redirect , get_object_or_404
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required, user_passes_test

from django.contrib import messages
from admin_panel.forms import FAQ_forms
from blog.models import FAQ
def is_superadmin(user):
    return user.is_authenticated and user.role =='superadmin'

def is_admin(user):
    return user.is_authenticated and user.role =='admin'

def is_staff(user):

    return user.is_authenticated and user.role =='staff'

def is_doctor(user):

    return user.is_authenticated and user.role =='doctor'




#faq list
@login_required
@user_passes_test(is_staff)
def blog_faq_list(request):
    faqs = FAQ.objects.all()
    return render(request, 'admin-panel/admin/faq2/list.html', {'faqs': faqs})




#faq add
@login_required
@user_passes_test(is_superadmin)
def blog_faq_add(request):
    form =FAQ_forms (request.POST or None)
    if form.is_valid():
        form.save()
        messages.success(request, ' اضافه شد.')
        return redirect('blog-faq-list')
    return render(request, 'admin_panel/admin/faq2/add_form.html', {'form': form, 'action':'add'})


# faq edit
@login_required
@user_passes_test(is_superadmin)
def blog_faq_edit(request, pk):
    faqs = get_object_or_404(FAQ, pk=pk)
    form = FAQ_forms(request.POST or None, instance=faqs)
    if form.is_valid():
        form.save()
        messages.success(request, 'تغییرات ذخیره شد.')
        return redirect('blog-faq-list')
    return render(request, 'admin_panel/admin/faq2/edit_form.html', {'form': form, 'action':'edit'})




# faq delete
@login_required
@user_passes_test(is_superadmin)
def blog_faq_delete(request, pk):
    faqs = get_object_or_404(FAQ, pk=pk)
    if request.method == 'POST':
        faqs.delete()
        messages.success(request, ' حذف شد.')
        return redirect('blog-faq-list')
    return render(request, 'admin_panel/admin/faq2/confirm_delete.html', {'object':'faqs' })