from django.urls import path
from .views import CustomerViewset

urlpatterns = [
    path('customers/', CustomerViewset.as_view()),
    path('customers/customer/<uuid:pk>', CustomerViewset.as_view())
]