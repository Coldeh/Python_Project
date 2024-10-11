"""
URL configuration for three_phase project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from client.views import *
from vendor.views import *
from admin_sector.views import *

urlpatterns = [
    path('admin/', admin.site.urls),

    #registration urls
    path('client_register/',clientreg,name='client_registration'),
    path('vendor_register/',vendor_reg,name='vendor_registration'),
    path('admin_register/',admin_reg,name='admin_registration'),


    #client urls
    path('client_login/',client_login,name='client_login'),
    path('client_logout/', client_logout,name='client_logout'),
    path('welcome/',welcome,name='client_dashboard'),

    #admin urls
    path('admin_login/',admin_login,name='admin_login'),
    path('admin_logout/',admin_logout,name='admin_logout'),
    path('admin_welcome/',admin_welcome,name='admin_welcome'),

    #vendor urls
    path('vendor_login/',vendor_login,name='vendor_login'),
    path('vendor_logout/',vendor_logout,name='vendor_logout'),
    path('vendor_welcome/',vendor_welcome,name='vendor_welcome'),

]
