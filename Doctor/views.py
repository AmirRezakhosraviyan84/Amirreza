from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import REASON_CHOICES
from django.urls import reverse
from django.conf import settings
from django.http import HttpResponse
import requests
from django.contrib import messages
from datetime import date
from django.views.generic import TemplateView
from django.contrib.auth.decorators import login_required
from .models import Doctor, Specialty, Service, City, Insurance,Appointment,DoctorRating,FAQ,Phone_Appointment,Text_Appointment,Review

import jdatetime
from .Forms import PatientInfoForm,RatingForm,PatientInfoForm,Review_form
from django.contrib.auth.decorators import login_required

def doctors_list(request):
    doctors = Doctor.objects.all()
    

    # نوبت‌های آزاد هر دکتر
    for doctor in doctors:
        doctor.available_appointments = Appointment.objects.filter(
            doctor=doctor,
            is_booked=False,
            date__gte=date.today()
        ).order_by('date', 'time')

    # فیلترها
    specialty = request.GET.get('specialty')
    service = request.GET.get('service')
    city = request.GET.get('city')
    insurance = request.GET.get('insurance')
    gender = request.GET.get('gender')
    urgent = request.GET.get('urgent')
    available = request.GET.get('available')

    if specialty:
        doctors = doctors.filter(specialty__id=specialty)
    if service:
        doctors = doctors.filter(services__id=service)
    if city:
        doctors = doctors.filter(city_id=city)
    if insurance:
        doctors = doctors.filter(insurances__id=insurance)
    if gender:
        doctors = doctors.filter(gender=gender)
    if urgent:
        doctors = doctors.filter(urgent_consultation=True)

    # فیلتر پزشکان دارای نوبت آزاد
    if available:
        doctors = [doc for doc in doctors if doc.available_appointments.exists()]

    # مرتب‌سازی
    sort = request.GET.get('sort')
    if sort == 'popular':
        doctors = sorted(doctors, key=lambda d: d.rating or 0, reverse=True)
    elif sort == 'next':
        doctors = sorted(
            doctors,
            key=lambda d: d.available_appointments.first().date
            if d.available_appointments.exists() else date.max
        )
    elif sort == 'successful':
        doctors = sorted(doctors, key=lambda d: d.successful_appointments or 0, reverse=True)

    # distinct (در صورت استفاده از list بعد از filter، نیازی نیست)
    # doctors = doctors.distinct()  # فقط برای queryset مفید است

    sorting_options = [
        ('popular', 'محبوب‌ترین'),
        ('next', 'نزدیک‌ترین نوبت'),
        ('successful', 'موفق‌ترین نوبت')
    ]

    tabs = [
        {'id': 'clinic', 'label': 'نوبت مطب'},
        {'id': 'phone', 'label': 'مشاوره تلفنی'},
        {'id': 'text', 'label': 'مشاوره متنی'},
    ]


    context = {
        'doctors': doctors,
        'specialties': Specialty.objects.all(),
        'services': Service.objects.all(),
        'cities': City.objects.all(),
        'insurances': Insurance.objects.all(),
        'sorting_options': sorting_options,
        'tabs': tabs,
        
    }
    return render(request, 'Doctor/doctor_list.html', context)


def doctor_profile(request, pk):
    doc = get_object_or_404(Doctor, pk=pk)
    sp = Specialty.objects.all()
    faqs = FAQ.objects.all().order_by('order')
    reviews =doc.reviews.all()

    def avg(field):
        vals = reviews.values_list(field, flat=True)
        return round(sum(vals) / len(vals), 2) if vals else 0

    # تبدیل فیلد ManyToMany به رشته
    symptoms_str = ", ".join([s.name for s in doc.symptoms.all()]) if hasattr(doc, 'symptoms') else ""
    
    doc.available_appointments = Appointment.objects.filter(
        doctor=doc,
        is_booked=False,
        date__gte=date.today()
    ).order_by('date', 'time')
    first_available = doc.available_appointments.first()

    for f in faqs:
        f.question = (f.question or "").replace("{{doctor.name}}", doc.name or "")
        f.answer   = (f.answer or "").replace("{{doctor.name}}", doc.name or "")
        f.answer   = f.answer.replace("{{doctor.address}}", str(doc.address) if doc.address else "")
        f.answer   = f.answer.replace("{{doctor.symptoms}}", symptoms_str)
        f.answer   = f.answer.replace("{{doctor.specialty}}", str(getattr(doc, 'specialty', '')) or "")
    criteria = [
        {"label": "نحوه برخورد پزشک", "value": avg("behavior"), "percent": avg("behavior") * 20},
        {"label": "توضیح پزشک در هنگام ویزیت", "value": avg("explain"), "percent": avg("explain") * 20},
        {"label": "مهارت پزشک در تشخیص و درمان", "value": avg("skill"), "percent": avg("skill") * 20},
        {"label": "فرآیند پذیرش و رفتار منشی", "value": avg("reception"), "percent": avg("reception") * 20},
        {"label": "شرایط محیطی", "value": avg("environment"), "percent": avg("environment") * 20},
    ]

    return render(request, 'Doctor/doctor_profile.html', {
        'doc': doc,
        'sp': sp,
        'faqs': faqs,
        'first_available':first_available,
        'criteria':criteria,
        "avg_rating": doc.average_rating(),
        "total_reviews": doc.total_reviews(),
    })


def show_doctor_select(request):
    # Show list of all doctors (for selection)
    doctors = Doctor.objects.all()
    return render(request, 'Doctor/doctor_select.html', {'doctors': doctors})



def online_consultation(request):
    doctors = Doctor.objects.all()

    # Apply filters based on GET parameters
    specialty = request.GET.get('specialty')
    for doctor in doctors:
        doctor.available_appointments = Appointment.objects.filter(
            doctor=doctor,
            is_booked=False,
            date__gte=date.today()
        ).order_by('date', 'time')

    if specialty:
        doctors =doctors.filter(specialty__id=specialty)
   
    orting_options = [
    ('popular', 'محبوب‌ترین'),
    ('next', 'نزدیک‌ترین نوبت'),
    ('successful', 'موفق‌ترین نوبت')]

    tabs = [
    {'id': 'clinic', 'label': 'نوبت مطب'},
    {'id': 'phone', 'label': 'مشاوره تلفنی'},
    {'id': 'text', 'label': 'مشاوره متنی'},]
    context = {
        'doctors': doctors,
        'specialties': Specialty.objects.all(),
        'tabs':tabs,
        'orting_options':orting_options,
    }
    return render(request, 'Doctor/onlinemedicalconsultation.html',context)  






@login_required(login_url='/accounts/register_phone/')

def book_appointment(request, appointment_id):
    appointment = get_object_or_404(Appointment, pk=appointment_id, is_booked=False)

    if request.method == 'POST':
        form = PatientInfoForm(request.POST)
        if form.is_valid():
            patient_info = form.save(commit=False)
            patient_info.appointment = appointment
            patient_info.save()

            # علامت‌گذاری نوبت به عنوان رزرو شده
            appointment.is_booked = True
            appointment.booked_by = request.user
            appointment.save()

            return redirect('my_appointments')  # صفحه نوبت‌های رزرو شده کاربر
    else:
        form = PatientInfoForm()

    return render(request, 'Doctor/book_appointment.html', {
        'appointment': appointment,
        'form': form
    })


def doctor_appointments(request, doctor_id):
    appointments = Appointment.objects.filter(
        doctor_id=doctor_id,
        is_booked=False,
        date__gte=date.today()
    ).order_by('date', 'time')

    return render(request, 'Doctor/doctor_appointments.html', {
        'appointments': appointments
    })

EN_TO_FA_WEEKDAYS = {
    "Saturday": "شنبه",
    "Sunday": "یکشنبه",
    "Monday": "دوشنبه",
    "Tuesday": "سه‌شنبه",
    "Wednesday": "چهارشنبه",
    "Thursday": "پنج‌شنبه",
    "Friday": "جمعه",
}

def appointment_list(request):
    doctor_id = request.GET.get("doctor_id")
    today = jdatetime.date.today()
    days = []

    for i in range(30):
        day = today + jdatetime.timedelta(days=i)
        en_day_name = day.strftime("%A")  # خروجی انگلیسی
        days.append({
            "date": day.togregorian().strftime("%Y-%m-%d"),
            "shamsi_date": day.strftime("%Y-%m-%d"),
            "day_name": EN_TO_FA_WEEKDAYS.get(en_day_name, en_day_name)  # ترجمه به فارسی
        })

    selected_date = request.GET.get("date", today.togregorian().strftime("%Y-%m-%d"))

    appointments = Appointment.objects.filter(
        doctor_id=doctor_id,
        date=selected_date
    ).order_by("time")

    today_gregorian = today.togregorian().strftime("%Y-%m-%d")
    if selected_date == today_gregorian:
        now = timezone.localtime().time()
        appointments = appointments.filter(time__gte=now)

    return render(request, "Doctor/appointments.html", {
        "days": days,
        "doctor_id": doctor_id,
        "selected_date": selected_date,
        "appointments": appointments,
    })


#ویو نوبت دهی مشاوره تلفنی

def Phone_appointment_list(request):
    doctor_id = request.GET.get('doctor_id')    
    
    today =jdatetime.date.today()
    days =[]

    for i in range(30):
        day =today+jdatetime.timedelta(days=i)
        en_day_name =day.strftime("%A") #خروجی انگلیسی اسم روزهای هفته
        days.append({
            "date": day.togregorian().strftime("%Y-%m-%d"),
            "shamsi_date": day.strftime("%Y-%m-%d"),
            "day_name": EN_TO_FA_WEEKDAYS.get(en_day_name, en_day_name)})
        
    selected_date = request.GET.get("date", today.togregorian().strftime("%Y-%m-%d")) 
    Phone_appointments =Phone_Appointment.objects.filter(
        doctor_id=doctor_id,
        date=selected_date
    ).order_by("time")
    today_gregorian = today.togregorian().strftime("%Y-%m-%d")
    if selected_date == today_gregorian:
        now = timezone.localtime().time()
        Phone_appointments = Phone_appointments.filter(time__gte=now)

    return render(request , "Doctor/phone_appointment.html",{
        'days':days,
        'doctor_id':doctor_id,
        'selected_date':selected_date,
        "Phone_appointments": Phone_appointments,

    })


#ویوو مساوره متنی
def text_appointment_list(request):

    doctor_id = request.GET.get('doctor_id')
    today  =jdatetime.date.today()
    days =[]

    for i in range(30):
        day =today+jdatetime.timedelta(day=i)
        en_day_name =days.strftime("%A")
        days.append({
           "date": day.togregorian().strftime("%Y-%m-%d"),
            "shamsi_date": day.strftime("%Y-%m-%d"),
            "day_name": EN_TO_FA_WEEKDAYS.get(en_day_name, en_day_name)})
        
        
    selected_date = request.GET.get("date", today.togregorian().strftime("%Y-%m-%d")) 
    text_appointments =Text_Appointment.objects.filter(
        doctor_id=doctor_id,
        date=selected_date
    ).order_by("time")

    today_gregorian = today.togregorian().strftime("%Y-%m-%d")
    if selected_date == today_gregorian:
        now = timezone.localtime().time()
        text_appointments = text_appointments.filter(time__gte=now)   \
        



        return render(request , 'Doctor/text_appointment.html',
           { 'doctor_id':doctor_id,
              'days=':days,
              'selected_date':selected_date,
               'text_appointments':text_appointments,
                               } )

 

    



def appointment_detail(request, appointment_id):
    appointment = get_object_or_404(Appointment, id=appointment_id)
    doctor = appointment.doctor

    if request.method == "POST":
        form = PatientInfoForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            return render(request, "Doctor/appointment_detail.html", {
                "doctor": doctor,
                "appointment": appointment,
                "appointment_data": data,
                "current_step": 2,  # مرحله اطلاعات مراجعه‌کننده
            })
    else:
        form = PatientInfoForm()

    return render(request, "appointment_form.html", {
        "doctor": doctor,
        "appointment": appointment,
        "form": form,
        "current_step": 1,  # مرحله فرم رزرو
    })








@login_required(login_url='/accounts/login/')
def rate_doctor(request, pk):
    doctor = get_object_or_404(Doctor, pk=pk)
    rating, created = DoctorRating.objects.get_or_create(
        doctor=doctor,
        user=request.user
    )

    if request.method == "POST":
        form = RatingForm(request.POST, instance=rating)
        if form.is_valid():
            form.save()
            return redirect('rate', pk=doctor.pk)
    else:
        form = RatingForm(instance=rating)

    avg_rating = doctor.average_rating()  # میانگین امتیاز همه کاربران

    return render(request, "Doctor/rate_doctor.html", {
        'doctor': doctor,
        'form': form,
        'avg_rating': avg_rating
    })

       


def doctor_review(request , pk):
    doctor =get_object_or_404(Doctor , pk=pk)
    reviews =doctor.reviews.all()

    def avg(field):
        vals = reviews.values_list(field, flat=True)
        return round(sum(vals) / len(vals), 2) if vals else 0
    

    criteria = [
        {"label": "نحوه برخورد پزشک", "value": avg("behavior"), "percent": avg("behavior") * 20},
        {"label": "توضیح پزشک در هنگام ویزیت", "value": avg("explain"), "percent": avg("explain") * 20},
        {"label": "مهارت پزشک در تشخیص و درمان", "value": avg("skill"), "percent": avg("skill") * 20},
        {"label": "فرآیند پذیرش و رفتار منشی", "value": avg("reception"), "percent": avg("reception") * 20},
        {"label": "شرایط محیطی", "value": avg("environment"), "percent": avg("environment") * 20},
    ]

    if request.method == "POST":
        form = Review_form(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.doctor = doctor
            if request.user.is_authenticated and not review.anonymous:
                review.user = request.user
            review.save()
            messages.success(request, "نظر شما با موفقیت ثبت شد.")
            return redirect("doctor-review", pk=doctor.pk)
    else:
        form = Review_form()

    context = {
        "doctor": doctor,
        "form": form,
        "criteria": criteria,
        "avg_rating": doctor.average_rating(),
        "total_reviews": doctor.total_reviews(),
        "recommend_percent": doctor.recommend_percent(),
        "avg_wait_label": "۱۵-۰ دقیقه",  # می‌تونی میانگین محاسبه کنی
        "reasons": [{"id": key, "label": label} for key, label in REASON_CHOICES],
    }
    return render(request, "Doctor/rate_doctor.html", context)


#payment view

def payment(request, appointment_id):
    appointment = get_object_or_404(Appointment, id=appointment_id)

    amount = 100000
    callback_url = request.build_absolute_uri(
        reverse('payment_verify', args=[appointment.id])
    )

    data = {
        "merchant_id": settings.ZARINPAL_MERCHANT_ID,
        "amount": amount,
        "callback_url": callback_url,
        "description": "پرداخت نوبت"
    }

    url = "https://sandbox.zarinpal.com/pg/rest/WebGate/PaymentRequest.json"

    try:
        r = requests.post(url, json=data, timeout=10, verify=False)  # verify=False فقط برای تست
        print("Status Code:", r.status_code)
        print("Response Text:", r.text)
        response = r.json()
    except Exception as e:
        return HttpResponse(f"خطا در اتصال به درگاه یا JSON: {e}")

    # sandbox response ممکنه data و authority با حروف متفاوت باشند
    authority = response.get('data', {}).get('Authority') or response.get('data', {}).get('authority')

    if authority:
        payment_url = f"https://sandbox.zarinpal.com/pg/StartPay/{authority}"
        return redirect(payment_url)
    else:
        return HttpResponse(f"خطا در ایجاد پرداخت تستی: {response}")




    

    #payment_verify view
def payment_verify(request, appointment_id):
    appointment = get_object_or_404(Appointment, id=appointment_id)
    authority = request.GET.get('Authority')
    status = request.GET.get('Status')

    if status == 'OK':
        data = {
            "merchant_id": settings.ZARINPAL_MERCHANT_ID,
            "amount": 10000,
            "authority": authority
        }
        url = "https://sandbox.zarinpal.com/pg/rest/WebGate/PaymentVerification.json"
        response = requests.post(url, json=data).json()

        if response.get('Code') == 100:
            appointment.paid = True
            appointment.save()
            return HttpResponse("پرداخت تستی با موفقیت انجام شد")
        else:
            return HttpResponse("پرداخت تستی ناموفق")
    else:
        return HttpResponse("پرداخت تستی لغو شد")




