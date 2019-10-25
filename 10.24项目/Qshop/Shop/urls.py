from django.urls import path,re_path
from Shop.views import *

urlpatterns = [
    re_path(r"^$",index),
    path("index/",index),
    path("register/",register),
    path("login/",login),
    path("logout/",logout),
    path("forget_password/",forget_password)


]