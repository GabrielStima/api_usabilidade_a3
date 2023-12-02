from django.urls import path
from .views import StoreViewset

urlpatterns = [
    path('stores/', StoreViewset.as_view()),
    path('stores/store/<uuid:pk>', StoreViewset.as_view())
]