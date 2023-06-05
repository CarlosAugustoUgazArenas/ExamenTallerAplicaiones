from django.shortcuts import get_object_or_404, redirect, render
from gestion.models import Doctor
from gestion.forms import DoctorForm
from gestion.models import Cita_medica
from gestion.models import Paciente

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
            'doctores' : doctor
        }
    )
def indexCita(request) :
    cita = Cita_medica.objects.all()
    return render(
        request , 'gestion/indexCita.html' , 
        {
            'citas' : cita
        }
    )
def indexPaciente(request) :
    paciente = Paciente.objects.all()
    return render(
        request , 'gestion/indexPaciente.html' , 
        {
            'pacientes' : paciente
        }
    )
    
def crear_nuevo_doctor(request):
    formulario = DoctorForm(request.POST)
    if formulario.is_valid():
        formulario.save()
        return redirect('indexDoctor')
    else:
        formulario = DoctorForm()
    return render(request, 'gestion/crear_nuevo_Doctor.html',{'formularioDoc': formulario})

def detalles_doctor(request, id):
    doctor = get_object_or_404(Doctor, pk=id)
    return render(
        request, 'gestion/detalles_doctor.html',
        {
            'doctor': doctor
        }
    )


def crear_nuevo_doctor(request):
    formulario = DoctorForm(request.POST)
    if formulario.is_valid():
        formulario.save()
        return redirect('indexDoctor')
    else:
        formulario = DoctorForm()
    return render(request, 'gestion/crear_nuevo_doctor.html',{'formulario': formulario})


def editar_doctor(request, id):
    doctor = get_object_or_404(Doctor, pk=id)

    if request.method == "POST":
        doctor_form = DoctorForm(request.POST, instance=doctor)
        if doctor_form.is_valid():
            doctor_form.save()
            return redirect('indexDoctor')
    else:
        doctor_form = DoctorForm(instance=doctor)

    return render(
        request, 'gestion/editar_doctor.html',
        {
            'doctor_form': doctor_form
        }
    )

def eliminar_doctor(request, id):
    doctor = get_object_or_404(Doctor, pk=id)

    if doctor:
        doctor.delete()

    return redirect('indexDoctor')