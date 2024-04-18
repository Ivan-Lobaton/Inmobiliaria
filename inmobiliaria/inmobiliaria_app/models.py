from django.db import models

# Choices for farm activities
TIPO_EDIFICIO_CHOICES = [
    ('residencial', 'Residencial'),
    ('comercial', 'Comercial'),
    ('oficinas', 'Oficinas'),
]

TIPO_CONSTRUCCION_CHOICES = [
    ('tradicional', 'Tradicional'),
    ('moderno', 'Moderno'),
]

ACTIVIDAD_CHOICES = [
    ('agricultura', 'Agricultura'),
    ('ganaderia', 'Ganadería'),
    ('mixto', 'Mixto'),
]

# Create your models here.
class Edificios(models.Model):
    nombre = models.CharField(max_length=255, verbose_name="Nombre del edificio", null=True)
    direccion = models.CharField(max_length=255, verbose_name="Dirección")
    tipoedificio = models.CharField(max_length=255, choices=TIPO_EDIFICIO_CHOICES, verbose_name="Tipo de edificio")
    estadoedificio = models.CharField(max_length=255, verbose_name="Estado del edificio")
    añoconstruccion = models.CharField(max_length=255, verbose_name="Año de construccion")
    
    def __str__(self):
        return self.nombre
    
    class Meta:
        verbose_name_plural = "Edificios"

class Casas(models.Model):
    barrio = models.CharField(max_length=255, verbose_name="Barrio", null=True)
    direccion = models.CharField(max_length=255, verbose_name="Dirección")
    numerohabitaciones = models.CharField(max_length=255, verbose_name="Número de habitaciones")
    añocontruccion = models.CharField(max_length=255, verbose_name="Año de construcción")
    tipocontruccion = models.CharField(max_length=255, choices=TIPO_CONSTRUCCION_CHOICES, verbose_name="Tipo de construcción")
    
    def __str__(self):
        return self.barrio
    
    class Meta:
        verbose_name_plural = "Casas"

class Fincas(models.Model):
    nombre = models.CharField(max_length=255, verbose_name="Nombre de la finca", null=True)
    tamañoterreno = models.CharField(max_length=255, verbose_name="Tamaño del terreno")
    actividad = models.CharField(max_length=255, choices=ACTIVIDAD_CHOICES, verbose_name="Actividad")
    infraestructura = models.CharField(max_length=255, verbose_name="Infraestructura")
    
    def __str__(self):
        return self.nombre
    
    class Meta:
        verbose_name_plural = "Fincas"

class Propietarios(models.Model):
    nombre = models.CharField(max_length=255, verbose_name="Nombre")
    apellido = models.CharField(max_length=255, verbose_name="Apellido", null=True)
    celular = models.CharField(max_length=255, verbose_name="Celular")
    cedula = models.CharField(max_length=255, verbose_name="Cedula")
    idedificios = models.ForeignKey(Edificios, on_delete=models.CASCADE, related_name="propietarios_edificios_list", verbose_name="Edificio en propiedad", null=True)
    idcasas = models.ForeignKey(Casas, on_delete=models.CASCADE, related_name="propietarios_casas_list", verbose_name="Casa en propiedad", null=True)
    idfincas = models.ForeignKey(Fincas, on_delete=models.CASCADE, related_name="propietarios_fincas_list", verbose_name="Finca en propiedad", null=True)
    
    def __str__(self):
        return self.nombre
    
    class Meta:
        verbose_name_plural = "Propietarios"
