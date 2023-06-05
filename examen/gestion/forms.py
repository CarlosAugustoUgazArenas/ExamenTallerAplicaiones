from django.forms import ModelForm
from .models import Doctor
from .models import Paciente
from .models import Cita_medica

class DoctorForm(ModelForm) :
    class Meta :
        model = Doctor
        fields = '__all__'
        
class PacienteForm(ModelForm) :
    class Meta :
        model = Paciente
        fields = '__all__'

class CitaForm(ModelForm) :
    class Meta :
        model = Cita_medica
        fields = '__all__'
        