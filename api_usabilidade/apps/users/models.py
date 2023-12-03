from django.db import models

# Create your models here.
class User(models.Model):
    first_name = models.CharField(max_length=20, blank=False)
    last_name = models.CharField(max_length=50, blank=False)
    email = models.EmailField(blank=False)
    cell_phone = models.BigIntegerField(blank=False)
    birth_date = models.DateField(blank=False)
    profile = models.CharField(max_length=20, blank=False)

    class Meta:
        verbose_name = 'Usuario'
        verbose_name_plural = 'Usuarios'
        ordering =['id']

    def __str__(self):
        return self.first_name