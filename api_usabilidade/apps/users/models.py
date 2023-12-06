from django.db import models

# Create your models here.
class User(models.Model):
    firstname = models.CharField(max_length=30, blank=False)
    lastname = models.CharField(max_length=50, blank=False)
    email = models.EmailField(blank=False)
    phone = models.BigIntegerField(blank=False)
    birthdate = models.DateField(blank=False)
    profile = models.CharField(max_length=20, blank=False)

    class Meta:
        verbose_name = 'Usuario'
        verbose_name_plural = 'Usuarios'
        ordering =['id']

    def __str__(self):
        return self.firstname