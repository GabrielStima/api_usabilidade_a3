from django.urls import path
from .views import CustomerViewset

urlpatterns = [
    path('customers/', CustomerViewset.as_view()),
    path('customers/customer/<uuid:id>', CustomerViewset.as_view())
]