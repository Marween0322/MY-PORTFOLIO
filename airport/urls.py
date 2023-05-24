from django.contrib import admin
from django.urls import path, include
from django.views.generic.base import TemplateView # new

urlpatterns = [
    path('', include('myapp.urls')),
    path('admin/', admin.site.urls),
    
]
