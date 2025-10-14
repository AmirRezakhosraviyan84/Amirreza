from django.contrib import admin
from .views import adminlogin, dashboard, admin_logout 


# حالا میتونیم ازش استفاده کنیم
admin.site.login = adminlogin

