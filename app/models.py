from django.db import models

# Create your models here.

class Province(models.Model):
    name = models.CharField(max_length=60)
    
    class meta:
        verbose_name        = "Provincia"
        verbose_name_plural = "Provincia"
    
    def __str__(self):
        return f'{self.name}'
    
    
class City(models.Model):
    name      = models.CharField(max_length=60)
    zip_code  = models.CharField(max_length=10)
    province  = models.ForeignKey(Province,on_delete=models.CASCADE)
    latitude  = models.DecimalField(verbose_name='Latitud', name=None, max_digits=12, decimal_places=8, null=True)
    longitude = models.DecimalField(verbose_name='Longitud', name=None, max_digits=12, decimal_places=8)
    time_zone = models.IntegerField(blank=True, null=True)
    
    class meta:
        verbose_name        = "Ciudad"
        verbose_name_plural = "Ciudades"
        
    def __str__(self):
        return f'{self.name}'


class Airport(models.Model):
    name           = models.CharField(max_length=60)
    icao           = models.CharField(max_length=5)
    latitude       = models.DecimalField(verbose_name='Latitud', name=None, max_digits=12, decimal_places=8)
    longitude      = models.DecimalField(verbose_name='Longitud', name=None, max_digits=12, decimal_places=8)
    altitude_feets = models.IntegerField()
    time_zone      = models.IntegerField(blank=True, null=True)
    
    class meta:
        verbose_name        = "Aeropuerto"
        verbose_name_plural = "Aeropuertos"
    
    def __str__(self):
        return f'{self.name}'    


class CategoryIVA(models.Model):
    category_IVA = models.CharField(max_length=30)
    
    class meta:
        verbose_name        = "Categoría IVA"
        verbose_name_plural = "Categorías IVA"
    
    def __str__(self):
        return f'{self.category_IVA}'


class ClubType(models.Model):
    type = models.CharField(max_length=20)
    
    class meta:
        verbose_name        = "Tipo Club"
        verbose_name_plural = "Tipos de Clubs"
    
    def __str__(self):
        return f'{self.type}'
    

class Club(models.Model):
    name                = models.CharField(max_length=60)
    address             = models.CharField(max_length=60, blank=True, null=True)
    city                = models.ForeignKey(City,on_delete=models.SET_NULL, blank=True, null=True)
    airport             = models.ForeignKey(Airport,on_delete=models.CASCADE, blank=True, null=True)
    fee                 = models.DecimalField(verbose_name='Cuota', name=None, max_digits=12, decimal_places=2)
    balance_close_month = models.CharField(max_length=10)
    payment_message     = models.TextField(blank=True, null=True)
    cuit                = models.CharField(max_length=17, blank=True, null=True)
    category_IVA        = models.ForeignKey(CategoryIVA,on_delete=models.CASCADE, blank=True, null=True)
    name_logo           = models.CharField(max_length=25, blank=True, null=True)
    active              = models.BooleanField(default=True)
    season_date         = models.CharField(max_length=10, blank=True, null=True)
    type                = models.ForeignKey(ClubType,on_delete=models.CASCADE, blank=True, null=True)
    
    def __str__(self):
        return f'{self.name}'

