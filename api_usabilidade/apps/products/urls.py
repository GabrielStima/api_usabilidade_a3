from django.urls import path
from .views import ProductViewset
from rest_framework import routers

app_name = 'products'

router = routers.DefaultRouter()

urlpatterns = [
    path('products/', ProductViewset.as_view()),
    path('products/product/<uuid:pk>', ProductViewset.as_view())
]