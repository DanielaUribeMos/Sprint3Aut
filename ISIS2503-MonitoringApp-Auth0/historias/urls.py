from django.urls import path
from django.views.decorators.csrf import csrf_exempt
from django.conf.urls import include

from . import views

urlpatterns = [
    path('historias/', views.historia_list, name='historiaList'),
    path('historia/<id>', views.single_historia, name='singleHistoria'),
    path('historiacreate/', csrf_exempt(views.historia_create), name='historiaCreate'),
]
