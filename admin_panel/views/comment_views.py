from django.shortcuts import render , redirect , get_object_or_404
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required, user_passes_test


from django.contrib import messages
from admin_panel.forms import Comment_form
from core.models import Comment

def is_superadmin(user):
    return user.is_authenticated and user.role =='superadmin'

def is_admin(user):
    return user.is_authenticated and user.role =='admin'

def is_staff(user):

    return user.is_authenticated and user.role =='staff'

def is_doctor(user):

    return user.is_authenticated and user.role =='doctor'





def comment_list(request):
    comments = Comment.objects.all()
    return render(request, 'admin_panel/admin/comment/list.html', {'comments': comments})

def comment_add(request):
    form = Comment_form(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('comment-list')
    return render(request, 'admin_panel/admin/comment/add_form.html', {'form': form})

def comment_edit(request, pk):
    obj = get_object_or_404(Comment, pk=pk)
    form = Comment_form(request.POST or None, instance=obj)
    if form.is_valid():
        form.save()
        return redirect('comment-list')
    return render(request, 'admin_panel/admin/comment/edit_form.html', {'form': form})

def comment_delete(request, pk):
    obj = get_object_or_404(Comment, pk=pk)
    obj.delete()
    return redirect('comment-list')