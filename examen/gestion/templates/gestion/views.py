from django.shortcuts import render
from .models import Doctor
from .models import Cita_medica
from .models import Paciente

# Create your views here.
def home(request) :    
    return render(
        request , 'gestion/homeGestion.html' , 
    )
    
def indexDoctor(request) :
    doctor = Doctor.objects.all()
    return render(
        request , 'gestion/indexDoctor.html' , 
        {
            'doctor' : doctor
        }
    )