from django.urls import path
#from analisis.apps.Oxxos.views import OxxoList
#from analisis.apps.Oxxos.views import AltaOxxo_view

from apps.Oxxos.views import Index, OxxosList

urlpatterns = [
    path('', Index, name='Index'),
    path('lista', OxxosList.as_view(), name='lista')
]