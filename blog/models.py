from django.db import models
from django.contrib.auth.models import User
from django.shortcuts import  reverse
from ckeditor.fields import RichTextField
from Doctor.models import Doctor




# Create your models here.

class type(models.Model):
     name =models.CharField(max_length=50)
     parent = models.ForeignKey(
        'self', null=True, blank=True,
        on_delete=models.CASCADE, related_name='children')
     slug = models.SlugField(null=True, blank=True, unique=True)
     image =models.ImageField( null=True , blank=True)

     def __str__(self):
          return self.name
     
     def get_absolute_url(self):
         return reverse("type", args=[self.slug])
     

class Post(models.Model):
    STATUS_CHOICES =[
        ('pub','published'),
        ('drf','draft'),
    ]
    title = models.TextField()
    text = RichTextField()   
    author = models.ForeignKey('accounts.CustomUser',on_delete=models.CASCADE)
    date_time_created = models.DateTimeField(auto_now_add=True)
    date_time_modified = models.DateTimeField(auto_now=True)
    status =models.CharField(choices=STATUS_CHOICES,max_length=4) 
    post_type =models.ForeignKey(type, on_delete=models.CASCADE , null=True , blank=True)
    doctors =models.ManyToManyField(Doctor , blank=True)
    image =models.ImageField(upload_to='icons' , null=True , blank= True)

    def __str__(self):
            return self.title
    
    def get_absolute_url(self):
        return reverse("post_detail", args=[self.id])
    


class Social_link(models.Model):
      PLATFORM_CHOICES = [
        ("instagram", "اینستاگرام"),
        ("telegram", "تلگرام"),
        ("youtube", "یوتیوب"),
        ("aparat", "آپارات"),
        ("website", "وب‌سایت"),
    ]


      platform=models.CharField(max_length=50 , choices=PLATFORM_CHOICES)
      title =models.CharField(max_length=50,help_text="")
      url = models.URLField(help_text="آدرس لینک شبکه اجتماعی") 
      icon = models.ImageField(upload_to="icons", blank=True, null=True, help_text="آیکن دلخواه (اختیاری)")  

      def __str__(self):
           return self.title



class FAQ(models.Model):
     post =models.ForeignKey(Post , on_delete= models.CASCADE , related_name='faqs')
     question =models.TextField()
     answer =models.TextField()
     def __str__(self):
        return f"FAQ for {self.post.title}: {self.question}"   
      

    