from django.conf.urls import url
from django.urls import path
from webKomber import views

urlpatterns = [
    # url(r'^map', views.tampil_map),
    path('', views.index, name="index"),
    url(r'^map/post', views.user_data_post),
    url(r'^map/get', views.user_data_get, name="data"),
    url(r'^home', views.home, name="home")
]