from django.conf.urls import url
from django.contrib import admin
from photo import views

urlpatterns = [
    url(r'^upload$', views.upload),
    url(r'^delete$',views.delete),
    url(r'^show$',views.user_photo),
]
