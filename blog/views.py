from django.shortcuts import render , get_object_or_404
from bs4 import BeautifulSoup
from django.template.loader import render_to_string
import re
from django.urls import reverse_lazy
from django.views import generic 
from .form import NEWPostForm
from . models import Post , type , Social_link,FAQ,type
from django.shortcuts import get_object_or_404
from django.views import generic 
from Doctor. models import Doctor , Specialty
from rest_framework.response import Response
from rest_framework import status


def Post_list_view(request):
   
   po =Post.objects.filter(status='pub').order_by('date_time_modified')
   
   sp =Specialty.objects.filter(

     name__in=["قلب و عروق", "مغز و اعصاب", "پوست","ارتوپدی","زنان و زایمان","روانشناسی"]
    ).prefetch_related('doctor_set')
   ty=type.objects.all()

   last_post =Post.objects.all().order_by('-date_time_created')

   right_posts =last_post[:3]  # سه پست اول → ستون راست

   left_posts = last_post[3:6] # سه پست بعدی → ستون چپ

   ri_post =po[:2]

   ce_post=po[2:3]

   le_post  =po[3:5]  

 
   context={
      'po':po,
      'ty':ty,
      'right_posts':right_posts,
      'left_posts':left_posts,
        'sp':sp,  
       'last_post':last_post, 
       'ri_post':ri_post,
        'ce_post':ce_post,
        'le_post':le_post,   
          }
   return render(request,'blog/post_lists.html', context)
  




def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    Sociallink=Social_link.objects.all()
    faq_list = post.faqs.all()

#پردازش متن با beaut Sociallinkifulsoup
    soup=BeautifulSoup(post.text , 'html.parser')

    toc=[]

    for tag in soup.find_all(['h2','h3']):
       anchor = re.sub(r'[^a-zA-Z0-9\-]','-', tag.get_text().strip())[:50]
       tag['id']=anchor
       

       toc.append({
          "title": tag.get_text(),
            "id": anchor,
            "level": tag.name,
       })

    return render(request, "blog/post_detail.html", {
        "post": post,
        "toc": toc,
        "content": soup.prettify(),
        ' Sociallink':Sociallink,
        "faq_list": faq_list,
    })

    




class PostCreateView(generic.CreateView):
   form_class =  NEWPostForm 
   template_name = 'blog/post_create.html'
   context_object_name = 'form'



class PostUpdateView(generic.UpdateView):
 model = Post
template_name = 'blog/post_create.html'
context_object_name = 'form'
    



class PostDeleteView(generic.DeleteView):

    model = Post
    template_name = 'blog/post_delete.html'
    success_url = reverse_lazy('posts_list')



def type_posts(request, type_id):
   post_type =get_object_or_404(type , pk=type_id)
   posts =Post.objects.filter(post_type=post_type ,  status='pub').order_by('-date_time_created')    
   return render(request , 'blog/type_post.html', {'post_type':post_type, 'posts':posts})


