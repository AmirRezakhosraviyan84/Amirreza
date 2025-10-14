from django.shortcuts import render , redirect , get_object_or_404
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required, user_passes_test

from django.contrib import messages
from admin_panel.forms import wallet_forms
from accounts.models import Wallet
def is_superadmin(user):
    return user.is_authenticated and user.role =='superadmin'

def is_admin(user):
    return user.is_authenticated and user.role =='admin'

def is_staff(user):

    return user.is_authenticated and user.role =='staff'

def is_doctor(user):

    return user.is_authenticated and user.role =='doctor'


#wallet list
@login_required
@user_passes_test(is_staff)
def wallet_list(request):
    wallets = Wallet.objects.all()
    return render(request, 'admin_panel/admin/wallet/list.html', {'wallets': wallets})




#wallet add
@login_required
@user_passes_test(is_superadmin)
def wallet_add(request):
    form =wallet_forms (request.POST or None)
    if form.is_valid():
        form.save()
        messages.success(request, ' اضافه شد.')
        return redirect('wallet-list')
    return render(request, 'admin_panel/admin/wallet/add_form.html', {'form': form, 'action':'add'})


# wallet edit
@login_required
@user_passes_test(is_superadmin)
def wallet_edit(request, pk):
    wallets = get_object_or_404(Wallet, pk=pk)
    form = wallet_forms(request.POST or None, instance=wallets)
    if form.is_valid():
        form.save()
        messages.success(request, 'تغییرات ذخیره شد.')
        return redirect('wallet-list')
    return render(request, 'admin_panel/admin/wallet/edit_form.html', {'form': form, 'action':'edit'})




# wallet delete
@login_required
@user_passes_test(is_superadmin)
def wallet_delete(request, pk):
    Wallets = get_object_or_404(Wallet, pk=pk)
    if request.method == 'POST':
        Wallets.delete()
        messages.success(request, ' حذف شد.')
        return redirect('wallet_list')
    return render(request, 'admin_panel/admin/wallet/confirm_delete.html', {'object':'Wallets' })