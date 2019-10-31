from django.urls import path,re_path
from Buyer.views import *

urlpatterns = [
    re_path(r"^$",index),
    path('index/',index),
    re_path(r'goods/(?P<id>\d+)/',goods),
    path('goods_list/',goods_list),

]