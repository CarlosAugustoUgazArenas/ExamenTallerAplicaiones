from os import path
from django.urls import path
import usuarios.views as v

urlpatterns = [
    path('', v.index ,name='usuarios'),
    path('crear_nuevo_usuario' , v.crear_nuevo_usuario) ,
    path('editar_usuario_<int:id>' , v.editar_usuario) ,
    path('detalles_usuario_<int:id>' , v.detalles_usuario) ,
    path('eliminar_usuario_<int:id>' , v.eliminar_usuario) ,
]