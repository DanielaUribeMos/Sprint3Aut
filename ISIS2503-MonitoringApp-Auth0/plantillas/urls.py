from django.urls import path
from django.views.decorators.csrf import csrf_exempt
from django.conf.urls import url, include

from . import plantilla

urlpatterns = [
    path('plantillas/', plantilla.plantilla_list),
    path('plantillacreate/', csrf_exempt(plantilla.plantilla_create), name='plantillaCreate'),
]