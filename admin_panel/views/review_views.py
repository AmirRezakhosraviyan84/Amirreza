from django.shortcuts import render , redirect , get_object_or_404
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required, user_passes_test


from django.contrib import messages
from admin_panel.forms import Review_forms
from Doctor.models import Review

def is_superadmin(user):
    return user.is_authenticated and user.role =='superadmin'

def is_admin(user):
    return user.is_authenticated and user.role =='admin'

def is_staff(user):

    return user.is_authenticated and user.role =='staff'

def is_doctor(user):

    return user.is_authenticated and user.role =='doctor'

#review list
@login_required
@user_passes_test(is_staff)
def review_list(request):
    reviews = Review.objects.all()
    return render(request, 'admin_panel/admin/review/list.html', {'reviews': reviews})


#review add
@login_required
@user_passes_test(is_superadmin)
def review_add(request):
    form =Review_forms (request.POST or None)
    if form.is_valid():
        form.save()
        messages.success(request, 'نظر اضافه شد.')
        return redirect('review-list')
    return render(request, 'admin_panel/admin/review/add_form.html', {'form': form, 'action':'add'})


#review edit
@login_required
@user_passes_test(is_superadmin)
def review_edit(request, pk):
    reviews = get_object_or_404(Review, pk=pk)
    form = Review_forms(request.POST or None, instance=reviews)
    if form.is_valid():
        form.save()
        messages.success(request, 'تغییرات ذخیره شد.')
        return redirect('review-list')
    return render(request, 'admin_panel/admin/review/edit_form.html', {'form': form, 'action':'edit'})

#review delete
@login_required
@user_passes_test(is_superadmin)
def review_delete(request, pk):
    reviews = get_object_or_404(Review, pk=pk)
    if request.method == 'POST':
        reviews.delete()
        messages.success(request, 'نظر حذف شد.')
        return redirect('review-list')
    return render(request, 'admin_panel/admin/review/confirm_delete.html', {'object':'reviews' })