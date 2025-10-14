from django.shortcuts import render,get_object_or_404, redirect
from django.contrib.auth import authenticate, login
from .forms import CustomUserCreationForm
from .forms import CustomUserCreationForm,RegisterForm,PhoneForm
from django.views.decorators.csrf import csrf_exempt
from django.urls import reverse_lazy
from django.http import JsonResponse
from .forms import DoctorForm,profile_form,WalletTopUpForm
from django.utils import timezone
from .models import CustomUser
from .models import UserOTP,Wallet
from Doctor.models import Doctor,Appointment,Order
from django.contrib.auth import get_user_model
from django.contrib.auth import logout


# Create your views here.



def signup_view(request):
    phone = request.GET.get('phone', '')

    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            username = phone  # استفاده از شماره موبایل به عنوان username

            # بررسی وجود کاربر با همین شماره
            if User.objects.filter(username=username).exists():
                form.add_error('full_name', 'این شماره موبایل قبلا ثبت شده است.')
            else:
                User.objects.create_user(
                    username=username,
                    password=form.cleaned_data['password'],
                    full_name=form.cleaned_data['full_name'],
                    phone_number=phone
                )
                # بعد از ثبت نام، ریدایرکت به لاگین
                return redirect('login')

    else:
        form = CustomUserCreationForm()

    return render(request, 'registration/signup.html', {'form': form, 'phone': phone})




def register_doctor(request):
    if request.method == 'POST':
        form = DoctorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('success')
    else:
        form = DoctorForm()
    return render(request, 'registration/register_doctor.html', {'form': form})




User = get_user_model()

def Register_User(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.is_active = False
            user.save()

            phone = form.cleaned_data['phone_number']
            otp = UserOTP.objects.create(user=user, phone_number=phone)
            print(f"OTP for {phone}: {otp.code}")

            return redirect('verify_otp', user_id=user.id)
        else:
            # فرم نامعتبر → render فرم با خطاها
            return render(request, 'registration/register.html', {'form': form})
    else:
        # حالت GET → فرم خالی
        form = RegisterForm()
        return render(request, 'registration/register.html', {'form': form})




@csrf_exempt
def Register_phone(request):
    if request.method == "POST":
        phone = request.POST.get('phone_number')
        if not phone:
            return JsonResponse({'success': False, 'errors': 'شماره موبایل وارد نشده'})
        
        # حذف OTPهای قبلی
        UserOTP.objects.filter(phone_number=phone).delete()
        phone = request.POST.get('phone_number')
        print("شماره دریافت شده:", phone)
        
        # ایجاد OTP ثابت برای تست
        otp_obj = UserOTP.objects.create(
            phone_number=phone,
            code='123456',
            created_at=timezone.now()
        )
        print(f"OTP برای شماره {phone}: {otp_obj.code}")
        return JsonResponse({'success': True, 'otp_id': otp_obj.id})
    return JsonResponse({'success': False, 'errors': 'درخواست نامعتبر'})



@csrf_exempt
# تایید OTP و ایجاد/ورود کاربر
def verify_otp(request, otp_id):
    if request.method == "POST":
        code = request.POST.get("code")
        try:
            otp_obj = UserOTP.objects.get(id=otp_id)
        except UserOTP.DoesNotExist:
            return JsonResponse({"success": False, "error": "رکورد پیدا نشد"})

        if otp_obj.code != code:
            return JsonResponse({"success": False, "error": "کد وارد شده اشتباه است"})

        # بررسی موجود بودن کاربر
        try:
            user = CustomUser.objects.get(phone_number=otp_obj.phone_number)
        except CustomUser.DoesNotExist:
            # کاربر جدید ایجاد می‌کنیم
            user = CustomUser.objects.create_user(
                phone_number=otp_obj.phone_number,
                password=None
            )

        login(request, user)
        otp_obj.delete()  # پاک کردن OTP بعد از استفاده
        return JsonResponse({"success": True})
    return JsonResponse({"success": False, "error": "درخواست نامعتبر"})


@csrf_exempt
# ارسال دوباره OTP
def Resend_otp_code(request, otp_id):
    try:
        otp_obj = UserOTP.objects.get(id=otp_id)
    except UserOTP.DoesNotExist:
        return JsonResponse({"success": False, "error": "رکورد پیدا نشد"})

    otp_obj.code = "123456"  # مقدار ثابت
    otp_obj.created_at = timezone.now()
    otp_obj.save()
    print(f"OTP دوباره برای شماره {otp_obj.phone_number} : {otp_obj.code}")
    return JsonResponse({"success": True})




@csrf_exempt
def register_doctor_phone(request):
    if request.method == "POST":
        phone = request.POST.get('phone_number')
        if not phone:
            return JsonResponse({'success': False, 'errors': 'شماره موبایل وارد نشده'})

        if len(phone) < 10:
            return JsonResponse({'success': False, 'errors': 'شماره موبایل نامعتبر است'})

        # حذف OTPهای قبلی برای این شماره و user_type
        UserOTP.objects.filter(phone_number=phone, user_type='doctor').delete()

        # ایجاد OTP جدید
        otp_obj = UserOTP.objects.create(
            phone_number=phone,
            code='123456',  # برای تست
            user_type='doctor'
        )

        return JsonResponse({'success': True, 'otp_id': otp_obj.id})
    
    return JsonResponse({'success': False, 'errors': 'درخواست نامعتبر'})



@csrf_exempt
def verify_doctor_otp(request, otp_id):
    if request.method == "POST":
        code = request.POST.get("code")
        try:
            otp_obj = UserOTP.objects.get(id=otp_id, user_type='doctor')
        except UserOTP.DoesNotExist:
            return JsonResponse({"success": False, "error": "رکورد پیدا نشد"})

        if otp_obj.code != code:
            return JsonResponse({"success": False, "error": "کد وارد شده اشتباه است"})

        # بررسی موجود بودن دکتر
        try:
            doctor = Doctor.objects.get(phone_number=otp_obj.phone_number)
        except Doctor.DoesNotExist:
            doctor = Doctor.objects.create(
                phone_number=otp_obj.phone_number,
            )

        # برای دکتر شاید بخواهیم login نکنیم، یا session مخصوص دکتر ایجاد کنیم
        otp_obj.delete()
        return JsonResponse({"success": True})

@csrf_exempt
def resend_doctor_otp(request, otp_id):
    try:
        otp_obj = UserOTP.objects.get(id=otp_id, user_type='doctor')
    except UserOTP.DoesNotExist:
        return JsonResponse({"success": False, "error": "رکورد پیدا نشد"})

    # ایجاد OTP جدید (یا ارسال دوباره همان OTP تست)
    otp_obj.code = "123456"  # برای تست ثابت، بعداً می‌تونی random بذاری
    otp_obj.created_at = timezone.now()
    otp_obj.save()

    return JsonResponse({"success": True})


def logout_view(request):
    logout(request)  # کاربر را لاگ‌اوت می‌کند
    return redirect('home')



def popup_phone_template(request):
    form = PhoneForm()  # فرم شماره موبایل
    return render(request, 'registration/popup_phone.html', {'form': form})



def profile_view(request):
    user = request.user  # کاربر لاگین شده
    form = profile_form(request.POST or None, instance=user)
  

    wallet =Wallet.objects.get_or_create(user=user)[0]
    wallet_form = WalletTopUpForm(request.POST or None)


    if request.method == "POST":
        if 'profile_submit' in request.POST and form.is_valid():
            form.save()
        elif 'wallet_submit' in request.POST and wallet_form.is_valid():
            wallet.balance += wallet_form.cleaned_data['amount']
            wallet.save()
            return redirect('profile')  # بعد از شارژ صفحه ریفرش شود

    appointments = Appointment.objects.filter(booked_by=user, is_booked=True).order_by('-date', '-time')
    orders = Order.objects.filter(user=user).order_by('-date')

    return render(request, 'accounts/profile.html', {'form': form , 'appointments':appointments ,'orders':orders , 'wallet':wallet,'wallet_form': wallet_form,'formatted_balance': f"{wallet.balance:,.0f}"})
