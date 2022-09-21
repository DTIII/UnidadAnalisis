from django.urls import path

from apps.oxxo.views import myfirstview


urlpatterns = [
   path('test/',myfirstview)
   
]