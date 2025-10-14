from django import forms
from .models import PatientInfo,DoctorRating , WAITING_CHOICES , REASON_CHOICES ,Review
from django.core.exceptions import ValidationError

class PatientInfoForm(forms.ModelForm):
    class Meta:
            model = PatientInfo
            fields = ['first_name', 'last_name', 'national_code', 'gender', 'birth_year', 'city']
            labels = {
            'first_name': 'نام',
            'last_name': 'نام خانوادگی',
            'national_code': 'کد ملی',
            'gender': 'جنسیت',
            'birth_year': 'سال تولد',
            'city': 'شهر',
        }
            
class RatingForm(forms.ModelForm):
    class Meta:
        model = DoctorRating
        fields = ['score']
        widgets = {
            'score': forms.RadioSelect(choices=[(i, i) for i in range(1, 6)])
        }

    def clean_score(self):
        score = self.cleaned_data.get('score')
        if score is None:
            raise ValidationError("لطفا یک امتیاز انتخاب کنید.")
        if score < 1 or score > 5:
            raise ValidationError("امتیاز باید بین 1 تا 5 باشد.")
        return score    
    

class Review_form(forms.ModelForm):
     
     class Meta:
          model =Review
          fields =[
                "overall", "recommend",
            "behavior", "explain", "skill", "reception", "environment",
            "wait_time", "reason", "comment", "anonymous"
          ]

          widgets = {
            "comment": forms.Textarea(attrs={"rows": 4, "placeholder": "اینجا بنویسید..."}),
            "wait_time": forms.RadioSelect(choices=WAITING_CHOICES),
            "reason": forms.Select(choices=REASON_CHOICES),
        }