from django.conf.urls import url
from users import views

urlpatterns = [
    url(r'^login$', views.login),
    url(r'^logout$',views.logout),
    url(r'^register$',views.register),
    url(r'^info$',views.info),
    url(r'^change$',views.change_info),
    url(r'^profile$',views.watch_profile),
    ]