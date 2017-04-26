from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^process$', views.process),
    url(r'^login$', views.login),
    url(r'^home$', views.home),
    url(r'^logout$', views.logout),
    url(r'^add_friend/(?P<id>\d+)$', views.add_friend),
    url(r'^remove_friend/(?P<id>\d+)$', views.remove_friend),
    url(r'^user/(?P<id>\d+)$', views.profile),
]
