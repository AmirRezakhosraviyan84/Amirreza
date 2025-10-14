from django.contrib import admin
from . models import Post,type,Social_link,FAQ
# Register your models here.
@admin.register(Post )
class PostAdmin(admin.ModelAdmin):
    list_display =('title','status','date_time_modified') 
    ordering =('status',)

@admin.register(type)

class typeAdmin(admin.ModelAdmin):
    list_display=['name', 'parent']


@admin.register(Social_link)    


class Social_linkAdmin(admin.ModelAdmin):

    list_display =['platform','title','url']
    list_filter = ("platform",)
    search_fields = ("title", "url")


@admin.register(FAQ)

class FAQAdmin(admin.ModelAdmin):
    list_display =['post']