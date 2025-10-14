from django.shortcuts import render , redirect , get_object_or_404
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required, user_passes_test


from django.contrib import messages
from ..forms import *
from ..models import *
# Create your views here.
def is_superadmin(user):
    return user.is_authenticated and user.role =='superadmin'

def is_admin(user):
    return user.is_authenticated and user.role =='admin'

def is_staff(user):

    return user.is_authenticated and user.role =='staff'

def is_doctor(user):

    return user.is_authenticated and user.role =='doctor'



def adminlogin(request):
    if request.method =='POST':
        form =AdminLoginForm(request.POST)
        if form.is_valid():
            phone =form.cleaned_data['phone_number']
            password =form.cleaned_data['password']

            user =authenticate(request , phone_number=phone , password=password)
            if user is not None and user.role =='superadmin':
                login(request,user)
                return redirect('admin_dashboard')
            else:
                form =AdminLoginForm()
            return render(request, 'admin_panel/admin/admin_login.html',{'form':form})
    else:
        form=AdminLoginForm()
        return render(request , 'admin_panel/admin/admin_login.html',{'form':form})