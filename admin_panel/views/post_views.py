from django.shortcuts import render , redirect , get_object_or_404
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required, user_passes_test


from django.contrib import messages
from admin_panel.forms import post_form
from blog.models import Post

def is_superadmin(user):
    return user.is_authenticated and user.role =='superadmin'

def is_admin(user):
    return user.is_authenticated and user.role =='admin'

def is_staff(user):

    return user.is_authenticated and user.role =='staff'

def is_doctor(user):

    return user.is_authenticated and user.role =='doctor'



#post list
@login_required
def post_list(request):
    posts = Post.objects.all()
    return render(request, 'admin_panel/admin/post/list.html', {'posts': posts})




#post  add
@login_required
@user_passes_test(is_superadmin)
def post_add(request):
    form =post_form (request.POST or None)
    if form.is_valid():
        form.save()
        messages.success(request, ' اضافه شد.')
        return redirect('post-list')
    return render(request, 'admin_panel/admin/post/add_form.html', {'form': form, 'action':'add'})


# post edit
@login_required
@user_passes_test(is_superadmin)
def post_edit(request, pk):
    posts = get_object_or_404(Post, pk=pk)
    form = post_form(request.POST or None, instance=posts)
    if form.is_valid():
        form.save()
        messages.success(request, 'تغییرات ذخیره شد.')
        return redirect('post-list')
    return render(request, 'admin_panel/admin/post/edit_form.html', {'form': form, 'action':'edit'})




# post delete
@login_required
@user_passes_test(is_superadmin)
def post_delete(request, pk):
    posts = get_object_or_404(Post, pk=pk)
    if request.method == 'POST':
        posts.delete()
        messages.success(request, ' حذف شد.')
        return redirect('post-list')
    return render(request, 'admin_panel/admin/post/confirm_delete.html', {'object':'posts' })
