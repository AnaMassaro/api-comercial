from django.conf.urls import url
from people import views

urlpatterns = [
    url(r'^api/user', views.user),
    url(r'^api/hello', views.helloworld),
]