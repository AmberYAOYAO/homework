"""DjangoFood URL Configuration

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
from django.urls import path,re_path,include
from django.views.decorators.csrf import csrf_exempt
from DjangoFood.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('news/',news),
    path("ckeditor/",include('ckeditor_uploader.urls'))

]
#
urlpatterns += [
    path('add_news/', add_news),
    path('add_foods/',add_foods),
    path('add_food_type/',add_food_type),
    path('add_shop/', add_shop),
    path('shop/', shop),
    re_path(r'shop_con/(?P<id>\d+)/', shop_con),
    re_path(r'news_con/(?P<id>\d+)/', news_con),
    path('rE/', requestExample),
    path('find_food/', find_food),
    path('agp/', ajax_get_page),
    path('agd/', ajax_get_data),
    path('app/', ajax_post_page),
    path('apd/', ajax_post_data),
    path('p_form/', p_form),
    path('setCookie/', setCookie),
    path('del_cookie/', del_cookie),
    path('login/', login),
    path('logout/', logout),
    path('beef/',beef),
    path('register/',register),
    path('vue/',vueExample),
    path('foods/',csrf_exempt(FoodView.as_view())),
    path('ajax_vue/',ajax_vue),
    path('meishi/',meishi),

]

from Foods.urls import router

urlpatterns += router.urls