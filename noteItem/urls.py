from django.conf.urls import url
from noteItem import views

urlpatterns = [
    url(r'^api/rota', views.rota),
    url(r'^api/list/(?P<id>[0-9]+)$', views.note_detail),
]