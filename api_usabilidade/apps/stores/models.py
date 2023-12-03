from django.db import models
from customers.models import Customer
import uuid

# Create your models here.
class Store(models.Model):
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    name = models.CharField(max_length=20, blank=False)
    cnpj = models.IntegerField(unique=True, blank=False)
    address = models.CharField(max_length=50, blank=False)
    customer_id = models.ForeignKey(Customer, on_delete=models.CASCADE)     # Quando o customer for deletado, STORE também será


    class Meta:
        verbose_name = 'Loja'
        verbose_name_plural = 'Lojas'
        ordering =['id']

    def __str__(self):
        return self.store_name