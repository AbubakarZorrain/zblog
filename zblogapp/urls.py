from django.conf.urls import url
from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from django.urls import re_path

urlpatterns = [

path('',views.navbar, name="index"),
path('home/',views.navbar, name="index"),
path('accounts/login/',views.signin,name="login"),
    path('logout',views.logout_view),


]