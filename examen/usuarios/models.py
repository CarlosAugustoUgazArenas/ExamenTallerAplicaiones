from django.db import models

# Create your models here.

class Usuario(models.Model) :
    name = models.CharField(max_length = 120 , blank = False , null = False)
    email = models.CharField(max_length = 220 ,blank = False , null = False)
    telefono = models.IntegerField(blank = False , null = True)
    
    class Meta : 
        verbose_name = "usuario"
        verbose_name_plural = "usuarios"
    
    def __str__(self) :
        return f'Usuario : { self.name }'