from django.conf.urls import url
from app.views import api

urlpatterns = [
    url(r'^', api),
]
