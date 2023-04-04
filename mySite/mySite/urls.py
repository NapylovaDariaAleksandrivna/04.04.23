#urls.py - объявления URL для этого проекта Django; 
# “оглавление” вашего сайта на базе Django


"""my_site URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from myApp import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from myApp import views
from django.http import HttpResponse #Импорт функции


urlpatterns = [
    
    path('', include('myApp.urls')),
    path('admin/', admin.site.urls),
    path('formpage/', views.form_name_view, name="form_name"),
]
