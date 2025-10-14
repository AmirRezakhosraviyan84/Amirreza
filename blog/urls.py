from django.urls import path
from .views import  Post_list_view, type_posts,post_detail

urlpatterns = [
    path('posts/',Post_list_view, name='posts_list'), 
    path('type/<int:pk>/',  type_posts , name ='type'),
    path('datail/<int:pk>/', post_detail , name ='post_detail'),
    
    
]
