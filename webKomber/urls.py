from django.conf.urls import url
from webKomber import views

urlpatterns = [
    # url(r'^map', views.tampil_map),
    url(r'^map/post', views.user_data_post)
]