from django.urls import path
from .views import UserViewset

urlpatterns = [
    path('users/', UserViewset.as_view()),
    path('users/user/<int:id>', UserViewset.as_view())
]