from django.urls import path
from django.views.decorators.csrf import csrf_exempt
from django.conf.urls import url, include

from . import views

urlpatterns = [
    path('plantillas/', views.plantilla_list),
    path('plantillacreate/', csrf_exempt(views.plantilla_create), name='plantillaCreate'),
]