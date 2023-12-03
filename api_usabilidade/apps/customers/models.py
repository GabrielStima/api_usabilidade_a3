from django.db import models

# Create your models here.
class Customer(models.Model):
    firstname = models.CharField(max_length=20, blank=False)
    lastname = models.CharField(max_length=50, blank=False)
    email = models.EmailField(blank=False)
    phone = models.BigIntegerField(blank=False)
    birthdate = models.DateField(blank=False)
    
    class Meta:
        verbose_name = 'Cliente'
        verbose_name_plural = 'Clientes'
        ordering =['id']

    def __str__(self):
        return self.first_name