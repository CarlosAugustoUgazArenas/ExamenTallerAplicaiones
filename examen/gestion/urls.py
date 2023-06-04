from os import path
from django.urls import path
import gestion.views as v

urlpatterns = [
    path('gestion/', v.index ,name='indexGestion'),
]