from django.db import models
from stores.models import Store

# Create your models here.
class Product(models.Model):
    title = models.CharField(max_length=30, blank=False)
    description = models.TextField(max_length=100, blank=False)
    category = models.CharField(max_length=15, blank=False)
    brand = models.CharField(max_length=30, blank=False)
    price = models.IntegerField(blank=False)
    stock = models.IntegerField(blank=False)
    store = models.ForeignKey(Store, on_delete=models.CASCADE)     # Quando o store for deletado, PRODUCT também será

    class Meta:
        verbose_name = 'Produto'
        verbose_name_plural = 'Produtos'
        ordering =['id']

    def __str__(self):
        return self.title