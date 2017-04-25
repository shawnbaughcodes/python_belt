
from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^register_user$', views.register_user),
    url(r'^login$', views.login),
    url(r'^dashboard$', views.dashboard),
    url(r'^process_quote$', views.process_quote),
    url(r'^user_info$', views.user_info),
]
