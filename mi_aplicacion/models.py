from django.db import models

# Create your models here.
class Carrera(models.Model):
    MODALIDADES = [
        ('pre', 'Presencial'),
        ('mx', 'Mixta'),
        ('vr', 'Virtual'),        
    ]
#[('presencial', 'Presencial'), ('virtual', 'Virtual')]
    nombre = models.CharField(max_length=50)
    clave = models.CharField(max_length=15)
    modalidad = models.CharField(max_length=10, choices=MODALIDADES)
    
    def __str__(self):
        return f"{self.nombre} ({self.get_modalidad_display()})"

class Estudiante(models.Model):
    nombre = models.CharField(max_length=20)
    appat = models.CharField(max_length=20)
    apmat = models.CharField(max_length=20)
    matricula = models.CharField(max_length=9)
    curp = models.CharField(max_length=20)
    fotografia = models.ImageField(upload_to='fotografias/', blank=True, null=True)
    carrera = models.ForeignKey(Carrera, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.nombre} {self.appat} {self.apmat}"