from django.db import models
from usuarios.models import Usuario

# Create your models here.


class Tipodoc(models.Model):
    name = models.CharField(max_length=100, blank=False, null=False)

    class Meta:
        verbose_name = "documento"
        verbose_name_plural = "documentos"

    def __str__(self):
        return f'Tipodoc : { self.name }'

    # Create your models here.


class Tiposeguro(models.Model):
    name = models.CharField(max_length=100, blank=False, null=False)

    class Meta:
        verbose_name = "seguro"
        verbose_name_plural = "seguros"

    def __str__(self):
        return f'Tiposeguro : { self.name }'

    # Create your models here.


class Especialidad(models.Model):
    name = models.CharField(max_length=100, blank=False, null=False)

    class Meta:
        verbose_name = "especialidad"
        verbose_name_plural = "especialidades"

    def __str__(self):
        return f'Especialidad : { self.name }'

    # Create your models here.


class Doctor (models.Model):
    name = models.CharField(max_length=100, blank=False, null=False)
    direccion = models.CharField(max_length=200, blank=False, null=False)
    telefono = models.IntegerField()

    class Meta:
        verbose_name = "doctor"
        verbose_name_plural = "doctores"

    def __str__(self):
        return f'Doctor : { self.name }'

    # Create your models here.


class Paciente(models.Model):
    numdoc = models.IntegerField()
    tipodoc = models.ForeignKey(
        Tipodoc, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=100, blank=False, null=False)
    apellidos = models.CharField(max_length=100, blank=False, null=False)
    direccion = models.CharField(max_length=250, blank=False, null=False)
    tiposeguro = models.ForeignKey(
        Tiposeguro, on_delete=models.CASCADE, null=True, blank=True)

    class Meta:
        verbose_name = "pactiente"
        verbose_name_plural = "pacientes"

    def __str__(self):
        return f'Paciente : { self.name }'

    # Create your models here.


class Cita_medica(models.Model):
    paciente = models.ForeignKey(Paciente,on_delete=models.RESTRICT, null=True,blank=True)
    especialidad = models.ForeignKey(Especialidad,on_delete=models.RESTRICT, null=True,blank=True)
    doctor = models.ForeignKey(Doctor,on_delete=models.RESTRICT, null=True,blank=True)
    observaciones = models.CharField(max_length=250, blank=False, null=False)
    usuario = models.ForeignKey(Usuario,on_delete=models.RESTRICT, null=True,blank=True)

    class Meta:
        verbose_name = "cita"
        verbose_name_plural = "citas"

    def __str__(self):
        return f'Cita_medica : { self.paciente }'
