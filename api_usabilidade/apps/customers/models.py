from django.db import models

# Create your models here.
class Customer(models.Model):
    first_name = models.CharField(max_length=20, blank=False)
    last_name = models.CharField(max_length=50, blank=False)
    email = models.EmailField(blank=False)
    cell_phone = models.BigIntegerField(blank=False)
    birth_date = models.DateField(blank=False)
    
    class Meta:
        verbose_name = 'Cliente'
        verbose_name_plural = 'Clientes'
        ordering =['id']

    def __str__(self):
        return self.first_name