from django import forms
from . models import Post
class NEWPostForm(forms.ModelForm):
    
    class Meta:
      model = Post
      fields = ['title','text', 'author' , 'status']