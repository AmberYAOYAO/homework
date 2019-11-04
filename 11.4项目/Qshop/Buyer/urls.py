from django.urls import path,re_path
from Buyer.views import *

urlpatterns = [
    path('index/',index),
    re_path(r'goods/(?P<id>\d+)/',goods),
    path('goods_list/',goods_list),
    path('cart/',cart),
    path('login/',login),
    path('logout/',logout),
    path('register/',register),
    re_path(r"^$",index),
    path('place_order/',place_order),
    path('goods_list/',goods_list),
    path('get_pay/',get_pay),
    path('pay_result/',pay_result),
    path('user_site/',user_site),
    path('user_order/',user_order),
    path('user_info/',user_info),
    path('add_car/',add_car),


]