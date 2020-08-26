from django.conf.urls import url
from note import views

urlpatterns = [
    url(r'^api/note', views.note),
    url(r'^api/update/(?P<id>[0-9]+)$', views.update),
]