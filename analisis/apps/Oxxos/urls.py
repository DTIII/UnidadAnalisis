from django.conf.urls import url, include

from apps.Oxxos.views import Index

urlpatterns = [
    url(r'^$', Index),
]