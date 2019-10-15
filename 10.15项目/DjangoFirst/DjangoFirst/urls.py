"""DjangoFirst URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from DjangoFirst.views import index
from django.contrib import admin
from django.urls import path,re_path
from DjangoFirst.views import *
urlpatterns = [
    path('admin/', admin.site.urls),
    # path('index/',index),
    path('say_hello/',say_hello),
    path('demo/',demo),
    re_path('^birthday/(?P<d1>.+)/(?P<d2>.+)/',birthday),
    re_path('get_birthday/(?P<month>\d{2})/(?P<day>\d{2})/',get_birthday),
    path('index1/', index1),
    path('in_page/', in_page),
    path('dog/',dog),
    path('shop/',shop),
    path('beef/',beef),
    path('band/',band),
    path('food/',food),
    path('news/',news),
    path('about/',about),
    path('meishicon/',meishicon),
    path('newscon/',newscon),
    path('shopcon/',shopcon)
]
