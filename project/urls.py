from django.contrib import admin
from django.urls import path, include
from investors.admin import investors_site

urlpatterns = [
    path('secret/', admin.site.urls),
    path('investors_admin/', investors_site.urls),
    path('', include('investors.urls')),
]
