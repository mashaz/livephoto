from django.conf.urls import url
from django.contrib import admin
from comments import views

urlpatterns = [
    url(r'^$', views.comment_post),
]
