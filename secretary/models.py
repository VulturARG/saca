################################################################################
#                             Made by Luis Briones
################################################################################

from django.db import models
from django.contrib.auth.models import User, Group
from django.core.validators import RegexValidator
from app.models import Club, City, Province

# Create your models here.

class Person(models.Model):
    name            = models.CharField('Nombre',max_length=60, blank=True, null=True)
    last_name       = models.CharField(max_length=60)
    document_type   = models.CharField(max_length=15, blank=True, null=True)
    document_number = models.CharField(max_length=15, blank=True, null=True)
    address         = models.CharField(max_length=60, blank=True, null=True)
    city            = models.ForeignKey(City,on_delete=models.SET_NULL, blank=True, null=True,verbose_name="Ciudad")
    province        = models.ForeignKey(Province,on_delete=models.SET_NULL, blank=True, null=True)
    birthday        = models.DateField(blank=True, null=True)
    birthday_place  = models.CharField(max_length=60, blank=True, null=True)
    citizenship     = models.CharField(max_length=20, blank=True, null=True)
    job             = models.CharField(max_length=60, blank=True, null=True)
    email           = models.EmailField(blank=True, null=True)
    cuit            = models.CharField(max_length=17, blank=True, null=True)
    categoryIVA     = models.CharField(max_length=25, blank=True, null=True)
    
    class meta:
        verbose_name        = "Persona"
        verbose_name_plural = "Personas"
    
    def __str__(self):
        return self.last_name if self.name is None else f'{self.last_name}, {self.name}'


class Pilot(models.Model):
    person                             = models.OneToOneField(Person,on_delete=models.CASCADE)
    file_number                        = models.CharField(max_length=10, blank=True, null=True)
    aircraft_license_type              = models.CharField(max_length=15, blank=True, null=True)
    aircraft_license_number            = models.CharField(max_length=15, blank=True, null=True)
    instructor_aircraft_license_number = models.CharField(max_length=15, blank=True, null=True)
    glider_license_type                = models.CharField(max_length=15, blank=True, null=True)
    glider_license_number              = models.CharField(max_length=15, blank=True, null=True)
    instructor_glider_license_number   = models.CharField(max_length=15, blank=True, null=True)
    is_VFR                             = models.BooleanField(default=True, blank=True, null=True)
    is_IFR                             = models.BooleanField(default=False, blank=True, null=True)
    night_habilitation                 = models.BooleanField(default=False, blank=True, null=True)
    is_single_engine                   = models.BooleanField(default=True, blank=True, null=True)
    is_multi_engine                    = models.BooleanField(default=False, blank=True, null=True)
    is_tug                             = models.BooleanField(default=False, blank=True, null=True)
    is_turboprop                       = models.BooleanField(default=False, blank=True, null=True)
    psychophysical_until               = models.DateField(blank=True, null=True)
    
    class meta:
        verbose_name        = "Piloto"
        verbose_name_plural = "Pilotos"
    
    def __str__(self):
        return f'{self.file_number}'


class ActivePilot(models.Model):
    pilot = models.ForeignKey(Pilot,on_delete=models.CASCADE)
    club  = models.ForeignKey(Club,on_delete=models.CASCADE)
    
    class meta:
        verbose_name        = "Piloto Activo"
        verbose_name_plural = "Pilotos Activos"
    
    def __str__(self):
        return f'{self.pilot} {self.club}'
    
  
class PartnerType(models.Model):
    type = models.CharField(max_length=25, blank=True, null=True)
    
    class meta:
        verbose_name        = "Tipo Socio"
        verbose_name_plural = "Tipo Socios"
    
    def __str__(self):
        return f'{self.partner}'


class Partner(models.Model):
    number         = models.IntegerField(blank=True, null=True)
    person         = models.ForeignKey(Person,on_delete=models.CASCADE)
    pilot          = models.ForeignKey(Pilot,on_delete=models.SET_NULL, blank=True, null=True)
    date_admission = models.DateField(blank=True, null=True)
    act_number     = models.IntegerField(blank=True, null=True)
    type           = models.ForeignKey(PartnerType,on_delete=models.SET_NULL, blank=True, null=True)
    club           = models.ForeignKey(Club,on_delete=models.CASCADE)
    presenter_1    = models.CharField(max_length=10, blank=True, null=True)
    presenter_2    = models.CharField(max_length=10, blank=True, null=True)
    user           = models.ForeignKey(User,on_delete=models.SET_NULL, blank=True, null=True)
    group          = models.ForeignKey(Group,on_delete=models.SET_NULL, blank=True, null=True)
    
    class meta:
        verbose_name        = "Socio"
        verbose_name_plural = "Socios"
    
    def __str__(self):
        return f'{self.number}'


class Leave(models.Model):
    partner    = models.OneToOneField(Partner,on_delete=models.CASCADE)
    date       = models.DateField(blank=True, null=True)
    act_number = models.IntegerField(blank=True, null=True)
    reason     = models.CharField(max_length=25, blank=True, null=True)

    class meta:
        verbose_name        = "Baja"
        verbose_name_plural = "Bajas"
    
    def __str__(self):
        return f'{self.partner}'


class Phone(models.Model):
    person       = models.ForeignKey(Person,on_delete=models.CASCADE)
    type         = models.CharField(max_length=20, blank=True, null=True)
    phone_number = models.CharField(max_length=20)
    
    class meta:
        verbose_name        = "Teléfono"
        verbose_name_plural = "Teléfonos"
    
    def __str__(self):
        return f'{self.phone_number}'


################################################################################
#                             Made by Luis Briones
################################################################################
    
'''
class PhoneField(MultiValueField):
    def __init__(self, **kwargs):
        # Define one message for all fields.
        error_messages = {
            'incomplete': 'Enter a country calling code and a phone number.',
        }
        # Or define a different message for each field.
        fields = (
            CharField(
                error_messages={'incomplete': 'Enter a country calling code.'},
                validators=[
                    RegexValidator(r'^[0-9]+$', 'Enter a valid country calling code.'),
                ],
            ),
            CharField(
                error_messages={'incomplete': 'Enter a phone number.'},
                validators=[RegexValidator(r'^[0-9]+$', 'Enter a valid phone number.')],
            ),
            CharField(
                validators=[RegexValidator(r'^[0-9]+$', 'Enter a valid extension.')],
                required=False,
            ),
        )
        super().__init__(
            error_messages=error_messages, fields=fields,
            require_all_fields=False, **kwargs
        )
'''