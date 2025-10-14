from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from . forms import CustomUserChangeForm,CustomUserCreationForm
from . models import CustomUser ,UserOTP,Wallet
# Register your models here.
class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = ('phone_number', 'full_name', 'is_staff', 'is_active')
    list_filter = ('is_staff', 'is_active')
    ordering = ('phone_number',)  # <- اینجا username رو حذف کردیم
    search_fields = ('phone_number', 'full_name')
    fieldsets = (
        (None, {'fields': ('phone_number', 'full_name', 'password')}),
        ('Permissions', {'fields': ('is_staff', 'is_active', 'is_doctor', 'is_patient', 'is_superuser', 'groups', 'user_permissions')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('phone_number', 'full_name', 'password1', 'password2', 'is_staff', 'is_active')}
        ),
    )
   

admin.site.register(CustomUser,CustomUserAdmin)

@admin.register(UserOTP)

class UserOTPAdmin(admin.ModelAdmin):
    list_display =['user','code','phone_number','created_at']



@admin.register(Wallet)

class WalletAdmin(admin.ModelAdmin):
    list_display =['user','balance']