from django.shortcuts import render,get_object_or_404 ,redirect
from django.views.generic import TemplateView
from datetime import date
from blog.models import type,Post
from django.db.models import Q
from accounts.models import Doctor_register
from Doctor.models import Appointment , Review
from blog.models import Post
from . models import MedicalCenterType, City, Mostvisitedspecializations,Symptoms_and_disease,Onlinemedical,SpecialtiesofDoctorToomedicalcenters,Centersfordiagnosisandtreatmentofsymptomsanddiseases
from. models import Thelatestmedicalcenters,TopClinics,CitieswithDoctorToolaboratories,Comment,Symptomsanddiseasesofwomen, Mostvisitedspecializations, Medical_Centers
from Doctor.models import Specialty,Service,Insurance,Doctor,Paraclinicservices,pharmacy,Onlinemedicalconsultation,labratory,Lab_specialty,khadamat

# Create your views here.
#home view
def home_view(request):
    most_visited = Mostvisitedspecializations.objects.all()[:10]
    cities = City.objects.all().order_by('name')
    Symptoms = Symptoms_and_disease.objects.all()
    Online = Onlinemedical.objects.all()
    tops = TopClinics.objects.all()
    medical = MedicalCenterType.objects.all()
    comment = Comment.objects.all()
    

    doc = Doctor.objects.all()
    for d in doc:
        if not d.image:
            d.image_url = '/static/images/default.jpg'
        else:
            d.image_url = d.image.url

    category = request.GET.get("category")
    city_id = request.GET.get("city")  
    centers =Medical_Centers.objects.all()   
    center_types = MedicalCenterType.objects.all()
    if category:
        centers = centers.filter(type__title__iexact=category)
    if city_id:
        centers = centers.filter(city__id=city_id)

          
    center_types = MedicalCenterType.objects.all()
    cities = City.objects.all()
    post =Post.objects.all()
    type_id = request.GET.get('type')  # حالا id می‌گیریم
    posts = Post.objects.all()
    if type_id:
        posts = posts.filter(type__id=type_id)  # فیلتر با id
    types = type.objects.filter(parent__isnull=True)
    doctor =Doctor.objects.all().order_by()

    context = {
        'Mostvisitedspecializations': most_visited,
        'cities': cities,
        'Symptoms': Symptoms,
        'Onlinemedical': Online,
        'TopClinics': tops,
        'Comment': comment,
        'doc': doc,
        'medical': medical,
        'centers': centers,
        'center_types': center_types,
        'active_category': category,
        'active_city': city_id,
        'center_types':center_types,
        'post':post,
        'posts':posts,
        'types ':types 

        
    }

    return render(request, 'home.html', context)



def search_view(request):
    q = request.GET.get('q', '').strip()
    doctors = Doctor.objects.none()  # پیشفرض هیچ دکتری

    if q:
        # 1) اگر دقیقا اسم یک دکتر بود → فقط همون دکتر
        doctor_match = Doctor.objects.filter(name__iexact=q).first()
        if doctor_match:
             return redirect("doctor_profile", pk=doctor_match.id)

        # 2) اگر دقیقا اسم یک تخصص بود → دکترهای اون تخصص
        specialty = Specialty.objects.filter(name__iexact=q).first()
        if specialty:
            return redirect(f"/doctors/?specialty={specialty.id}")
        

        service =Service.objects.filter(name__iexact=q).first()
        if service:
            return redirect(f"/doctors/?service={service.id}")


        # 4) اگر دقیقا اسم مرکز درمانی بود → دکترهای اون مرکز
        elif Medical_Centers.objects.filter(name__iexact=q).exists():
            center = Medical_Centers.objects.get(name__iexact=q)
            doctors = Doctor.objects.filter(center=center)

        # 5) اگر هیچ کدوم match دقیق نشد → سرچ آزاد
        else:
            doctors = Doctor.objects.filter(
                Q(name__icontains=q) |
                Q(description__icontains=q) |
                Q(specialty__name__icontains=q) |
                Q(diseases__name__icontains=q) |
                Q(center__name__icontains=q)
            ).distinct()

    return render(request, "search_result.html", {
        "query": q,
        "doctors": doctors
    })
def nobat_azemayeshgah(request):
    cit = City.objects.all()
    lab = labratory.objects.all()
    labs =Lab_specialty.objects.all()

 
   
    context ={
        'cit':cit,
        'lab':lab,
        'labs':labs,
    }
    return render(request,'box/nobat_azmayeshgah.html',context)



def labratory_detail(request,pk):

 lab =get_object_or_404(labratory, pk=pk)
 labs =Lab_specialty.objects.all()
 

 context ={
     'lab':lab,
     'labs':labs,
     
 }

 return render (request,'clinic/labratory_detail.html', context)

def center_detail(request,pk):
    center =get_object_or_404(MedicalCenterType,pk=pk)
    return render(request,'center_detail.html',{'center':center})

def search_to_lab_detail(request):
    query = request.GET.get('query', '').strip()
    city_id = request.GET.get('city')

    lab = labratory.objects.all()

    if query:
        lab = lab.filter(name__icontains=query)
    if city_id:
        lab = lab.filter(city_id=city_id)

    lab = lab.first()  # اولین نتیجه

    if lab:
        return redirect('labratory_detail', pk=lab.pk)
    else:
        # اگر چیزی پیدا نشد، می‌تونی برگردونی به home یا صفحه نتایج خالی
        return redirect('home')


def medical_center_view(request):
    category = request.GET.get("category")  # داروخانه، کلینیک و ...
    
    if category:
        # گرفتن مراکز درمانی که نوعشون همون category هست
        centers = Medical_Centers.objects.filter(type__title__iexact=category)
    else:
        centers = Medical_Centers.objects.all()

    # گرفتن لیست دسته‌ها برای نمایش فیلتر
    categories = MedicalCenterType.objects.values_list("title", flat=True).distinct()

    return render(request, "home.html", {
        "categories": categories,
        "centers": centers,
        "active_category": category,
    })





def top_clinic_detail(request,pk):
    tp =get_object_or_404(TopClinics,pk=pk)
    box = tp
    doctors =tp.doctors.all()
    com =Comment.objects.all()
    re =Review.objects.all()
  
    return render(request,'clinic/clinic_detail.html',{'box':box,'tp':tp,'com':com,'doctors':doctors , 'clinic_id':tp.id , 're':re})             
      


       

def medical_center_list(request):
    center_types = MedicalCenterType.objects.all()
    cities = City.objects.all()
    specialities =SpecialtiesofDoctorToomedicalcenters.objects.all()
    centers = Centersfordiagnosisandtreatmentofsymptomsanddiseases.objects.all()
    the_lasts = Thelatestmedicalcenters.objects.all()
    return render(request, 'box/Medical centers.html', {
        'center_types': center_types,
        'cities': cities,
        'request': request,
        'specialities': specialities,
        'centers':centers,
        'the_lasts':the_lasts,

    })


def medical_center_detail(request,pk):
    center = get_object_or_404(Centersfordiagnosisandtreatmentofsymptomsanddiseases,pk=pk)
    return render(request,'box/medical_center_detail.html',{'center':center})



def medical_center_type_detail(request, pk):
    center_type = get_object_or_404(MedicalCenterType, pk=pk)
    centers = Medical_Centers.objects.all()

    # فیلتر بر اساس نوع مرکز
    centers = centers.filter(type=center_type)

    # فیلتر بر اساس GET
    city = request.GET.get('city')
    service = request.GET.get('service')
    insurance = request.GET.get('insurance')

    if city:
        centers = centers.filter(city_id=city)
    if service:
        centers = centers.filter(services__id=service)
    if insurance:
        centers = centers.filter(insurances__id=insurance)

    context = {
        'center_type': center_type,
        'centers': centers,
        'cities': City.objects.all(),
        'services': Service.objects.all(),
        'insurances': Insurance.objects.all(),
    }
    return render(request, 'clinic/center_type_detail.html', context)

    

def city_detail(request, pk):
    city = get_object_or_404(City, pk=pk)
    Most = Mostvisitedspecializations.objects.filter(city_id=pk)
    sy = Symptoms_and_disease.objects.filter(city_id=pk)
    doc = Doctor.objects.filter(city_id=pk)  
    ser = Service.objects.filter(city_id=pk)
    medical =MedicalCenterType.objects.filter(city_id=pk)
    pc =Paraclinicservices.objects.filter(city_id=pk)
    ph =pharmacy.objects.filter(city_id=pk)

    return render(request, 'clinic/city_detail.html', {
        'city': city,
        'Most': Most,
        'sy': sy,
        'doc': doc,
        'ser': ser,
        'medical':medical,
        'pc':pc,
        'ph':ph,
    })






def specialty_detail(request,pk):
    sp = get_object_or_404(SpecialtiesofDoctorToomedicalcenters,pk=pk)
    return render(request,'clinic/specialty_detail.html',{'sp':sp})




def latest_center_detail(request,pk):
    la =get_object_or_404(Thelatestmedicalcenters,pk=pk)
    return render (request,'clinic/latset_centerdetail.html',{'la':la})




def most_visited_detail(request, pk):
    box = get_object_or_404(Mostvisitedspecializations, pk=pk)

    specialties = Specialty.objects.all()
    services = Service.objects.all()
    cities = City.objects.all()
    insurances = Insurance.objects.all()

    # انتخاب دکترها فقط برای تخصص‌های مرتبط
    selected_specialties = box.specialties.all()
    doctors = Doctor.objects.filter(
        specialty__in=selected_specialties
    ).order_by("name")

    for doctor in doctors:
        doctor.available_appointments = Appointment.objects.filter(
            doctor=doctor,
            is_booked=False,
            date__gte=date.today()
        ).order_by('date', 'time')

    context = {
        'box': box,
        'specialties': specialties,
        'services': services,
        'cities': cities,
        'insurances': insurances,
        'doctors': doctors,
        'tabs': [
            {'id': 'clinic', 'label': 'نوبت مطب'},
            {'id': 'phone', 'label': 'مشاوره تلفنی'},
            {'id': 'text', 'label': 'مشاوره متنی'},
        ],
        'orting_options': [
            ('popular', 'محبوب‌ترین'),
            ('next', 'نزدیک‌ترین نوبت'),
            ('successful', 'موفق‌ترین نوبت')
        ],
        'selected_specialty_ids': list(selected_specialties.values_list("id", flat=True)),
    }

    return render(request, "clinic/most_visited_detail.html", context)

    


def Symptoms_and_disease_detail(request, pk):
    sy = get_object_or_404(Symptoms_and_disease, pk=pk)
    
    specialties = Specialty.objects.all()
    selected_specialties = sy.specialties.all()

    # دکترهای مرتبط با این بیماری
    doctors = Doctor.objects.filter(
        specialty__in=selected_specialties
    ).order_by("name")

    # فیلترهای GET
    specialty_id = request.GET.get('specialty')
    city_id = request.GET.get('city')
    gender = request.GET.get('gender')

    if specialty_id:
        doctors = doctors.filter(specialty_id=specialty_id)
    if city_id:
        doctors = doctors.filter(city_id=city_id)
    if gender:
        doctors = doctors.filter(gender=gender)

    context = {
        'symptom': sy,
        'doctors': doctors,
        'specialties': specialties,
        'cities': City.objects.all(),
        'selected_specialty_ids': list(selected_specialties.values_list("id", flat=True)),
        'selected_specialty': specialty_id,
        'selected_city': city_id,
        'selected_gender': gender,
    }

    return render(request, 'clinic/Symptoms_and_disease_detail.html', context)





def Online_detail(request, pk):
    on = get_object_or_404(Onlinemedical, pk=pk)
    sp =Specialty.objects.all()
    cities =City.objects.all()
    insurances =Insurance.objects.all()

    doctors = Doctor.objects.filter(
        specialty__in=on.specialties.all()
    ).order_by("name")

    # اعمال فیلترها
    specialty = request.GET.get("specialty")
    city = request.GET.get("city")
    insurance = request.GET.get("insurance")
    urgent = request.GET.get("urgent")
    available = request.GET.get("available")
    gender = request.GET.get("gender")
    sort = request.GET.get("sort")

    if specialty:
        doctors = doctors.filter(specialty_id=specialty)
    if city:
        doctors = doctors.filter(city_id=city)
    if insurance:
        doctors = doctors.filter(insurances__id=insurance)
    if urgent:
        doctors = doctors.filter(urgent_consultation=True)
    if available:
        doctors = doctors.filter(has_available_slots=True)
    if gender:
        if gender in ["خانوم", "آقا"]:
            doctors = doctors.filter(gender=gender)

    # مرتب‌سازی
    if sort == "popular":
        doctors = doctors.order_by("-rating")
    elif sort == "next":
        doctors = doctors.order_by("next_available_date")
    elif sort == "successful":
        doctors = doctors.order_by("-successful_appointments")

    context = {
        "on": on,
        "doctors": doctors,
        "sp":sp,
        "cities":cities,
        "insurances":insurances,
    }
    return render(request, "clinic/online_detail.html", context)





def clinics_doctor(request,clinic_id):
    clinic = get_object_or_404(TopClinics, pk=clinic_id)
    doctors =clinic.doctors.all()
    return render(request ,'clinics_doctors/dr_tavaloly_doctors.html',{'clinic':clinic,'doctors':doctors ,'clinic_id':clinic.id})



def search_form(request):
    query = request.GET.get('q', '').strip()
    
    # اگر چیزی وارد نشده باشد، QuerySet خالی
    doctors = Doctor.objects.none()
    specialties = Specialty.objects.none()
    medical = MedicalCenterType.objects.none()
    
    if query:
        doctors = Doctor.objects.filter(name__icontains=query)
        specialties = Specialty.objects.filter(name__icontains=query)
        medical = MedicalCenterType.objects.filter(title__icontains=query)

    return render(request, 'search_results.html', {
        'query': query,
        'doctors': doctors,
        'specialties': specialties,
        'medical': medical,
    })


def doctor_to_services(request):
    khadamat_obj = get_object_or_404(khadamat, name="پوست ،مو و زیبایی")
    khadamat_obj2 = get_object_or_404(khadamat, name="دندانپزشکی")
    khadamat_obj3 = get_object_or_404(khadamat, name="روانشناسی")
    khadamat_obj4 = get_object_or_404(khadamat, name="چشم پزشکی")
    khadamat_obj5 = get_object_or_404(khadamat, name="اورولوژی")
    khadamat_obj6 = get_object_or_404(khadamat, name="جراحی بینی")
    doc =Doctor.objects.all()
    cit = City.objects.all()
    se =Service.objects.all()
    kh =khadamat.objects.all()
    kho =khadamat.objects.filter(name ='پوست ،مو و زیبایی')
    dan=khadamat.objects.filter(name ='دندانپزشکی')
    zir_dan =Service.objects.filter(khadamat__in=dan).distinct()
    zir_gorooh = Service.objects.filter(khadamat__in=kho).distinct()
    context={
        'doc':doc,
        'cit':cit,
        'se':se,
        'kh':kh,
        'kho':kho,
        'zir_gorooh':zir_gorooh,
       'khadamat_obj':khadamat_obj,
        'dan':dan,
         'zir_dan':zir_dan ,
         'khadamat_obj2':khadamat_obj2,
         'khadamat_obj3':khadamat_obj3,
         'khadamat_obj4':khadamat_obj4,
         'khadamat_obj5':khadamat_obj5,
         'khadamat_obj6':khadamat_obj6}
    
    return render (request , 'box/doctor_to_services.html', context)




