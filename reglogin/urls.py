from xml.etree.ElementInclude import include
from django.contrib import admin
from django.urls import path, include
from reglogin import views

urlpatterns = [
    path('', views.index, name=''),
   #path('', views.SignUpView, name='Signup'),
    path('login', views.login, name='login')
]