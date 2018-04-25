from django.conf.urls import url
from . import views 

urlpatterns = [ 
    url(r'^$', views.index), 
    url(r'^register', views.register),
    url(r'login', views.login),
    url(r'success', views.success),
    url(r'^rev_create', views.rev_create), 
    url(r'^user/(?P<id>\d+)', views.uShow), #so confusing :(
    url(r'^fav_btn', views.fav_btn),
    url(r'^unfav_btn', views.unfav_btn),
    url(r'logout', views.logout)
    ]