from django.shortcuts import render
from .models import Cita_medica

# Create your views here.
def index(request) :
    citas = Cita_medica.objects.all()
    return render(
        request , 'gestion/index.html' , 
        {
            'citas' : citas
        }
    )